# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time
from my_logging import debug, info

import screen_shotter
import fish_line_detector
from fish_line_analyzer import FishLineAnalyzer, fst
from key_presser import KeyPresser

debug("coucou éé")
info("pouet")

DICT_DELAY_FROM_FISHING_STATE = {
    fst.HIGHLIGHTED : 0.5,
    fst.SIGNAL_SENT : 0.1,
    fst.WAIT_FISH : 0.1,
    fst.FISH_NEAR : 0.000001,
    fst.SEND_SIGNAL : 0.000001,
    fst.CRITICAL_ZONE_NOT_FOUND : 0.1,
}

fish_line_info = fish_line_detector.detect()
if fish_line_info is None:
    raise Exception("impossible de trouver la ligne de fishing à l'écran")

fish_line_analyzer = FishLineAnalyzer(*fish_line_info)
fst_prev = fst.HIGHLIGHTED

key_presser = KeyPresser("Firefox", 100, "a")

while True:

    fish_line_analyzer.analyze_screenshot()
    fish_line_analyzer.refresh_current_state()
    fst_cur = fish_line_analyzer.fst_cur

    if fst_prev != fst_cur:

        if fst_cur == fst.SEND_SIGNAL:
            key_presser.press_key()

        info(" ".join((
            str(fst.dictReverse[fst_prev]),
            "->",
            str(fst.dictReverse[fst_cur])
        )))
        fish_line_analyzer.log_current_info()
        info("")
        fst_prev = fst_cur

    time.sleep(DICT_DELAY_FROM_FISHING_STATE[fst_cur])
