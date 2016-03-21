#!/usr/bin/env python3

import fileinput
import re

def is_nice1(word):
    return bool(
        len(re.findall(r'[aeiou]', word)) >= 3 and
        re.search(r'([a-z])\1', word) and
        not re.search(r'ab|cd|pq|xy', word))

def is_naughty1(word):
    return not is_nice1(word)

def is_nice2(word):
    return bool(
        re.search(r'([a-z]{2}).*\1', word) and
        re.search(r'([a-z])[a-z]\1', word))

def is_naughty2(word):
    return not is_nice2(word)

if __name__ == '__main__':
    nice_count1 = 0
    nice_count2 = 0
    for line in fileinput.input():
        line = line.strip()
        if is_nice1(line):
            nice_count1 += 1
        if is_nice2(line):
            nice_count2 += 1
    print(nice_count1)
    print(nice_count2)
