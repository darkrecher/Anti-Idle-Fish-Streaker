# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import colrtool
import screen_shotter



def find_first_color(
    screenshot, coord_start, coord_step,
    color_to_find, color_type, search_for_equality):
    """Parcourt une ligne ou une colonne de l'écran
    (ou autre chose de plus bizarre), et trouve le premier pixel
    correspondant / ne correspondant pas à une couleur spécifique."""

    # TODO : docstring meilleure que ça.
    # TODO : remplacer search_for_equality par une lambda qui prend
    #        2 couleurs en params et renvoie True/False.
    # TODO : check param sanity. coord_step != 0, 0. coord_start in rect, ...

    if color_type == "hsv":
        func_get_color = screenshot.get_pixel_hsv
    else:
        func_get_color = screenshot.get_pixel_rgb

    # TODO : trouver pourquoi cette andouille de sublime text affiche
    # mes "lambda" sur fond ROSE. argh !
    if coord_step[0] == 0:
        func_in_bounds_x = lambda(x) : True
    elif coord_step[0] < 0:
        func_in_bounds_x = lambda(x) : x >= 0
    else:
        func_in_bounds_x = lambda(x) : x < screen_shotter.size_screen[0]

    if coord_step[1] == 0:
        func_in_bounds_y = lambda(y) : True
    elif coord_step[1] < 0:
        func_in_bounds_y = lambda(y) : y >= 0
    else:
        func_in_bounds_y = lambda(y) : y < screen_shotter.size_screen[1]

    coord_cur = list(coord_start)
    while func_in_bounds_x(coord_cur[0]) and func_in_bounds_y(coord_cur[1]):

        pix_current_color = func_get_color(coord_cur)
        debug("pix_current_color : " + str(pix_current_color))
        if search_for_equality:
            if pix_current_color == color_to_find:
                return tuple(coord_cur)
        else:
            if pix_current_color != color_to_find:
                return tuple(coord_cur)

        coord_cur[0] += coord_step[0]
        coord_cur[1] += coord_step[1]

    return None


def detect():
    screenshot = screen_shotter.ScreenShot()
    # On parcourt la colonne du milieu de l'écran, on cherche le premier pixel
    # dont la couleur correspondrait à la ligne de fishing.
    a = find_first_color(
        screenshot, (640, 0), (0, +1),
        (0, 204, 255), "rgb", True)
    debug(a)


