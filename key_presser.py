# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from my_logging import debug, info

import win32api
import win32com.client


class KeyPresser(object):

    def __init__(self, app_name, delay_init_time, char_key_to_press):
        self.char_key_to_press = char_key_to_press
        self.shell = win32com.client.Dispatch("WScript.Shell")
        self.shell.AppActivate(app_name)
        win32api.Sleep(delay_init_time)

    def press_key(self):
        self.shell.SendKeys(self.char_key_to_press)
