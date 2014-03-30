# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import screen_shotter

class FishSublineAnalyzer(object):

    def __init__(self, y_line, x1_line, x2_line):
        self.y_line = y_line
        self.x1_line = x1_line
        self.x2_line = x2_line
        self.line_length = x2_line - x1_line + 1

    def analyze(self):
        self._make_screenshot_sub_line()
        self._reset_screenshot_values()
        self._process_screenshot()

    def _make_screenshot_sub_line(self):
        self.screenshot = screen_shotter.ScreenShot(
            (self.x1_line, self.y_line),
            (self.line_length, 1))

    def _reset_screenshot_values(self):
        self.x_critical_zone_1 = None
        self.x_critical_zone_2 = None

    def _process_screenshot(self):

        for x_line in range(self.line_length):
            red, grn, blu = self.screenshot.get_pixel_rgb((x_line, 0))

            if red == 0 and grn > 250 and blu > 250:
                if self.x_critical_zone_1 is None:
                    self.x_critical_zone_1 = x_line
                elif self.x_critical_zone_2 is None:
                    self.x_critical_zone_2 = x_line
                else:
                    raise Exception("trop de pixels de zone critique")

        debug(" ".join((
            "crit_zone_1:",
            str(self.x_critical_zone_1),
            "crit_zone_2:",
            str(self.x_critical_zone_2)
        )))

        if (self.x_critical_zone_1 is not None
            and self.x_critical_zone_2 is not None
            and self.x_critical_zone_1 != self.x_critical_zone_2-1):

            raise Exception("Pixels de zone critique pas adjacents.")

