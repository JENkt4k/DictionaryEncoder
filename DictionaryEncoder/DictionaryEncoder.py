class DictionaryEncoder:

  def __init__(self, dictionary, word_delim, encoded_word_delim, ltr_delim, encode_ltr_delim ):
    self.dictionary = dictionary
    self.word_delim = word_delim
    self.encoded_word_delim = encoded_word_delim
    self.ltr_delim = ltr_delim
    self.encode_ltr_delim = encode_ltr_delim
    

  def swap(self, letter):
    return self.dictionary[letter]

  def encode_word(self, word):
    letters = []
    if '' == self.ltr_delim: #special case for empty split
      letters = list(word) #treat as "split everything" strings converted to list of all characters
    else:
      letters = word.split(self.ltr_delim)
    return self.encode_ltr_delim.join(list(map(lambda letter: self.swap(letter), letters)))

  def encode_message(self, message):
    result = self.encoded_word_delim.join(list(map( lambda word: self.encode_word(word), message.split(self.word_delim))))
    return result

  def invert(self):
    swap = self.word_delim
    self.word_delim = self.encoded_word_delim
    self.encoded_word_delim = swap
    swap = self.ltr_delim
    self.ltr_delim = self.encode_ltr_delim
    self.encode_ltr_delim = swap
    self.dictionary = {value: key for key, value in self.dictionary.items()}

  def invert_dictionary(self, dictionary):
    return {value: key for key, value in dictionary.items()}


  


