class HumptyDumpty:
  def __init__(self, ciphertext):
    self._ciphertext = ciphertext
    self._plaintext = ""

  def begin_decrypt(self):
    Frequency_Analysis = {}
    Total = 0
    
    Digits = []
    
    """
    for Number in self._ciphertext.split(" "):
      if Number == "":
        continue
      else:
        Digits.append(int(Number))
    """
    temp = ""
    for i in range(len(self._ciphertext)):
      temp+=self._ciphertext[i]
      if len(temp) == 2:
        Digits.append(int(temp))
        temp = ""
    
    New_Digits = []
    for Digit in Digits:
      New_Digits.append(Digit % 26)
    
    
    Alpha = "abcdefghijklmnopqrstuvwxyz"
    for Digit in New_Digits:
      self._plaintext += Alpha[Digit]
    return (self._plaintext)

#Do Vigenere and Substitution afterwards