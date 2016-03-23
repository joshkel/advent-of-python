#!/usr/bin/env python3

from pypeg2 import *

class ToggleCommand(str):
    grammar = 'toggle'

    def action(self):
        print('Switcheroo!')

class TurnOffCommand(str):
    grammar = 'turn off'

    def action(self):
        print('Power off')

class TurnOnCommand(str):
    grammar = 'turn on'

    def action(self):
        print('Turn it on!')

Command = [ToggleCommand, TurnOnCommand, TurnOffCommand]

class Coord(List):
    grammar = int, ',', int

class Command(List):
    grammar = Command, Coord, 'through', Coord

result = parse('turn off 1,2 through 5,6', Command)
print(result)
result[0].action()
print(result[1][1])
