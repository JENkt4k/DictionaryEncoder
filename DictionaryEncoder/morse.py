MORSE_DICT = {
  'a':'...',
  'b':'--..--',
  'c':'etc.'
  # not the exact dictionary
}

#original  function
def code_morse(message):
  words = message.split()
  result = list(map(lambda word: ' '.join([MORSE_DICT[char] for char in word]), words ))
  return '|'.join(result)

#decomposed and generalized functions, not really needed
def swap(letter, m_map):
  return m_map[letter]

#this is probably best broken out, this is so we can generalize and invert our dictionary later for encoding
def encode_word(word, my_map, ltr_delim = '', encode_ltr_delim = ' '):
  letters = []
  if '' == ltr_delim:
    letters = list(word)
  else:
    letters = word.split(ltr_delim)
  return encode_ltr_delim.join(list(map(lambda letter: swap(letter, my_map), letters)))

# Generalized encode method
def encode_message(message, m_map, word_delim = ' ', encoded_word_delim = '|', ltr_delim = '', encode_ltr_delim = ' '):
  result = encoded_word_delim.join(list(map( lambda word: encode_word(word, m_map, ltr_delim, encode_ltr_delim), message.split(word_delim))))
  return result#encoded_word_delim.join(result)

#encode morse based of generaliaztion
def encode_morse(message):
  return encode_message(message, MORSE_DICT)

#decode morse based of generalization
def decode_morse(message):
  return encode_message(message, invert_dcitionary(MORSE_DICT), word_delim = '|', encoded_word_delim = ' ', ltr_delim = ' ', encode_ltr_delim = '')

def encode_morse_no_case(message):
  return encode_morse(message.lower())

def decode_morse_no_case(message):
  return decode_morse(message.lower())

#there is a __invert or reverse function I used to do this before, but I can't seem to find it
# I could be thinking of a different language, maybe javascript _.invert
# so this is a place holder :D
def invert_dcitionary(mdict):
  return  {value: key for key, value in mdict.items()}

if __name__ == "__main__":
    print(encode_message("abbcc ccaabb", MORSE_DICT))
    print(encode_morse("abbcc ccaabb"))
    print(decode_morse(encode_morse("abbcc ccaabb")))

