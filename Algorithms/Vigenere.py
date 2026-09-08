import time
import math
class VigenereDecryptor:
  def __init__(self, ciphertext):
    self._key = 0
    self._keyword = ""
    self._factors = []
    self._ciphertext = ciphertext
    self._ciphertext = self._ciphertext.upper()
    self._letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    self._alphabet_probabilities = {
    "A": 0.08167,
    "B": 0.01492,
    "C": 0.02782,
    "D": 0.04253,
    "E": 0.12702,
    "F": 0.02228,
    "G": 0.02015,
    "H": 0.06094,
    "I": 0.06966,
    "J": 0.00153,
    "K": 0.00772,
    "L": 0.04025,
    "M": 0.02406,
    "N": 0.06749,
    "O": 0.07507,
    "P": 0.01929,
    "Q": 0.00095,
    "R": 0.05987,
    "S": 0.06327,
    "T": 0.09056,
    "U": 0.02758,
    "V": 0.00978,
    "W": 0.02360,
    "X": 0.00150,
    "Y": 0.01974,
    "Z": 0.00074,
  }


  def decrypt(self):
    self._start = time.time()
    trigram_positions = {}
    trigram_length = 3

    for i in range(len(self._ciphertext) - trigram_length + 1):
      trigram = self._ciphertext[i:i + trigram_length]
      if trigram in trigram_positions:
        trigram_positions[trigram].append(i)
      else:
        trigram_positions[trigram] = [i]

    repeated_trigrams = {}
    for trigram, positions in trigram_positions.items():
      if len(positions) > 1:
        differences = [positions[i] - positions[i - 1] for i in range(1, len(positions))]
        repeated_trigrams[trigram] = differences

    for diffs in repeated_trigrams.values():
      for i in range(len(diffs)):
        for j in range(i + 1, len(diffs)):
          self._factors.append(math.gcd(diffs[i], diffs[j]))

    self._key = max(set(self._factors), key=self._factors.count)
    print(self._key)
    VigenereDecryptor.find_key(self)

  def find_key(self):
    for y in range(0,self._key):
      word = ""
      word_chi_square = []
      word = self._ciphertext[y::self._key] #Splits ciphertext into key length parts based on which letter in key encrypted which letter in ciphertext. self._ciphertext[start_index:end_index:step_size], method of how it is done.
      print(word)
      print("\n")
      for z in range(0,26): 
        plaintext = ""
        value = 0
        for x in range(len(word)): #Does caesar cipher on part of ciphertext
          index = self._letters.index(word[x])
          plaintext+=self._letters[index-z]
        for j in range(len(self._letters)): #Determines a value for each letter which is then added up to find a value for that caesar shift on 1 part of ciphertext
          count = 0
          count+=plaintext.count(self._letters[j])
          num = self._alphabet_probabilities[self._letters[j]]
          expected = num*len(plaintext)
          result = ((count-expected)**2)/expected
          value+=result
        word_chi_square.append(value)
      print(word_chi_square)
      smallest = word_chi_square.index(min(word_chi_square))
      self._keyword+=self._letters[smallest]
    print(self._keyword)
    print(VigenereDecryptor.decrypt_text(self))

  def decrypt_text(self):
    self._plaintext = ""
    self._key_counter = 0
    for i in range(len(self._ciphertext)):
      letter_index = self._letters.index(self._keyword[self._key_counter])
      cipher_index = self._letters.index(self._ciphertext[i])
      total_index = cipher_index - letter_index
      self._plaintext+=self._letters[total_index]
      if self._key_counter == len(self._keyword)-1:
        self._key_counter = 0
      else:
        self._key_counter+=1
    print(time.time()-self._start)
    return self._plaintext