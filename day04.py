#!/usr/bin/env python3

from hashlib import md5
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import sys

def advent_coin(key, count, start=1, stride=1):
    i = start
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
        i += stride

def advent_coin_multithreaded(key, count):
    cpus = multiprocessing.cpu_count()
    with ProcessPoolExecutor(max_workers=cpus) as executor:
        futures = [executor.submit(advent_coin, key, count, i + 1, cpus) for i in range(cpus)]
        return min([f.result() for f in futures])

if __name__ == '__main__':
    _, key, count = sys.argv
    count = int(count)
    print(advent_coin(key, count))
