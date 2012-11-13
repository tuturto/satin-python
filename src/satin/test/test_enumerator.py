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
Tests for enumerators
"""
#pylint: disable=C0103, R0201
from PyQt4.QtGui import QApplication, QLabel, QHBoxLayout
from satin.enumerators import iterate_widgets

from hamcrest import assert_that, contains_inanyorder

class TestFindingWidgets(object):
    """
    Tests for enumerating widgets
    """
    def __init__(self):
        """
        Default constructor
        """
        super(TestFindingWidgets, self).__init__()
        self.application = None

    def setup(self):
        """
        Setup test case
        """
        self.application = QApplication([])

    def teardown(self):
        """
        Tear down the test case
        """
        self.application = None

    def test_enumerating_single_widget(self):
        """
        If there is only a single widget in hierarchy, it should be returned
        """
        label = QLabel()

        widgets = []
        for widget in iterate_widgets(label):
            widgets.append(widget)

        assert_that(widgets, contains_inanyorder(label))

    def test_enumerating_layout_with_widget(self):
        """
        If there is layout containing a widget, the widget should be returned
        """
        layout = QHBoxLayout()
        label = QLabel()

        layout.addWidget(label)

        widgets = []
        for widget in iterate_widgets(layout):
            widgets.append(widget)

        assert_that(widgets, contains_inanyorder(label))

    def test_layout_inside_layout(self):
        """
        Layout inside of layout should be treated like just a layout
        """
        outer_layout = QHBoxLayout()
        inner_layout = QHBoxLayout()
        label = QLabel()

        inner_layout.addWidget(label)
        outer_layout.addLayout(inner_layout)

        widgets = []
        for widget in iterate_widgets(outer_layout):
            widgets.append(widget)

        assert_that(widgets, contains_inanyorder(label))

    def test_mixed_layouts_and_widgets(self):
        """
        Mixing layouts and widgets at different levels
        """
        outer_layout = QHBoxLayout()
        inner_layout = QHBoxLayout()
        label_1 = QLabel('one')
        label_2 = QLabel('two')

        inner_layout.addWidget(label_1)
        outer_layout.addLayout(inner_layout)
        outer_layout.addWidget(label_2)

        widgets = []
        for widget in iterate_widgets(outer_layout):
            widgets.append(widget)

        assert_that(widgets, contains_inanyorder(label_1, label_2))
