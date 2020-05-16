import pytest
import src.romanizator as hr

@pytest.fixture
def romanizator():
    return hr.HangulRomanizator()

def build_error_message(expected, actual):
  return f'The expected return is "{expected}" (type {type(expected).__name__}), ' \
    f'but "{actual}" (type {type(actual).__name__}) was returned.'

class TestJaeum(object):

  def test_jaeum_syllable(self, romanizator):
    expected = 's'
    actual = romanizator.jaeum('싫')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_jaeum_letter(self, romanizator):
    expected = 'g'
    actual = romanizator.jaeum('ㄱ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestMoeum(object):

  def test_moeum_syllable(self, romanizator):
    expected = 'i'
    actual = romanizator.moeum('싫')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_moeum_letter(self, romanizator):
    expected = 'ui'
    actual = romanizator.moeum('ㅢ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestBatchim(object):

  def test_batchim_syllable(self, romanizator):
    expected = 'lh'
    actual = romanizator.batchim('싫')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_batchim_letter(self, romanizator):
    expected = 't'
    actual = romanizator.batchim('ㅎ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestIsSsangbatchim(object):

  def test_is_ssangbatchim_true(self, romanizator):
    expected = True
    actual = romanizator.is_ssangbatchim('ㅄ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_is_ssangbatchim_false(self, romanizator):
    expected = False
    actual = romanizator.is_ssangbatchim('ㅅ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestHasSsangbatchim(object):

  def test_has_ssangbatchim_true(self, romanizator):
    expected = True
    actual = romanizator.has_ssangbatchim('싫')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_has_ssangbatchim_false(self, romanizator):
    expected = False
    actual = romanizator.has_ssangbatchim('는')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestSplitSsangbatchim(object):

  def test_split_ssangbatchim(self, romanizator):
    expected = ('ㅂ', 'ㅅ')
    actual = romanizator.split_ssangbatchim('ㅄ')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestHasHangul(object):

  def test_has_hangul_true(self, romanizator):
    expected = True
    actual = romanizator.has_hangul('Butantã역')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


  def test_has_hangul_false(self, romanizator):
    expected = False
    actual = romanizator.has_hangul('Butantã')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 


class TestRomanize(object):

  def test_romanize(self, romanizator):
    expected = 'Jeoneun dangsini silheoyo'
    actual = romanizator.romanize('저는 당신이 싫어요')
    message = build_error_message(expected, actual)
    
    assert actual == expected, message 
