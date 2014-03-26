# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import wx
from colrtool import hsv_from_rgb

# initialisation du  contexte
app = wx.App(False)
screen = wx.ScreenDC()
wxobj_size_screen = screen.GetSize()
size_screen = (wxobj_size_screen[0], wxobj_size_screen[1])
debug("La taille de l'écran est : %s" % str(size_screen))


class ScreenShot(object):

    def __init__(self, coord_upleft=(0, 0), size_screenshot=size_screen):
        # TODO : si coord_upleft + size_screenshot dépasse le coin inférieur
        # droit, ça plante. Donc il faudra créer un size_screenshot_corrected.
        self.coord_upleft = coord_upleft
        self.size_screenshot = size_screenshot
        self.bmp = wx.EmptyBitmap(size_screenshot[0], size_screenshot[1])
        self.mem = wx.MemoryDC(self.bmp)
        self.mem.Blit(
            0, 0,
            size_screenshot[0], size_screenshot[1],
            screen,
            coord_upleft[0], coord_upleft[1])
        # FUTURE :
        # Je garde comme variable membre self.bmp ET self.mem.
        # J'ai besoin du self.bmp pour la fonction save. Mais Est-ce bien
        # nécessaire ? On peut peut-être refaire un bmp à partir de self.mem.

    def save(self, path_file_save):
        self.bmp.SaveFile(path_file_save, wx.BITMAP_TYPE_PNG)

    def get_pixel_rgb(self, x_pix, y_pix):
        return self.mem.GetPixel(x_pix, y_pix)[0:3]

    def get_pixel_hsv(self, x_pix, y_pix):
        red, grn, blu = self.mem.GetPixel(x_pix, y_pix)[0:3]
        return hsv_from_rgb(red, grn, blu)


# Exemple d'utilisation / tests unitaires à l'arrache.
if __name__ == '__main__':
    DIR_SHOTS = ("J:\\Recher\\projets\\git\\"
                 "Anti-Idle-Fish-Streaker\\screenshots\\")
    screen_shot_mini = ScreenShot((50, 50), (200, 200))
    screen_shot_mini.save(DIR_SHOTS + "mini.png")
    screen_shot_big = ScreenShot()
    debug("color : " + str(screen_shot_big.get_pixel_rgb(49, 49)))
    debug("color : " + str(screen_shot_big.get_pixel_hsv(49, 49)))
    screen_shot_big.save(DIR_SHOTS + "big.png")
