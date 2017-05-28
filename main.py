#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime as dt
import fileinput as fi
import romanizator as r


def printline(string):
    print(string.strip())


if __name__ == '__main__':
    start = dt.now()

    r = r.Romanizator()
    romanized = []

    print('--- Original Text ---\n')
    for line in fi.input():
        printline(line)
        romanized.append(r.romanize(line))
    print()

    print('--- Romanized Text ---\n')
    for line in romanized:
        printline(line)
    print()

    end = dt.now()

    print('Time running: {}\n'.format(end - start))