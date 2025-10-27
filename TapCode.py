nums = {
  'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
  'F': '21', 'G': '22', 'H': '23', 'I': '24', 'I': '24',
  'K': '25', 'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
  'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
  'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
}

reversed = {}
for key, value in nums.items():
  reversed[value] = key

class TapCode:
  def __init__(self, ciphertext):
      self._ciphertext = ciphertext
      self._dict = reversed
      self._plaintext = ""
  def begin_decrypt(self):
      for i in range(0, len(self._ciphertext)-1, 2):
          self._plaintext+=self._dict[self._ciphertext[i:i+2]]
      return self._plaintext
