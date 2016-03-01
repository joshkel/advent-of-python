#!/usr/bin/env python3

import unittest

from day01 import elevator

class TestElevator(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(elevator('(())'), 0)
        self.assertEqual(elevator('()()'), 0)

    def test_3(self):
        self.assertEqual(elevator('((('), 3)
        self.assertEqual(elevator('(()(()('), 3)

if __name__ == '__main__':
    unittest.main()
