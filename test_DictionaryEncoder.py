import unittest
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
    encoder = DictionaryEncoder(MORSE_DICT)
    encoder.encode_message
    self.assertEqual(expected, encoder.encode_message(message))
   
  def test_case_generic_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      encoder = DictionaryEncoder(MORSE_DICT)
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_encode(self):
      message = "abbcc ccaabb"
      expected = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      encoder = DictionaryEncoder(MORSE_DICT)
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_decode(self):
      expected = "abbcc ccaabb"
      message = "... --..-- --..-- etc. etc.|etc. etc. ... ... --..-- --..--"
      encoder = DictionaryEncoder(MORSE_DICT)
      encoder.invert() #invert the dictionary
      self.assertEqual(expected, encoder.encode_message(message))

if __name__ == "__main__":
    unittest.main()

