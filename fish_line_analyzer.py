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
)
fst = FISHING_STATE

class FishLineAnalyzer(object):

    def __init__(self, y_line, x1_line, x2_line):
        self.y_line = y_line
        self.x1_line = x1_line
        self.x2_line = x2_line
        self.line_length = x2_line - x1_line + 1

        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        self.cyan_dominant = False

        # Valeur initiale arbitraire à la con.
        # De plus, le nommage est à l'arrache.
        self.x_red_mark_defined = self.line_length + 50
        self.fst_cur = fst.HIGHLIGHTED
        self.x_red_mark_1_prev = None # TODO : useless ??

    def analyze_screenshot(self):
        # TODO : séparer ça dans des fonctions plus petites.
        screenshot = screen_shotter.ScreenShot(
            (self.x1_line, self.y_line),
            (self.line_length, 1))

        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        nb_cyan_pix = 0
        hue_diff_min = 361

        for x_line in range(self.line_length):
            rgb_pix = screenshot.get_pixel_rgb((x_line, 0))
            # debug("rgb_pix: " + str(rgb_pix))

            if rgb_pix == (239, 12, 15):
                if self.x_red_mark_1 is None:
                    self.x_red_mark_1 = x_line
                elif self.x_red_mark_2 is None:
                    self.x_red_mark_2 = x_line
                else:
                    raise Exception("trop de pixels de marque rouge")

            elif rgb_pix == (0, 204, 255):
                nb_cyan_pix += 1

            else:
                hsv_pix = colrtool.hsv_from_rgb(*rgb_pix)
                # hue=35 correspond à l'orange = la pointe du triangle.
                # TODO : foutre tous ces trucs dans des constantes.
                hue_diff = abs(hsv_pix[0] - 35)
                if hue_diff < 50 and hue_diff_min > hue_diff:
                    hue_diff_min = hue_diff
                    self.x_triangle = x_line

        if (self.x_red_mark_1 is not None
            and self.x_red_mark_2 is not None
            and self.x_red_mark_1 != self.x_red_mark_2-1):

            debug(str(self.x_red_mark_1) + ", " + str(self.x_red_mark_2))
            raise Exception("Les deux marques rouge ne sont pas adjacentes")

        if nb_cyan_pix < self.line_length / 2:
            self.cyan_dominant = False
        else:
            self.cyan_dominant = True

    def log_current_info(self):
        info(" ".join((
            "cyan_dom:", str(self.cyan_dominant),
            "red_mark:", str(self.x_red_mark_1),
            "x_red_mark_defined:", str(self.x_red_mark_defined),
            "x_triangle", str(self.x_triangle)
        )))
        self.log_diff()

    def log_diff(self):
        if self.x_triangle is not None and self.x_red_mark_1 is not None:
            debug("diff " + str(abs(self.x_triangle - self.x_red_mark_1)))


    # TODO : Fonction interne. Et une fonction externe qui enchaine tout.
    def refresh_current_state(self):

        if not self.cyan_dominant:
            self.fst_cur = fst.HIGHLIGHTED
            self.x_red_mark_defined = None
            return

        if self.x_red_mark_1 is not None:
            self.x_red_mark_defined = self.x_red_mark_1

        # TODO : crap
        #if (self.x_red_mark_1_prev is None
        #    or abs(self.x_red_mark_1_prev-self.x_red_mark_1 > 1)):
        #
        #    # la marque vient de changer. On réactualise. À priori,
        #    # le triangle n'est pas encore là. Il arrivera plus tard.
        #    self.x_red_mark_1_prev = self.x_red_mark_1
        #    self.fst_cur = fst.WAIT_FISH
        #    return

        if self.x_triangle is None:
            # Le triangle n'est pas encore là.
            self.fst_cur = fst.WAIT_FISH
            return

        if self.x_red_mark_defined is not None:

            if (self.x_red_mark_defined == self.x_triangle
                or self.x_red_mark_defined == self.x_triangle + 1):

                # On est dessus. Envoyez le signal ! (Sauf si déjà fait)
                if self.fst_cur == fst.SEND_SIGNAL:
                    self.fst_cur = fst.SIGNAL_SENT
                else:
                    self.fst_cur = fst.SEND_SIGNAL
                return

            else:

                # TODO : valeur de seuil complètement à l'arrache.
                if abs(self.x_triangle - self.x_red_mark_defined) < 10:
                    # Le triangle est proche. Faut rafraîchir souvent.
                    self.fst_cur = fst.FISH_NEAR
                else:
                    # Le triangle est là, mais loin. Pas de quoi s'affoler.
                    self.fst_cur = fst.WAIT_FISH












