#!/usr/bin/env python3

import unittest

from day01 import elevator, when_floor
from day02 import parse_size, wrapping_paper, ribbon
from day03 import dispatch_flight_path
from day04 import advent_coin
from day05 import is_nice1, is_naughty1, is_nice2, is_naughty2
from day07 import Circuit

class TestDay01(unittest.TestCase):
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

class TestDay02(unittest.TestCase):
    def test_parse_size(self):
        self.assertEqual(parse_size('2x3x4'), (2,3,4))

    def test_wrapping_paper(self):
        self.assertEqual(wrapping_paper(parse_size('2x3x4')), 58)
        self.assertEqual(wrapping_paper(parse_size('1x1x10')), 43)

    def test_ribbon(self):
        self.assertEqual(ribbon(parse_size('2x3x4')), 34)
        self.assertEqual(ribbon(parse_size('1x1x10')), 14)

class TestDay03(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(len(dispatch_flight_path('>')), 2)
        self.assertEqual(len(dispatch_flight_path('^>v<')), 4)
        self.assertEqual(len(dispatch_flight_path('^v^v^v^v^v')), 2)

    def test_with_robo_santa(self):
        self.assertEqual(len(dispatch_flight_path('^v', 2)), 3)
        self.assertEqual(len(dispatch_flight_path('^>v<', 2)), 3)
        self.assertEqual(len(dispatch_flight_path('^v^v^v^v^v', 2)), 11)

class TestDay04(unittest.TestCase):
    def test_simple(self):
        # Only do one test, for reasons of performance
        self.assertEqual(advent_coin('abcdef', 5), 609043)
        # self.assertEqual(advent_coin('pqrstuv', 5), 1048970)

class TestDay05(unittest.TestCase):
    def test_one(self):
        self.assertTrue(is_nice1('ugknbfddgicrmopn'))
        self.assertTrue(is_nice1('aaa'))
        self.assertTrue(is_naughty1('jchzalrnumimnmhp'))
        self.assertTrue(is_naughty1('haegwjzuvuyypxyu'))
        self.assertTrue(is_naughty1('dvszwmarrgswjxmb'))

    def test_two(self):
        self.assertTrue(is_nice2('qjhvhtzxzqqjkmpb'))
        self.assertTrue(is_nice2('xxyxx'))
        self.assertTrue(is_naughty2('uurcxstgmygtbstg'))
        self.assertTrue(is_naughty2('ieodomkazucvgmuy'))

class TestDay07(unittest.TestCase):
    commands = [
        '123 -> x',
        '456 -> y',
        'x AND y -> d',
        'x OR y -> e',
        'x LSHIFT 2 -> f',
        'y RSHIFT 2 -> g',
        'NOT x -> h',
        'NOT y -> i'
    ]

    def test_parses(self):
        for c in self.commands:
            self.assertTrue(Circuit.parse(c))

    def test_execute(self):
        circuit = Circuit(self.commands)
        self.assertEqual(circuit.get_value('x'), 123)
        self.assertEqual(circuit.get_value('y'), 456)
        self.assertEqual(circuit.get_value('d'), 72)
        self.assertEqual(circuit.get_value('e'), 507)
        self.assertEqual(circuit.get_value('f'), 492)
        self.assertEqual(circuit.get_value('g'), 114)
        self.assertEqual(circuit.get_value('h'), 65412)
        self.assertEqual(circuit.get_value('i'), 65079)

if __name__ == '__main__':
    unittest.main()

