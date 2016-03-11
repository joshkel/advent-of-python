#!/usr/bin/env python3

from hashlib import md5
import sys

def advent_coin(key, count):
    i = 1
    key = key.encode('ascii')
    search = '0' * count
    m = md5()
    m.update(key)
    while True:
        m2 = m.copy()
        m2.update(str(i).encode('ascii'))
        digest = m2.hexdigest()
        if digest[:count] == search:
            return i
        i += 1

if __name__ == '__main__':
    _, key, count = sys.argv
    count = int(count)
    print(advent_coin(key, count))
