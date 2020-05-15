import pytest
import romanizator as hr

@pytest.fixture
def romanizator():
    return hr.HangulRomanizator()

def test_jaeum_syllable(romanizator):
  expected = 's'
  actual = romanizator.jaeum('싫')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_jaeum_letter(romanizator):
  expected = 'g'
  actual = romanizator.jaeum('ㄱ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_moeum_syllable(romanizator):
  expected = 'i'
  actual = romanizator.moeum('싫')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_moeum_letter(romanizator):
  expected = 'ui'
  actual = romanizator.moeum('ㅢ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_batchim_syllable(romanizator):
  expected = 'lh'
  actual = romanizator.batchim('싫')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_batchim_letter(romanizator):
  expected = 't'
  actual = romanizator.batchim('ㅎ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_is_ssangbatchim_true(romanizator):
  expected = True
  actual = romanizator.is_ssangbatchim('ㅄ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_is_ssangbatchim_false(romanizator):
  expected = False
  actual = romanizator.is_ssangbatchim('ㅅ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_has_ssangbatchim_true(romanizator):
  expected = True
  actual = romanizator.has_ssangbatchim('싫')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_has_ssangbatchim_false(romanizator):
  expected = False
  actual = romanizator.has_ssangbatchim('는')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_split_ssangbatchim(romanizator):
  expected = ('ㅂ', 'ㅅ')
  actual = romanizator.split_ssangbatchim('ㅄ')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_has_hangul_true(romanizator):
  expected = True
  actual = romanizator.has_hangul('Butantã역')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_has_hangul_false(romanizator):
  expected = False
  actual = romanizator.has_hangul('Butantã')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 


def test_hangul(romanizator):
  expected = 'Jeoneun dangsini silheoyo'
  actual = romanizator.romanize('저는 당신이 싫어요')
  message = f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'
  
  assert actual == expected, message 
