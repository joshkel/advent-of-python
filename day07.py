#!/usr/bin/env python

import fileinput
import re


INT16_MAX = 0xffff

OPS = {
    'AND': int.__and__,
    'OR': int.__or__,
    'LSHIFT': int.__lshift__,
    'RSHIFT': int.__rshift__,
    'NOT': int.__invert__
}

OPS_RE = '|'.join(OPS.keys())



class Wire:
    def __init__(self, id):
        self.id = id

    def value(self, circuit):
        return circuit.get_value(self.id)


class Signal:
    def __init__(self, value):
        self._value = value

    def value(self, circuit):
        return self._value


class BinaryGate:
    def __init__(self, op, inputs):
        self.op = op
        self.inputs = inputs

    def value(self, circuit):
        return self.op(self.inputs[0].value(circuit), self.inputs[1].value(circuit))


class UnaryGate:
    def __init__(self, op, input):
        self.op = op
        self.input = input

    def value(self, circuit):
        return self.op(self.input.value(circuit)) & INT16_MAX


class Circuit:
    def __init__(self, cmd_list):
        self.circuit = {}
        for cmd in cmd_list:
            output, input = self.parse(cmd)
            self.circuit[output] = input
        self.cache = {}

    @staticmethod
    def parse_term(term):
        try:
            return Signal(int(term))
        except ValueError:
            return Wire(term)

    @classmethod
    def parse(cls, cmd):
        # Binary operators
        m = re.match(r'(\w+|\d+)\s+(%s)\s+(\w+|\d+)\s+->\s+(\w+)$' % OPS_RE, cmd)
        if m:
            return m.group(4), BinaryGate(OPS[m.group(2)], [cls.parse_term(m.group(1)), cls.parse_term(m.group(3))])

        # Unary operators
        m = re.match(r'(%s)\s+(\w+|\d+)\s+->\s+(\w+)$' % OPS_RE, cmd)
        if m:
            return m.group(3), UnaryGate(OPS[m.group(1)], cls.parse_term(m.group(2)))

        # Assignment
        m = re.match(r'(\w+|\d+)\s+->\s+(\w+)$', cmd)
        if m:
            return m.group(2), cls.parse_term(m.group(1))

        raise RuntimeError('Bad input %s' % cmd)

    def get_value(self, id):
        if id not in self.cache:
            self.cache[id] = self.circuit[id].value(self)
        return self.cache[id]


if __name__ == '__main__':
    cmd_list = [line.strip() for line in fileinput.input()]
    circuit = Circuit(cmd_list)
    print(circuit.get_value('a'))
