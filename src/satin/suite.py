#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   Copyright 2012 Tuukka Turto
#
#   This file is part of satin-python.
#
#   pyherc is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   pyherc is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with satin-python.  If not, see <http://www.gnu.org/licenses/>.

import types
from PyQt4.QtGui import QApplication

def satin_suite(cls):

    if hasattr(cls, 'setup'):
        orig_setup = cls.setup
        cls.setup = _setup
        cls._setup = orig_setup

    if hasattr(cls, 'teardown'):
        orig_teardown = cls.teardown
        cls.teardown = _teardown
        cls._teardown = orig_teardown

    return cls

def _setup(self):
    self.qt_app = QApplication([])
    self._setup()

def _teardown(self):
    self.qt_app = None
    self._teardown()
