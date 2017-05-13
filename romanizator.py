#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Terminology: 

# 자음 or jaeum:    consonant
# 모음 or moeum:    vowel
# 밭침 or batchim:  final letter 
# 음절 or eumjeol:  block or syllable 

import korean.hangul as kr
import serialization as s
import sys

class Romanizator(object):

    def __init__(self):
        self.output = ''
        self.input = self.get_input(True)
        self.hangul = s.deserialize('data', 'hangul')

    def get_input(self, welcome=False):
        if welcome:
            print('Welcome to the Hangul->Latin Script Converter 0.9\n')

        print('Please insert the korean text and press CTRL + D:\n')

        return sys.stdin.read().split('\n')

    def jaeum(self, letter):
        return self.hangul['jaeum'].get(letter)

    def moeum(self, letter):
        return self.hangul['moeum'].get(letter)

    def batchim(self, letter, inicial_next=''):
        if letter == '':
            return ''

        return self.hangul['batchim'].get(letter)

    def romanize(self):
        output_romanized = list()

        for sentence in self.input:

            sentence_latin = ''
            syllables = list(sentence)

            for i, syllable in enumerate(syllables):

                if kr.is_hangul(syllable):
                    sentence_latin += self.jaeum(kr.get_initial(syllable))
                    sentence_latin += self.moeum(kr.get_vowel(syllable))
                    sentence_latin += self.batchim(kr.get_final(syllable))
                else:
                    sentence_latin += syllable

            sentence_latin = sentence_latin.strip()


            if len(sentence_latin) and not sentence_latin[0].isupper():
                sentence_latin = sentence_latin.capitalize()
            
            output_romanized.append(sentence_latin)

        self.output = output_romanized


    def print_output(self):
        print('\n☯  Romanized version ☯\n')

        for line in self.output:
            print(line)

if __name__ == "__main__":
    r = Romanizator()
    r.romanize()
    r.print_output()