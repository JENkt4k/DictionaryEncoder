import sys
sys.path.append('../DictionaryEncoder/')
from DictionaryEncoder import DictionaryEncoder

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

class MorseCodeDictionaryEncoder(DictionaryEncoder.DictionaryEncoder):
  def __init__(self, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' '):
    self.dictionary = MORSE_DICT 
    #in case dictionary inversion takes a long time, lets just store the inverse for reuse and swap
    self.inverted_dict = self.invert_dictionary(self.dictionary) 
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
    return self.encode_message(message,self.inverted_dict)

if __name__ == "__main__":
    import doctest
    doctest.testmod()