#!/usr/bin/env python3

import unittest

from day01 import elevator, when_floor
from day02 import parse_size, wrapping_paper, ribbon

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

class TestWrappingPaper(unittest.TestCase):
    def test_parse_size(self):
        self.assertEqual(parse_size('2x3x4'), (2,3,4))

    def test_wrapping_paper(self):
        self.assertEqual(wrapping_paper(parse_size('2x3x4')), 58)
        self.assertEqual(wrapping_paper(parse_size('1x1x10')), 43)

    def test_ribbon(self):
        self.assertEqual(ribbon(parse_size('2x3x4')), 34)
        self.assertEqual(ribbon(parse_size('1x1x10')), 14)

if __name__ == '__main__':
    unittest.main()
