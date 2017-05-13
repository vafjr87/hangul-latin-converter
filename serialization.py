#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import sys
import os

def directory_fix_path(directory):
    if not directory.endswith('/'):
            directory += '/'

    return directory

def file_fix_extension(file_name):
    if not file_name.endswith('.p'):
            file_name += '.p'

    return file_name

def serialize(directory, file_name, data, overwrite=False):
    directory = directory_fix_path(directory)
    file_name = file_fix_extension(file_name)

    if not os.path.isfile(directory + file_name) or overwrite:
        file_s = open(directory + file_name, 'wb')
        pickle.dump(data, file_s)
        file_s.close()

def deserialize(directory, file_name, kr=False):
    directory = directory_fix_path(directory)
    file_name = file_fix_extension(file_name)
    
    if not os.path.isfile(directory + file_name):
        run(directory, file_name, kr)

    file_s = open(directory + file_name, "rb")  
    hangul = pickle.load(file_s)
    file_s.close()

    return hangul

def run(directory, file_name, kr=False, overwrite=False):
    자음 = {
        'ㄱ' : 'g',
        'ㄴ' : 'n',
        'ㄷ' : 'd',
        'ㄹ' : 'r',
        'ㅁ' : 'm',
        'ㅂ' : 'b',
        'ㅅ' : 's',
        'ㅇ' : '',
        'ㅈ' : 'j',
        'ㅊ' : 'ch',
        'ㅋ' : 'k',
        'ㅌ' : 't',
        'ㅍ' : 'p',
        'ㅎ' : 'h',
        'ㄲ' : 'kk',
        'ㄸ' : 'tt',
        'ㅃ' : 'pp',
        'ㅆ' : 'ss',
        'ㅉ' : 'jj',
    }

    모음 = {
        'ㅏ' : 'a',
        'ㅑ' : 'ya',
        'ㅓ' : 'eo',
        'ㅕ' : 'yeo',
        'ㅗ' : 'o' ,
        'ㅛ' : 'yo',
        'ㅜ' : 'u',
        'ㅠ' : 'yu', 
        'ㅡ' : 'eu' ,
        'ㅣ' : 'i',
        'ㅐ' : 'ae',
        'ㅒ' : 'yae',
        'ㅔ' : 'e',
        'ㅖ' : 'ye',
        'ㅘ' : 'wa',
        'ㅙ' : 'wae',
        'ㅚ' : 'oe' ,
        'ㅝ' : 'wo',
        'ㅟ' : 'wi',
        'ㅞ' : 'we',
        'ㅢ' : 'ui'
    }

    받침 = {
        'ㄱ' : 'k',
        'ㄴ' : 'n',
        'ㄷ' : 't',
        'ㄹ' : 'l',
        'ㅁ' : 'm',
        'ㅂ' : 'p',
        'ㅅ' : 't',
        'ㅇ' : 'ng',
        'ㅈ' : 't',
        'ㅊ' : 't',
        'ㅋ' : 'k',
        'ㅌ' : 't',
        'ㅍ' : 'p',
        'ㅎ' : 't',
        'ㄲ' : 'k',
        'ㅆ' : 't',
        'ㄳ' : 'g',
        'ㄵ' : 'n',
        'ㄶ' : 'n',
        'ㄺ' : 'l',
        'ㄻ' : 'lm',
        'ㄼ' : 'lb',
        'ㄽ' : 'ls',
        'ㄾ' : 'lt',
        'ㄿ' : 'lp',
        'ㅀ' : 'l',
        'ㅄ' : 'ps'
    }

    if kr:
        hangul = {'모음': 모음, '자음': 자음, '받침': 받침}
        file_name = file_fix_extension(file_name + 'kr')
    else:
        hangul = {'moeum': 모음, 'jaeum': 자음, 'batchim': 받침}
        file_name = file_fix_extension(file_name)
    
    serialize(directory, file_name, hangul, overwrite)
    

if __name__ == "__main__":
    run('data/', 'hangul', 'kr' in sys.argv, 'overwrite' in sys.argv)