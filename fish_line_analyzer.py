# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info
from enum import enum

import screen_shotter
import colrtool

FISHING_STATE = enum(

    "FISHING_STATE",

    # La couleur cyan n'est pas dominante.
    # On vient de capturer ou de rater un triangle, la zone de jeu
    # est donc en train de s'illuminer en vert ou en rouge.
    "HIGHLIGHTED",

    # Le triangle est passé sur la marque rouge, on l'a détecté,
    # et on a envoyé le signal.
    # Il faut attendre que la marque rouge se réactualise
    # (elle doit se déplacer à un autre endroit)
    "SIGNAL_SENT",

    # La marque rouge s'est réactualisée. On attend le triangle.
    # Soit il est pas là du tout, soit il est là, mais encore loin.
    "WAIT_FISH",

    # Le triangle est très proche. Il faut faire des screen shot très fréquent,
    # Afin de détecter le bon moment où le triangle passe sur la marque rouge.
    "FISH_NEAR",

    # Le triangle est pil poil sur la marque rouge. Il faut envoyer le signal.
    "SEND_SIGNAL",

    # La zone critique (celle dans laquelle le triangle doit se trouver,
    # lorsqu'on appuie sur une touche), n'a pas été trouvée à l'écran.
    # Alors qu'on aurait dû. (Un triangle est présent)
    "CRITICAL_ZONE_NOT_FOUND",
)
fst = FISHING_STATE

class FishLineAnalyzer(object):

    def __init__(self, y_line, x1_line, x2_line, fish_line_analyzer):
        self.y_line = y_line
        self.x1_line = x1_line
        self.x2_line = x2_line
        self.fish_line_analyzer = fish_line_analyzer
        self.line_length = x2_line - x1_line + 1

        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        self.cyan_dominant = False

        # Valeur initiale arbitraire à la con.
        # TODO : De plus, le nommage est à l'arrache.
        self.x_red_mark_defined = self.line_length + 50
        self.fst_cur = fst.HIGHLIGHTED

    def analyze(self):
        self._make_screenshot_main_line()
        self._reset_screenshot_values()
        self._process_screenshot()
        self._refresh_current_state()

    def get_current_info(self, with_diff=True):
        current_info = " ".join((
            "cyan_dom:", str(self.cyan_dominant),
            "red_mark:", str(self.x_red_mark_1),
            "x_red_mark_defined:", str(self.x_red_mark_defined),
            "x_triangle:", str(self.x_triangle)
        ))
        if with_diff:
            current_info = " ".join((current_info, self.get_current_diff()))
        return current_info

    def get_current_diff(self):
        if self.x_triangle is not None and self.x_red_mark_1 is not None:
            return "diff: " + str(abs(self.x_triangle - self.x_red_mark_1))
        else:
            return "diff: None"

    def _make_screenshot_main_line(self):
        self.screenshot = screen_shotter.ScreenShot(
            (self.x1_line, self.y_line),
            (self.line_length, 1))

    def _reset_screenshot_values(self):
        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        self.nb_cyan_pix = 0
        self.hue_diff_min = 361

    def _process_screenshot(self):

        for x_line in range(self.line_length):
            rgb_pix = self.screenshot.get_pixel_rgb((x_line, 0))
            # debug("rgb_pix: " + str(rgb_pix))

            if rgb_pix == (239, 12, 15):
                if self.x_red_mark_1 is None:
                    self.x_red_mark_1 = x_line
                elif self.x_red_mark_2 is None:
                    self.x_red_mark_2 = x_line
                else:
                    raise Exception("trop de pixels de marque rouge")

            elif rgb_pix == (0, 204, 255):
                self.nb_cyan_pix += 1

            else:
                hsv_pix = colrtool.hsv_from_rgb(*rgb_pix)
                # hue=35 : orange. C'est la couleur de la pointe du triangle.
                # TODO : foutre tous ces trucs dans des constantes.
                hue_diff = abs(hsv_pix[0] - 35)
                if hue_diff < 50 and self.hue_diff_min > hue_diff:
                    self.hue_diff_min = hue_diff
                    self.x_triangle = x_line

        if (self.x_red_mark_1 is not None
            and self.x_red_mark_2 is not None
            and self.x_red_mark_1 != self.x_red_mark_2-1):

            debug(str(self.x_red_mark_1) + ", " + str(self.x_red_mark_2))
            raise Exception("Les deux marques rouge ne sont pas adjacentes")

        if self.nb_cyan_pix < self.line_length / 2:
            self.cyan_dominant = False
        else:
            self.cyan_dominant = True

    def _refresh_current_state(self):

        if not self.cyan_dominant:
            self.fst_cur = fst.HIGHLIGHTED
            self.x_red_mark_defined = None
            return

        if self.x_red_mark_1 is not None:
            self.x_red_mark_defined = self.x_red_mark_1

        if self.x_triangle is None:
            # Le triangle n'est pas encore là.
            self.fst_cur = fst.WAIT_FISH
            return

        if self.x_red_mark_defined is None:
            # Problème. Le triangle est là, mais la marque rouge
            # n'a pas été trouvée. C'est parce qu'on a atteint un streak
            # assez haut, et la marque rouge n'est plus affichée à l'écran.
            # Il faut faire une autre capture d'écran, quelques pixels
            # en dessous, et repérér les pixels les plus cyan sur la ligne.
            self.fish_line_analyzer.analyze()
            if self.fish_line_analyzer.x_critical_zone_1 is not None:
                # TODO : line too long.
                self.x_red_mark_defined = self.fish_line_analyzer.x_critical_zone_1
            else:
                self.fst_cur = fst.CRITICAL_ZONE_NOT_FOUND
                return

        # Arrivé ici, on est sur que x_red_mark_defined et x_triangle sont
        # différents de None. Donc on peut faire des calculs avec.
        if (self.x_red_mark_defined == self.x_triangle):
            # TODO TEST :or self.x_red_mark_defined == self.x_triangle - 1):
            # TODO : ça ne marche pas à 100%, et je ne comprends pas bien
            # pourquoi. Je crois que je m'en tamponne et que je vais pas
            # chercher. Ça devrait être suffisant pour atteindre
            # le fameux streak de 20.

            # On est dessus. Envoyez le signal ! (Sauf si déjà fait)
            if self.fst_cur == fst.SEND_SIGNAL:
                self.fst_cur = fst.SIGNAL_SENT
            else:
                self.fst_cur = fst.SEND_SIGNAL
            return

        else:

            # TODO : valeur de seuil complètement à l'arrache.
            if abs(self.x_triangle - self.x_red_mark_defined) < 20:
                # Le triangle est proche. Faut rafraîchir souvent.
                self.fst_cur = fst.FISH_NEAR
            else:
                # Le triangle est là, mais loin. Pas de quoi s'affoler.
                self.fst_cur = fst.WAIT_FISH












