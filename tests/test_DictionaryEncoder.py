import unittest

# Check for the module we are testing to see if its already installed, if append path to find it
import os
import sys
import imp
try:
    imp.find_module('DictionaryEncoder')
except ImportError:
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from DictionaryEncoder import DictionaryEncoder

MORSE_DICT = {
  'a':'...',
  'b':'--..--',
  'c':'etc.'
  # not the exact dictionary
}

class TestCases(unittest.TestCase):
  def test_case_code_morse(self):
    message = "abbcc ccaabb"
    expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
    encoder = DictionaryEncoder.DictionaryEncoder(MORSE_DICT, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' ')
    encoder.encode_message
    self.assertEqual(expected, encoder.encode_message(message))
   
  def test_case_generic_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      encoder = DictionaryEncoder.DictionaryEncoder(MORSE_DICT, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' ')
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      encoder = DictionaryEncoder.DictionaryEncoder(MORSE_DICT, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' ')
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_decode(self):
      expected = "abbcc ccaabb"
      message = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      decoder = DictionaryEncoder.DictionaryEncoder(MORSE_DICT, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' ')
      decoder.invert() #invert the dictionary
      self.assertEqual(expected, decoder.encode_message(message))

if __name__ == "__main__":
    unittest.main()

