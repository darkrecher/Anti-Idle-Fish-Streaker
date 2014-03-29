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
        # debug("pix_current_color : " + str(pix_current_color))
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
    coord_fish_line = find_first_color(
        # TODO : le X de la colonne à analyser est complètement à l'arrache.
        # il faudrait tester plusieurs colonnes, par dichotomie.
        screenshot, (900, 0), (0, +1),
        (0, 204, 255), "rgb", True)
    if coord_fish_line is None:
        info("Impossible de trouver la ligne de fishing")
        return None
    y_line = coord_fish_line[1]
    debug("y:" + str(y_line))

    # Ça va planter si y'a aucun pixel de la couleur cherchée, dans la ligne.
    # Pas supposée arriver puisqu'on vient de trouver un bon pixel dans cette
    # ligne là, juste avant.
    (x1_line, _) = find_first_color(
        screenshot, (0, y_line), (+1, 0),
        (0, 204, 255), "rgb", True)
    (x2_line, _) = find_first_color(
        screenshot, (screen_shotter.size_screen[0]-1, y_line), (-1, 0),
        (0, 204, 255), "rgb", True)
    debug("x1: " + str(x1_line) + " x2: " + str(x2_line))
    return (y_line, x1_line, x2_line)


