# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import wx

# initialisation du  contexte
app = wx.App(False)
screen = wx.ScreenDC()
wxobj_size_screen = screen.GetSize()
size_screen = (wxobj_size_screen[0], wxobj_size_screen[1])
debug("La taille de l'écran est : %s" % str(size_screen))

class ScreenShot(object):

    def __init__(self, coord_upleft, size_screenshot):
        self.coord_upleft = coord_upleft
        self.size_screenshot = size_screenshot
        self.bmp = wx.EmptyBitmap(size_screenshot[0], size_screenshot[1])
        self.mem = wx.MemoryDC(self.bmp)
        self.mem.Blit(
            0, 0,
            size_screenshot[0], size_screenshot[1],
            screen,
            coord_upleft[0], coord_upleft[1])
        # FUTURE : je garde comme variable membre self.bmp ET self.mem.
        #          Est-ce bien nécessaire ?

    def save(self, path_file_save):
        self.bmp.SaveFile(path_file_save, wx.BITMAP_TYPE_PNG)

    def get_pixel_rgb(self, x_pix, y_pix):
        return self.mem.GetPixel(x_pix, y_pix)[0:3]