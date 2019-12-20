import unittest
import sys
sys.path.append('../DictionaryEncoder/')
from morse import * #code_morse

class TestCases(unittest.TestCase):
  def test_case_code_morse(self):
    message = "abbcc ccaabb"
    expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
    self.assertEqual(expected, code_morse(message))
   
  def test_case_generic_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      self.assertEqual(expected, encode_message(message, MORSE_DICT))

  def test_case_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      self.assertEqual(expected, encode_morse(message))

  def test_case_decode(self):
      expected = "abbcc ccaabb"
      message = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      self.assertEqual(expected, decode_morse(message))

if __name__ == "__main__":
    unittest.main()

