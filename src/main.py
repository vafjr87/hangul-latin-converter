#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import fileinput 
import romanizator as hr


# def printline(string):
#     print(string.strip())

def romanize(file):
    hangul = hr.HangulRomanizator()

    romanized = []
    for line in file:
        romanized.append(hangul.romanize(line))
    else:
        return romanized


def print_text(text, label):
    print(f'{label.upper()}:')

    for line in text:
        print(line.strip())
    else:
        print('\n')


if __name__ == '__main__':
    original = list(fileinput.input())
    romanized = romanize(fileinput.input())
    print_text(original, 'original')
    print_text(romanized, 'romanized')
