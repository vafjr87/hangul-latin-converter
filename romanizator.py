#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Terminology: 

# 자음 or jaeum:    consonant
# 모음 or moeum:    vowel
# 밭침 or batchim:  final letter 
# 음절 or eumjeol:  block or syllable

# Hangul sorting order
# ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
# ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㄹㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
# ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ

import korean.hangul as kr
import serialization as s
import sys

class Romanizator(object):
    """Class for romanization from Hangul to Latin"""
    def __init__(self):
        self.VERSION = 1.0
        self.output = ''
        self.input = self.get_input(True)
        self.hangul = s.deserialize('data', 'hangul')

    def get_input(self, welcome=False):
        """Get the text to convert

        :param welcome: boolean; to print the welcome message"""
        if welcome:
            print('Welcome to the Hangul->Latin Script Converter {version}\n'.format(version=self.VERSION))

        print('Please insert the korean text and press CTRL + D:\n')

        return sys.stdin.read().split('\n')

    def get_initial_next(self, syllables, i):
        """Get the initial letter of the next syllable of a word

        :param syllabes: list; syllables in Hangul
        :param i: int; the current index of the syllable in the sentence"""
        if i < (len(syllables) - 1):
            if syllables[i + 1] != '' and kr.is_hangul(syllables[i + 1]):
                return kr.get_initial(syllables[i + 1])

        return ''

    def get_final_prior(self, syllables, i):
        """Get the batchim of the prior syllable of a word

        :param syllabes: list; syllables in Hangul
        :param i: int; the current index of the syllable in the sentence"""
        if i > 0:
            if syllables[i - 1] != '' and kr.is_hangul(syllables[i - 1]):
                return kr.get_final(syllables[i - 1])

        return ''

    def is_double_batchim(self, batchim):
        """True if param is double batchim

        :param batchim: char; the final letter of a syllable"""
        return batchim in ['ㄳ', 'ㄵ', 'ㄶ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅄ'] 

    def split_double_batchim(self, batchim):
        """Split the double in a tuple

        :param batchim: char; the final letter of a syllable"""
        if batchim == 'ㄳ':
            return ('ㄱ', 'ㅅ')
        elif batchim == 'ㄵ':
            return ('ㄴ', 'ㅈ')
        elif batchim == 'ㄶ':
            return ('ㄴ', 'ㅎ')
        elif batchim == 'ㄺ':
            return ('ㄹ', 'ㄱ')
        elif batchim == 'ㄻ':
            return ('ㄹ', 'ㅁ')
        elif batchim == 'ㄼ':
            return ('ㄹ', 'ㅂ')
        elif batchim == 'ㄽ':
            return ('ㄹ', 'ㅅ')
        elif batchim == 'ㄾ':
            return ('ㄹ', 'ㅌ')
        elif batchim == 'ㄿ':
            return ('ㄹ', 'ㅍ')
        elif batchim == 'ㅀ':
            return ('ㄹ', 'ㅎ')
        elif batchim == 'ㅄ':
            return ('ㅂ', 'ㅅ')

        return ('', '')

    def jaeum(self, current, prior=''):
        """Convert a consonant to latin script following grammatical rules

        :param current: char; the initial consonant of a syllable
        :param prior: char; the final consonant of the prior syllable, if it exists"""
        if prior in ('ㄴ', 'ㄹ'):
            if current == 'ㄹ':
                return self.hangul['jaeum'].get('ㄹㄹ')

        elif prior in ('ㄶ', 'ㅀ', 'ㅎ',):
            if current == 'ㄱ':
                return self.hangul['jaeum'].get('ㅋ')
            elif current == 'ㄷ':
                return self.hangul['jaeum'].get('ㅌ')
            elif current == 'ㅂ':
                return self.hangul['jaeum'].get('ㅍ')
        elif current == 'ㅎ':
            if prior in ['ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ']:
                return ''

        return self.hangul['jaeum'].get(current)

    def moeum(self, letter):
        """Converts a vowel to latin script

        :param letter: char; the vowel of a syllable"""
        return self.hangul['moeum'].get(letter)

    def batchim(self, current, next=''):
        """Converts a final consonant to latin script following grammatical rules

        :param current: char; the final consonant of a syllable
        :param prior: char; the initial consonant of the next syllable, if it exists"""
        if current == '':
            return ''

        # ㅇ comes first because it's a special case 
        if next != '':
            if next == 'ㅇ':
                if current == 'ㅇ':
                    pass
                elif current in self.hangul['jaeum'].keys():
                    return self.jaeum(current)            
            elif self.is_double_batchim(current):
                return self.batchim(self.split_double_batchim(current)[0])

            elif next in ('ㄴ', 'ㅁ'):
                if current == 'ㅂ':
                    return self.jaeum('ㅁ')
        
            elif next in ('ㄱ', 'ㄷ', 'ㅂ'):
                if current == 'ㅎ':
                    return ''

            elif next == 'ㄹ':
                if current in ('ㄴ', 'ㄹ'):
                    return self.jaeum('ㄹㄹ')
            elif next == 'ㅎ':
                if current == 'ㄱ':
                    return self.jaeum('ㅋ')
                if current == 'ㄷ':
                    return self.jaeum('ㅌ')
                if current == 'ㅂ':
                    return self.jaeum('ㅍ')
                   
        return self.hangul['batchim'].get(current)

    def romanize(self):
        """Convert a list of sentences in Hangul to Latin Script"""
        output_romanized = list()

        for sentence in self.input:
            sentence_latin = ''
            syllables = list(sentence)

            for i, syllable in enumerate(syllables):

                if kr.is_hangul(syllable):
                    sentence_latin += self.jaeum(kr.get_initial(syllable),
                                        self.get_final_prior(syllables, i))
                    sentence_latin += self.moeum(kr.get_vowel(syllable))
                    sentence_latin += self.batchim(kr.get_final(syllable),
                                        self.get_initial_next(syllables, i))
                else:
                    sentence_latin += syllable

            sentence_latin = sentence_latin.strip()

            # capitalize the sentence only if the first letter is alpha
            if sentence_latin and not sentence_latin[0].isupper() \
            and sentence_latin[0].isalpha():
                    sentence_latin = sentence_latin.capitalize()
            
            output_romanized.append(sentence_latin)

        self.output = output_romanized


    def print_output(self):
        """Prints a converted text in terminal"""
        print('\n☯  Romanized version ☯\n')

        for line in self.output:
            print(line)

if __name__ == "__main__":
    r = Romanizator()
    r.romanize()
    r.print_output()