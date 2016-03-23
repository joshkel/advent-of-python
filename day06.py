#!/usr/bin/env python3

import fileinput
from pypeg2 import *
import numpy as np

class Coord(List):
    grammar = int, ',', int

class Range(List):
    grammar = Coord, 'through', Coord

    def apply(self, lights, f):
        x1, y1 = self[0]
        x2, y2 = self[1]
        x2 += 1
        y2 += 1
        if not callable(f):
            (lights[x1:x2,y1:y2])[:] = f
            return
        for i in range(x1, x2):
            for j in range(y1, y2):
                lights[i][j] = f(lights[i][j])

class ToggleCommand:
    grammar = 'toggle', attr('range', Range)

    def action(self, lights):
        self.range.apply(lights, lambda l: not l)

class TurnOffCommand:
    grammar = 'turn off', attr('range', Range)

    def action(self, lights):
        self.range.apply(lights, False)

class TurnOnCommand:
    grammar = 'turn on', attr('range', Range)

    def action(self, lights):
        self.range.apply(lights, True)

commands = [ToggleCommand, TurnOnCommand, TurnOffCommand]

def make_lights():
    return np.zeros((1000,1000), dtype=np.bool)

if __name__ == '__main__':
    lights = make_lights()
    for line in fileinput.input():
        cmd = parse(line, commands)
        cmd.action(lights)
    print(lights)
    print("Total lights: %i" % np.sum(lights))

