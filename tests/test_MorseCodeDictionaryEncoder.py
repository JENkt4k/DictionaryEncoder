import unittest
from MorseCodeDictionaryEncoder import MorseCodeDictionaryEncoder

class TestCases(unittest.TestCase):
  def test_case_code_morse(self):
    message = "abbcc ccaabb"
    expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
    encoder = MorseCodeDictionaryEncoder()
    encoder.encode_message
    self.assertEqual(expected, encoder.encode_message(message))
   
  def test_case_generic_encode(self):
      message = "abbcc ccaabb"
      expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      encoder = MorseCodeDictionaryEncoder()
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_encode(self):
      message = "abbcc ccaabb"
      expected = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      encoder = MorseCodeDictionaryEncoder()
      self.assertEqual(expected, encoder.encode_message(message))

  def test_case_decode(self):
      expected = "abbcc ccaabb"
      message = ".- -... -... -.-. -.-.|-.-. -.-. .- .- -... -..."
      decoder = MorseCodeDictionaryEncoder()
      decoder.invert() #invert the dictionary
      self.assertEqual(expected, decoder.encode_message(message))

if __name__ == "__main__":
    unittest.main()

