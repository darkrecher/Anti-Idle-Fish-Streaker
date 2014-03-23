# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import wx

# initialisation du  contexte
app = wx.App(False)
screen = wx.ScreenDC()
object_size_screen = screen.GetSize()
size_screen = (object_size_screen[0], object_size_screen[1])
debug("La taille de l'écran est : %s" % str(size_screen))

class ScreenShot(object):

    def __init__(self, coord_upleft, size_screenshot):
        self.coord_upleft = coord_upleft
        self.size_screenshot = size_screenshot
        bmp = wx.EmptyBitmap(size_screenshot[0], size_screenshot[1])
        self.mem = wx.MemoryDC(bmp)
        self.mem.Blit(0, 0, size_screenshot[0], size_screenshot[1], screen, coord_upleft[0], coord_upleft[1])
        # TODO : ne pas sauvegarder ici, mais faire une fonction que le fait quand on a envie.
        bmp.SaveFile("J:\\Recher\\projets\\git\\Anti-Idle-Fish-Streaker\\screenshots\\paf.png", wx.BITMAP_TYPE_PNG)

