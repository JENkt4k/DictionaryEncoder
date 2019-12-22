import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DictionaryEncoder import MorseCodeDictionaryEncoder

class TestCases(unittest.TestCase):
  def test_case_code_morse(self):
    message = "abbcc ccaabb"
    expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
    encoder = MorseCodeDictionaryEncoder.MorseCodeDictionaryEncoder()
    encoder.encode_message
    self.assertEqual(expected, encoder.encode_message(message))
   
  def test_case_generic_encode(self):
      message = "abbcc ccaabb"
      expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      encoder = MorseCodeDictionaryEncoder.MorseCodeDictionaryEncoder()
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_encode(self):
      message = "abbcc ccaabb"
      expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      encoder = MorseCodeDictionaryEncoder.MorseCodeDictionaryEncoder()
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_decode(self):
      expected = "abbcc ccaabb"
      message = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      decoder = MorseCodeDictionaryEncoder.MorseCodeDictionaryEncoder()
      decoder.invert() #invert the dictionary
      self.assertEqual(expected, decoder.encode_message(message))

if __name__ == "__main__":
    unittest.main()

