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
Module for testing labels
"""
from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.wrap_matcher import wrap_matcher
from .enumerators import all_widgets

class LabelMatcher(BaseMatcher):
    """
    Check if Widget has label with given text
    """

    def __init__(self, text):
        """
        Default constructor
        """
        super(LabelMatcher, self).__init__()

        if hasattr(text, 'matches'):
            self.text = text
        else:
            self.text = wrap_matcher(text)

    def _matches(self, item):
        """
        Check if matcher matches item

        :param item: object to match against
        :returns: True if matching, otherwise False
        :rtype: Boolean
        """
        widgets = all_widgets(item)

        for widget in widgets:
            if hasattr(widget, 'text') and self.text.matches(widget.text()):
                return True

        return False

    def describe_to(self, description):
        """
        Describe this matcher
        """
        description.append('Control with label {0}'.format(self.text))

    def describe_mismatch(self, item, mismatch_description):
        """
        Describe this mismatch
        """
        mismatch_description.append(
                'QLabel with text {0} was not found'.format(self.text))

def has_label(text):
    """
    Check if Widget has label with given text
    """
    return LabelMatcher(text)
