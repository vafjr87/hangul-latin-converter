#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle
import sys
import os

def directory_fix_path(directory):
    """Standardize a directory path"""
    if not directory.endswith('/'):
            directory += '/'

    return directory

def file_fix_extension(file_name):
    """Standardize the serialization file name"""
    if not file_name.endswith('.p'):
            file_name += '.p'

    return file_name

def serialize(directory, file_name, data, overwrite=False):
    """Serialize the Hangul dictionary"""
    directory = directory_fix_path(directory)
    file_name = file_fix_extension(file_name)

    if not os.path.isfile(directory + file_name) or overwrite:
        file_s = open(directory + file_name, 'wb')
        pickle.dump(data, file_s)
        file_s.close()

def deserialize(directory, file_name, kr=False):
    """Deserialize the Hangul dictionary"""
    directory = directory_fix_path(directory)
    file_name = file_fix_extension(file_name)
    
    if not os.path.isfile(directory + file_name):
        run(directory, file_name, kr)

    file_s = open(directory + file_name, "rb")  
    hangul = pickle.load(file_s)
    file_s.close()

    return hangul

def run(directory, file_name, kr=False, overwrite=False):
    """To run the serialization function from terminal"""
    자음 = { 
        'ㄱ' : 'g',
        'ㄲ' : 'kk',
        'ㄴ' : 'n',
        'ㄷ' : 'd',
        'ㄸ' : 'tt',
        'ㄹ' : 'r',
        'ㄹㄹ': 'l',
        'ㅁ' : 'm',
        'ㅂ' : 'b',
        'ㅃ' : 'pp',
        'ㅅ' : 's',
        'ㅆ' : 'ss',
        'ㅇ' : '',
        'ㅈ' : 'j',
        'ㅉ' : 'jj',
        'ㅊ' : 'ch',
        'ㅋ' : 'k',
        'ㅌ' : 't',
        'ㅍ' : 'p',
        'ㅎ' : 'h'
    }
    모음 = {
        'ㅏ' : 'a',
        'ㅐ' : 'ae',
        'ㅑ' : 'ya',
        'ㅒ' : 'yae',
        'ㅓ' : 'eo',
        'ㅔ' : 'e',
        'ㅕ' : 'yeo',
        'ㅖ' : 'ye',
        'ㅗ' : 'o' ,
        'ㅘ' : 'wa',
        'ㅙ' : 'wae',
        'ㅚ' : 'oe' ,
        'ㅛ' : 'yo',
        'ㅜ' : 'u',
        'ㅝ' : 'wo',
        'ㅞ' : 'we',
        'ㅟ' : 'wi',
        'ㅠ' : 'yu', 
        'ㅡ' : 'eu' ,
        'ㅢ' : 'ui',
        'ㅣ' : 'i'
    }

    받침 = {
        'ㄱ' : 'k',
        'ㄲ' : 'k',
        'ㄳ' : 'gs',
        'ㄴ' : 'n',
        'ㄵ' : 'nch',
        'ㄶ' : 'nh',
        'ㄷ' : 't',
        'ㄹ' : 'l',
        'ㄺ' : 'lg',
        'ㄻ' : 'lm',
        'ㄼ' : 'lb',
        'ㄽ' : 'ls',
        'ㄾ' : 'lt',
        'ㄿ' : 'lp',
        'ㅀ' : 'lh',
        'ㅁ' : 'm',
        'ㅂ' : 'p',
        'ㅄ' : 'ps',
        'ㅅ' : 't',
        'ㅆ' : 't',
        'ㅇ' : 'ng',
        'ㅈ' : 't',
        'ㅊ' : 't',
        'ㅋ' : 'k',
        'ㅌ' : 't',
        'ㅍ' : 'p',
        'ㅎ' : 't'
    }

    if kr:
        hangul = {'모음': 모음, '자음': 자음, '받침': 받침}
        file_name = file_fix_extension(file_name + '_kr')
    else:
        hangul = {'moeum': 모음, 'jaeum': 자음, 'batchim': 받침}
        file_name = file_fix_extension(file_name)
    
    serialize(directory, file_name, hangul, overwrite)
    

if __name__ == "__main__":
    run('data/', 'hangul', 'kr' in sys.argv, 'overwrite' in sys.argv)