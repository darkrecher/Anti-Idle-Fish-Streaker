# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
from my_logging import debug, info

import screen_shotter
import fish_line_detector
from fish_line_analyzer import FishLineAnalyzer, fst

debug("coucou éé")
info("pouet")


fish_line_info = fish_line_detector.detect()
if fish_line_info is None:
    raise SystemExit(1)

fish_line_analyzer = FishLineAnalyzer(*fish_line_info)
fst_prev = fst.HIGHLIGHTED

while True:

    fish_line_analyzer.analyze_screenshot()
    fish_line_analyzer.refresh_current_state()
    fst_cur = fish_line_analyzer.fst_cur

    if fst_prev != fst_cur:
        info(" ".join((
            str(fst.dictReverse[fst_prev]),
            "->",
            str(fst.dictReverse[fst_cur])
        )))
        fish_line_analyzer.log_current_info()
        info("")
        fst_prev = fst_cur

    # TODO : une valeur spécifique pour chaque état.
    if fst_cur == fst.FISH_NEAR:
        time.sleep(0.00001)
        #fish_line_analyzer.log_current_info()
    else:
        time.sleep(0.25)
