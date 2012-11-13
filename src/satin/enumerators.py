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

"""
Module for enumerating control hierarchy
"""

def iterate_widgets(widget):
    """
    Iterate over widget and collect all sub-widgets

    :param widget: widget to process
    :type widget: QWidget
    :return: generator to iterate through all widgets
    :rtype: generator
    """
    if hasattr(widget, 'itemAt'):
        for index in xrange(widget.count()):
            if hasattr(widget, 'itemAt'):
                generator = iterate_widgets(widget.itemAt(index))
                for sub_widget in generator:
                    yield sub_widget
    elif hasattr(widget, 'widget'):
        if widget != None:
            yield widget.widget()
    elif hasattr(widget, 'layout'):
        if widget.layout() != None:
            generator = iterate_widgets(widget.layout())
            for sub_widget in generator:
                yield sub_widget
        else:
            yield widget
    else:
        yield widget
