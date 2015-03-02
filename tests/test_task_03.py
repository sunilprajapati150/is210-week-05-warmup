#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 03."""


# Import Python libs
import unittest


# Import user libs
import task_03


class Task03TestCase(unittest.TestCase):
    """Lesson 09, Task 03 tests"""

    def test_time_value(self):
        """Tests task_02.TIME value"""
        self.assertIs(task_03.JELLY, task_03.BUTTER)


if __name__ == '__main__':
    unittest.main()
