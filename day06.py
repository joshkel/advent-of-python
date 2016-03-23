#!/usr/bin/env python3

from pypeg2 import *
import numpy as np

class Coord(List):
    grammar = int, ',', int

class Range(List):
    grammar = Coord, 'through', Coord

    def apply(self, lights, f):
        for i in range(self[0][0], self[1][0] + 1):
            for j in range(self[0][1], self[1][1] + 1):
                if callable(f):
                    lights[i][j] = f(lights[i][j])
                else:
                    lights[i][j] = f

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

lights = np.zeros((1000,1000), dtype=np.bool)
cmd = parse('toggle 0,0 through 999,999', commands)
cmd.action(lights)
print(lights)
print("Total lights: %i" % np.sum(lights))