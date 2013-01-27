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

from PyQt4.QtGui import QApplication
from PyQt4 import QtCore

def satin_suite(cls):

    if hasattr(cls, 'setup'):
        cls.setup = setup(cls.setup)

    if hasattr(cls, 'teardown'):
        cls.teardown = teardown(cls.teardown)

    for key, attribute in cls.__dict__.items():
        if hasattr(attribute, '__call__') and 'test_' in key:
            setattr(cls, '_{0}'.format(key), getattr(cls, key))
            setattr(cls, '_wrapper_{0}'.format(key), get_wrapper(key))
            setattr(cls, key, get_test_step(key))

            getattr(cls, key).im_func.__name__ = getattr(cls, '_{0}'.format(key)).__name__
            getattr(cls, '_{0}'.format(key)).im_func.__name__ = '_{0}'.format(key)

    return cls

def setup(fn):
    def setup(self):
        self.qt_app = QApplication([])
        fn(self)
    return setup

def teardown(fn):
    def teardown(self):
        self.qt_app = None
        fn(self)
    return teardown

def get_wrapper(original_step):
    def _wrapper(self):
        getattr(self, '_{0}'.format(original_step))()
        self.qt_app.exit(0)
    return _wrapper

def get_test_step(original_step):
    def _step(self):
        timer = QtCore.QTimer()
        timer.setSingleShot(True)
        timer.start()

        timer.timeout.connect(getattr(self,
                                '_wrapper_{0}'.format(original_step)))

        self.qt_app.exec_()
    return _step

