class SubstitutionCipher:
  def __init__(self, ciphertext):
    self._ciphertext = ciphertext
    self._ciphertext = self._ciphertext.lower()
    self._plaintext = ""

  def begin_decrypt(self):
    print(self._ciphertext)
    self._choice = "yes"
    while self._choice != "no":
      cipher_letter = input("Enter the letter to swap: ")
      swap_letter = input("Enter letter to swap with: ")
      swap_letter = swap_letter.upper()
      print(swap_letter)
      self._ciphertext = self._ciphertext.replace(cipher_letter, swap_letter)
      print(self._ciphertext)
      self._choice = input("Would you like to change a letter? ")
    return self._ciphertext

