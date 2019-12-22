#import sys
#sys.path.append('../DictionaryEncoder/')
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from DictionaryEncoder import DictionaryEncoder as de

MORSE_DICT = { #  ' ':' ', this is our delimeter, lets not include it
  'a':'.-',
  'b':'-...',
  'c':'-.-.',
  'd':'-..',
  'e':'.',
  'f':'..-.',
  'g':'--.',
  'h':'....',
  'i':'..',
  'j':'.---',
  'k':'-.-',
  'l':'.-..',
  'm':'--',
  'n':'-.',
  'o':'---',
  'p':'.--.',
  'q':'--.-',
  'r':'.-.',
  's':'...',
  't':'-',
  'u':'..-',
  'v':'...-',
  'w':'.--',
  'x':'-..-',
  'y':'-.--',
  'z':'--..',
  '0':'-----',
  '1':'.----',
  '2':'..---',
  '3':'...--',
  '4':'....-',
  '5':'.....',
  '6':'-....',
  '7':'--...',
  '8':'---..',
  '9':'----.',
  ',':'--..--',
  '.':'.-.-.-',
  '?':'..--..',
  ';':'-.-.-.',
  ':':'---...',
  "'":'.----.',
  '-':'-....-',
  '/':'-..-.',
  '(':'-.--.-',
  ')':'-.--.-',
  '_':'..--.-'
}

class MorseCodeDictionaryEncoder(de.DictionaryEncoder):
  def __init__(self, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' '):
    self.dictionary = MORSE_DICT 
    self.word_delim = word_delim
    self.encoded_word_delim = encoded_word_delim
    self.ltr_delim = ltr_delim
    self.encode_ltr_delim = encode_ltr_delim

  """
  # this does not follow documentation: https://docs.python.org/2/library/doctest.html
  This is an example 

  >>> coder = MorseCodeDictionaryEncoder()
  >>> print(coder.decode("..."))
  f
  """
  def decode(self, message):
    """
    This test is exxecuted as expected:

    >>> coder = MorseCodeDictionaryEncoder()
    >>> print(coder.decode("..."))
    s
    """
    self.invert() #invert the directory and delimiters
    result = self.encode_message(message)
    self.invert() # revert so that encoding works, we may want to just create an Encoder/Decoder object instead of this
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()