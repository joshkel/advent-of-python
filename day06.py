#!/usr/bin/env python3

import fileinput
from pypeg2 import *
import numpy as np

class Coord(List):
    grammar = int, ',', int

class Range(List):
    grammar = Coord, 'through', Coord

    def slice(self, lights):
        x1, y1 = self[0]
        x2, y2 = self[1]
        return lights[x1:x2+1, y1:y2+1]

    def apply(self, lights, f):
        l = self.slice(lights)
        l[:] = f(l)

class ToggleCommand:
    grammar = 'toggle', attr('range', Range)

    def simple_action(self, lights):
        # For a bool, 1 - b is equivalent to not b
        self.range.apply(lights, lambda l: 1 - l)

    def fancy_action(self, lights):
        self.range.apply(lights, lambda l: l + 2)

class TurnOffCommand:
    grammar = 'turn off', attr('range', Range)

    def simple_action(self, lights):
        self.range.apply(lights, lambda l: False)

    def fancy_action(self, lights):
        self.range.apply(lights, lambda l: np.fmax(l - 1, 0))

class TurnOnCommand:
    grammar = 'turn on', attr('range', Range)

    def simple_action(self, lights):
        self.range.apply(lights, lambda l: True)

    def fancy_action(self, lights):
        self.range.apply(lights, lambda l: l + 1)

commands = [ToggleCommand, TurnOnCommand, TurnOffCommand]

def make_lights(dtype):
    return np.zeros((1000,1000), dtype=dtype)

if __name__ == '__main__':
    simple_lights = make_lights(np.bool)
    fancy_lights = make_lights(np.int32)

    for line in fileinput.input():
        cmd = parse(line, commands)
        cmd.simple_action(simple_lights)
        cmd.fancy_action(fancy_lights)

    print(simple_lights)
    print("Total lights (simple): %i" % np.sum(simple_lights))

    print(fancy_lights)
    print("Total lights (fancy): %i" % np.sum(fancy_lights))

