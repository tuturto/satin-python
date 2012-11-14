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
import satin

from hamcrest import assert_that, contains_inanyorder, is_, equal_to

class TestEnumeratingWidgets(object):
    """
    Tests for enumerating widgets
    """
    def __init__(self):
        """
        Default constructor
        """
        super(TestEnumeratingWidgets, self).__init__()
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

        assert_that(satin.all_widgets(label),
                    contains_inanyorder(label))

    def test_enumerating_layout_with_widget(self):
        """
        If there is layout containing a widget, the widget should be returned
        """
        layout = QHBoxLayout()
        label = QLabel()

        layout.addWidget(label)

        assert_that(satin.all_widgets(layout),
                    contains_inanyorder(label))

    def test_layout_inside_layout(self):
        """
        Layout inside of layout should be treated like just a layout
        """
        outer_layout = QHBoxLayout()
        inner_layout = QHBoxLayout()
        label = QLabel()

        inner_layout.addWidget(label)
        outer_layout.addLayout(inner_layout)

        assert_that(satin.all_widgets(outer_layout),
                    contains_inanyorder(label))

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

        assert_that(satin.all_widgets(outer_layout),
                    contains_inanyorder(label_1, label_2))

class TestFindingWidgets(object):
    """
    Tests for locating sub widget
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

    def test_finding_widget(self):
        """
        Test that a sub widget can be found
        """
        outer_layout = QHBoxLayout()
        inner_layout = QHBoxLayout()
        label_1 = QLabel('one')
        label_2 = QLabel('two')
        label_3 = QLabel('three')

        inner_layout.addWidget(label_1)
        inner_layout.addWidget(label_2)
        outer_layout.addLayout(inner_layout)
        outer_layout.addWidget(label_3)

        widget = satin.widget(outer_layout,
                              lambda control: control.text() == 'three')

        assert_that(widget, is_(equal_to(label_3)))
