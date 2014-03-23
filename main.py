# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import screen_shotter

debug("coucou éé")
info("pouet")

screen_shot = screen_shotter.ScreenShot((50, 50), (100, 100))
debug("shot taken")