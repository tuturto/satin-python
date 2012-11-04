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

def collect_widgets(widget):
    """
    Iterate over widget and collect all sub-widgets

    :param widget: widget to process
    :type widget: QWidget
    :return: list of widgets
    :rtype: [QWidget]
    """
    widgets = []

    if hasattr(widget, 'count'):
        for index in range(widget.count()):
            widgets.extend(collect_widgets(widget.itemAt(index)))
    elif hasattr(widget, 'widget'):
        widgets.append(widget.widget())
    elif hasattr(widget, 'layout'):
        widgets.extend(collect_widgets(widget.layout()))
    else:
        widgets.append(widget)

    return widgets
