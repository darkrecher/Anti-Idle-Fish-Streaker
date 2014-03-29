# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
from my_logging import debug, info

import screen_shotter
import fish_line_detector
from fish_line_analyzer import FishLineAnalyzer

debug("coucou éé")
info("pouet")


fish_line_info = fish_line_detector.detect()
if fish_line_info is None:
    raise SystemExit(1)

fish_line_analyzer = FishLineAnalyzer(*fish_line_info)

while True:
    fish_line_analyzer.analyze()
    time.sleep(0.5)
