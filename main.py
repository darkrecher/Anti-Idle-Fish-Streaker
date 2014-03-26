# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import screen_shotter

debug("coucou éé")
info("pouet")

screen_shot = screen_shotter.ScreenShot()
debug("shot taken")
debug("color : " + str(screen_shot.get_pixel_rgb(49, 49)))
debug("color : " + str(screen_shot.get_pixel_hsv(49, 49)))

