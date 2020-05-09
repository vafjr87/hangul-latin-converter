#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Terminology:

# 자음 or jaeum:         consonant
# 모음 or moeum:         vowel
# 밭침 or batchim:       final letter
# 쌍받침 or ssangbatchim: double final letter
# 음절 or eumjeol:       block or syllable

# Hangul sorting order
# ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ
# ㄱ ㄲ ㄴ ㄷ ㄸ ㄹ ㄹㄹ ㅁ ㅂ ㅃ ㅅ ㅆ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ
# ㄱ ㄲ ㄳ ㄴ ㄵ ㄶ ㄷ ㄹ ㄺ ㄻ ㄼ ㄽ ㄾ ㄿ ㅀ ㅁ ㅂ ㅄ ㅅ ㅆ ㅇ ㅈ ㅊ ㅋ ㅌ ㅍ ㅎ

from korean import hangul as kr

class HangulRomanizator(object):
    """Class for romanization from Hangul to Latin"""
    def __init__(self):
        jaeum = {
            'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt', 'ㄹ': 'r',
            'ㄹㄹ': 'l', 'ㅁ': 'm', 'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's', 'ㅆ': 'ss',
            'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj', 'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ': 't',
            'ㅍ': 'p', 'ㅎ': 'h'
        }

        moeum = {
            'ㅏ': 'a', 'ㅐ': 'ae', 'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e',
            'ㅕ': 'yeo', 'ㅖ': 'ye', 'ㅗ': 'o' , 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe',
            'ㅛ': 'yo', 'ㅜ': 'u', 'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu',
            'ㅡ': 'eu' , 'ㅢ': 'ui', 'ㅣ': 'i'
        }

        batchim = {
            'ㄱ': 'k', 'ㄲ': 'k', 'ㄳ': 'gs', 'ㄴ': 'n', 'ㄵ': 'nch', 'ㄶ': 'nh',
            'ㄷ': 't', 'ㄹ': 'l', 'ㄺ': 'lg', 'ㄻ': 'lm', 'ㄼ': 'lb', 'ㄽ': 'ls',
            'ㄾ': 'lt', 'ㄿ': 'lp', 'ㅀ': 'lh', 'ㅁ': 'm', 'ㅂ': 'p', 'ㅄ': 'ps',
            'ㅅ': 't', 'ㅆ': 't', 'ㅇ': 'ng', 'ㅈ': 't', 'ㅊ': 't', 'ㅋ': 'k',
            'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 't'
        }

        ssangbatchim = {
            'ㄳ': ('ㄱ', 'ㅅ'),  'ㄵ': ('ㄴ', 'ㅈ'), 'ㄶ': ('ㄴ', 'ㅎ'), 'ㄺ': ('ㄹ', 'ㄱ'), 
            'ㄻ': ('ㄹ', 'ㅁ'), 'ㄼ': ('ㄹ', 'ㅂ'), 'ㄽ': ('ㄹ', 'ㅅ'), 'ㄾ': ('ㄹ', 'ㅌ'), 
            'ㄿ': ('ㄹ', 'ㅍ'), 'ㅀ': ('ㄹ', 'ㅎ'), 'ㅄ': ('ㅂ', 'ㅅ')
        }

        self.__hangul = {
            'jaeum': jaeum,
            'moeum': moeum,
            'batchim': batchim,
            'ssangbatchim': ssangbatchim
        }

        self.hangul = self.__hangul

    def __get_initial_next(self, syllables, i):
        """Get the initial letter of the next syllable of a word

        :param syllabes: list; syllables in Hangul
        :param i: int; the current index of the syllable in the sentence"""
        if i < (len(syllables) - 1):
            if syllables[i + 1] != '' and kr.is_hangul(syllables[i + 1]):
                return kr.get_initial(syllables[i + 1])
    
        return ''


    def __get_final_prior(self, syllables, i):
        """Get the batchim of the prior syllable of a word

        :param syllabes: list; syllables in Hangul
        :param i: int; the current index of the syllable in the sentence"""
        if i > 0:
            if syllables[i - 1] != '' and kr.is_hangul(syllables[i - 1]):
                return kr.get_final(syllables[i - 1])

        return ''


    def is_ssangbatchim(self, batchim):
        """Return True if the batchim is double batchim"""

        # :param batchim: char; the final letter of a syllable
        return batchim in self.__hangul['ssangbatchim'].keys()


    def has_ssangbatchim(self, syllable):
        """Return True if the syllable contains a double batchim"""

        # :param syllable: char; a syllable
        if kr.is_hangul(syllable):
            return self.is_ssangbatchim(kr.get_final(syllable))
        else:
            return False


    def split_ssangbatchim(self, char):
        """Split the double batchim in a tuple"""

        # :param char: char; the final letter of a syllable or a syllable
        if char in self.__hangul['ssangbatchim'].keys():
            return self.__hangul['ssangbatchim'].get(char)
        else:
            return self.__hangul['ssangbatchim'].get(kr.get_final(char))


    def jaeum(self, syllable, prior=''):
        """Convert a consonant to latin script following grammatical rules"""

       # :param syllable: char; a hangul syllable
       # :param prior: char; the final consonant of the prior syllable, if it exists

        if syllable in self.__hangul['jaeum'].keys():
            current = syllable
        else:
            current = kr.get_initial(syllable)

        if prior in ('ㄴ', 'ㄹ'):
            if current == 'ㄹ':
                return self.__hangul['jaeum'].get('ㄹㄹ')

        elif prior in ('ㄶ', 'ㅀ', 'ㅎ',):
            if current == 'ㄱ':
                return self.__hangul['jaeum'].get('ㅋ')
            elif current == 'ㄷ':
                return self.__hangul['jaeum'].get('ㅌ')
            elif current == 'ㅂ':
                return self.__hangul['jaeum'].get('ㅍ')
        elif current == 'ㅎ':
            if prior in ['ㄷ', 'ㅅ', 'ㅆ', 'ㅈ', 'ㅊ', 'ㅌ']:
                return ''

        return self.__hangul['jaeum'].get(current)


    def moeum(self, syllable):
        """Convert a vowel to latin script"""

       # :param syllable: char; a hangul syllable
        if syllable in self.__hangul['moeum'].keys():
            return self.__hangul['moeum'].get(syllable)
        else:
            return self.__hangul['moeum'].get(kr.get_vowel(syllable))

    def batchim(self, syllable, next=''):
        """Convert a final consonant to latin script following grammatical rules"""

       # :param syllable: char; a hangul syllable
       # :param prior: char; the initial consonant of the next syllable, if it exists

        current = kr.get_final(syllable)

        if current == '':
            return ''

        # ㅇ comes first because it's a special case
        if next != '':
            if next == 'ㅇ':
                if current == 'ㅇ':
                    pass
                elif current in self.__hangul['jaeum'].keys():
                    return self.jaeum(current)
            elif self.is_ssangbatchim(current):
                return self.batchim(self.split_ssangbatchim(current)[0])

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

        return self.__hangul['batchim'].get(current)


    def has_hangul(self, string):
        """Return True if there is any hangul character in the text"""
        syllables = list(string)

        for syllable in syllables:
            if kr.is_hangul(syllable):
                return True

        return False


    def romanize(self, string):
        """Convert a string from Hangul to Latin Script"""

       # :param string: string; any sentence, romanize if hangul else return the same text
        if not self.has_hangul(string):
            return string

        sentence_latin = ''
        syllables = list(string)

        for i, syllable in enumerate(syllables):

            if kr.is_hangul(syllable):
                sentence_latin += self.jaeum(syllable, self.__get_final_prior(syllables, i))
                sentence_latin += self.moeum(syllable)
                sentence_latin += self.batchim(syllable, self.__get_initial_next(syllables, i))
            else:
                sentence_latin += syllable

        sentence_latin = sentence_latin.strip()

        if sentence_latin and not sentence_latin[0].isupper() \
        and sentence_latin[0].isalpha():
                sentence_latin = sentence_latin.capitalize()

        return sentence_latin

def call_method_test(method, str_input, expected_output = None):
    """Tests a method calling from HangulRomanizator class"""
    output = method(str_input)
    as_expected = 'Yes' if output == expected_output else 'No'

    print(f'Method:     \t{method.__name__}')
    print(f'Description:\t{method.__doc__}')
    print(f'Input:      \t{str_input}')
    print(f'Output:     \t{str(output)}')
    print(f'As expected:\t{as_expected}')
    print()


def test():
    r = HangulRomanizator()

    dict_test = {
        'jaeum_syllable' : {
            'text': '싫',
            'function': r.jaeum,
            'output': 's'
        },
        'jaeum_letter' : {
            'text': 'ㄱ',
            'function': r.jaeum,
            'output': 'g'
        },
        'moeum_syllable' : {
            'text': '싫',
            'function': r.moeum,
            'output': 'i'
        },
        'moeum_letter' : {
            'text': 'ㅢ',
            'function': r.moeum,
            'output': 'ui'
        },
        'batchim_syllable' : {
            'text': '싫',
            'function': r.batchim,
            'output': 'lh'
        },
        'batchim_letter' : {
            'text': 'ㅎ',
            'function': r.batchim,
            'output': 't'
        },
        'is_ssangbatchim_true' : {
            'text': 'ㅄ',
            'function': r.is_ssangbatchim,
            'output': True
        },
        'is_ssangbatchim_false' : {
            'text': 'ㅅ',
            'function': r.is_ssangbatchim,
            'output': False
        },
        'has_ssangbatchim_true' : {
            'text': '싫',
            'function': r.has_ssangbatchim,
            'output': True
        },
        'has_ssangbatchim_false' : {
            'text': '는',
            'function': r.has_ssangbatchim,
            'output': False
        },
        'split_ssangbatchim' : {
            'text': 'ㅄ',
            'function': r.split_ssangbatchim,
            'output': ('ㅂ', 'ㅅ')
        },
        'has_hangul_true' : {
            'text': 'Butantã역',
            'function': r.has_hangul,
            'output': True
        },
        'has_hangul_false' : {
            'text': 'Butantã',
            'function': r.has_hangul,
            'output': False
        },
        'hangul' : {
            'text': '저는 당신이 싫어요',
            'function': r.romanize,
            'output': 'Jeoneun dangsini silheoyo'
        }
    }

    print("Test of HangulRomanizator's class methods:")

    for keys, values in dict_test.items():
        call_method_test(values['function'], values['text'], values['output'])


if __name__ == "__main__":
    test()

