#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests for Task 02."""


# Import Python libs
import unittest


# Import user libs
import task_01.peanut
import task_02


class Task02TestCase(unittest.TestCase):
    """Lesson 09, Task 02 tests"""

    def test_time_value(self):
        """Tests task_02.TIME value"""
        self.assertIs(task_02.TIME, task_01.peanut.BUTTER)


if __name__ == '__main__':
    unittest.main()
