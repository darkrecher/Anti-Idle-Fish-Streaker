# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging

logging.basicConfig(format="%(levelname)s:%(message)s", level=logging.DEBUG)
logging.debug("log initialisé")

# Alias de fonction
debug = logging.debug
info = logging.info

