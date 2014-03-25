# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import screen_shotter

debug("coucou éé")
info("pouet")

screen_shot = screen_shotter.ScreenShot((50, 50), (200, 200))
debug("shot taken")
debug("color : " + str(screen_shot.get_pixel_rgb(49, 49)))
screen_shot.save("J:\\Recher\\projets\\git\\Anti-Idle-Fish-Streaker\\screenshots\\paf.png")
