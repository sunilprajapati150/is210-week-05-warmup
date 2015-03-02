#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests task 01."""


# Import Python libs
import unittest


# Import user libs
import task_01.peanut


class Task01TestCase(unittest.TestCase):
    """Task 01 tests"""

    def test_peanut_butter_is_truthy(self):
        """Tests task_01.peanut.BUTTER is truthy"""
        self.assertTrue(task_01.peanut.BUTTER)

    def test_peanut_oil_is_falsy(self):
        """Tests task_01.peanut.OIL is falsy"""
        self.assertFalse(task_01.peanut.OIL)


if __name__ == '__main__':
    unittest.main()
