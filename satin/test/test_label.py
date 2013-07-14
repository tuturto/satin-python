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
Tests for labels
"""
#pylint: disable=C0103, R0201
from PyQt4.QtGui import QApplication, QLabel
from PyQt4.QtSvg import QSvgWidget
from hamcrest import is_, equal_to, assert_that
from satin.label import LabelMatcher

class TestLabelMatching(object):
    """
    Test matching labels
    """
    def __init__(self):
        """
        Default constructor
        """
        super(TestLabelMatching, self).__init__()
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

    def test_matching_label(self):
        """
        Label with matching text is reported matching
        """
        label = QLabel(text = 'Intro')

        matcher = LabelMatcher(text = 'Intro')

        assert_that(matcher.matches(label), is_(equal_to(True)))

    def test_unmatching_label(self):
        """
        Label that does not match, should be reported as non-matching
        """
        label = QLabel(text = 'Description')

        matcher = LabelMatcher(text = 'Intro')

        assert_that(matcher.matches(label), is_(equal_to(False)))

    def test_non_label(self):
        """
        Widget without text property should not match or crash the system
        """
        widget = QSvgWidget()

        matcher = LabelMatcher(text = 'Intro')

        assert_that(matcher.matches(widget), is_(equal_to(False)))
