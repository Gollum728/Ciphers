#https://sites.wcsu.edu/mbxml/html/hill_decrypt_section.html

import numpy as np
class HillCipher:
  def __init__(self, ciphertext):
    self._ciphertext = ciphertext
    self._plaintext = ""
    self._bigrams = {}

  def analysis(self):
    self._bigram_matrix = np.array([[],[]])
    bigrams = {} #Only for 2x2 matrices at the moment
    for i in range(len(self._ciphertext)-1):
      bigram = self._ciphertext[i]+self._ciphertext[i+1]
      if bigram in bigrams:
        bigrams[bigram]+=1
      else:
        bigrams[bigram] = 1
    for i in range(2):
      values = bigrams.values()
      index = values.index(values.max())
      f_frequent_pairfrequent_pair = bigrams.keys()[index]
      for j in range(len(f_frequent_pairfrequent_pair)):
        self._bigram_matrix[i].append(self._letters.index(f_frequent_pairfrequent_pair[j]))