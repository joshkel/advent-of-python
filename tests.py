#!/usr/bin/env python3

import unittest

from day01 import elevator, when_floor

class TestElevator(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(elevator('(())'), 0)
        self.assertEqual(elevator('()()'), 0)

    def test_3(self):
        self.assertEqual(elevator('((('), 3)
        self.assertEqual(elevator('(()(()('), 3)

    def test_when_floor(self):
        self.assertEqual(when_floor(')', 0), 0)
        self.assertEqual(when_floor(')', -1), 1)
        self.assertEqual(when_floor('()())', -1), 5)
        self.assertEqual(when_floor('((', -1), None)

if __name__ == '__main__':
    unittest.main()
