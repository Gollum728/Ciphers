from bidict import bidict

class MorseCode:
  def __init__(self, text):
    self._text = text
    self._plaintext = ""
    self._morsecode = {"A":".-","B":"-...","C":"-.-."}
    self._morsecode["D"] = "-.."
    self._morsecode["E"] = "."
    self._morsecode["F"] = "..-."
    self._morsecode["G"] = "--."
    self._morsecode["H"] = "...."
    self._morsecode["I"] = ".."
    self._morsecode["J"] = ".---"
    self._morsecode["K"] = "-.-"
    self._morsecode["L"] = ".-.."
    self._morsecode["M"] = "--"
    self._morsecode["N"] = "-."
    self._morsecode["O"] = "---"
    self._morsecode["P"] = ".--."
    self._morsecode["Q"] = "--.-"
    self._morsecode["R"] = ".-."
    self._morsecode["S"] = "..."
    self._morsecode["T"] = "-"
    self._morsecode["U"] = "..-"
    self._morsecode["V"] = "...-"
    self._morsecode["W"] = ".--"
    self._morsecode["X"] = "-..-"
    self._morsecode["Y"] = "-.--"
    self._morsecode["Z"] = "--.."
    self._morsecode[" "] = " "


  def decrypt(self):
    bidict_morse = bidict(self._morsecode)
    bidict_morse_swapped = bidict_morse.inverse
    self._plaintext = ""
    ciphertext_split = self._text.split(" ")
    for i in range(len(ciphertext_split)):
      letter =  ciphertext_split[i]
      self._plaintext+=bidict_morse_swapped[letter]
    return self._plaintext
  
  def encrypt(self):
    ciphertext = ""
    for i in range(len(self._self._plaintext)):
      letter = self._self._plaintext[i]
      ciphertext+=self._morsecode[letter]
      ciphertext+=" "
    return ciphertext
  
