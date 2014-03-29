# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import screen_shotter
import colrtool

class FishLineAnalyzer(object):

    def __init__(self, y_line, x1_line, x2_line):
        self.y_line = y_line
        self.x1_line = x1_line
        self.x2_line = x2_line
        self.line_length = x2_line - x1_line + 1

        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        # state_stable = True : la couleur cyan est dominante.
        # On attend un triangle, ou il y en a un en train de passer.
        # state_stable = False : la couleur cyan n'est pas dominante.
        # On vient de capturer ou de rater un triangle, la zone de jeu
        # est donc en train de s'illuminer en vert ou en rouge.
        self.state_stable = False

    def analyze(self):
        screenshot = screen_shotter.ScreenShot(
            (self.x1_line, self.y_line),
            (self.line_length, 1))

        self.x_red_mark_1 = None
        self.x_red_mark_2 = None
        self.x_triangle = None
        nb_cyan_pix = 0
        hue_diff_max = 0

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
                # hue=192 correspond au cyan (0, 204, 255)
                # TODO : foutre tous ces trucs dans des constantes.
                hue_diff = abs(hsv_pix[0] - 192)
                if hue_diff > 50 and hue_diff_max < hue_diff:
                    hue_diff_max = hue_diff
                    self.x_triangle = x_line

        if (self.x_red_mark_1 is not None
            and self.x_red_mark_2 is not None
            and self.x_red_mark_1 != self.x_red_mark_2-1):

            debug(str(self.x_red_mark_1) + ", " + str(self.x_red_mark_2))
            raise Exception("Les deux marques rouge ne sont pas adjacentes")

        if nb_cyan_pix < self.line_length / 2:
            self.state_stable = False
        else:
            self.state_stable = True

        debug(" ".join((
            "state_stable:", str(self.state_stable),
            "red_mark:", str(self.x_red_mark_1),
            "x_triangle", str(self.x_triangle)
        )))
