class Scytale:
  def __init__(self, ciphertext, rows):
    self._ciphertext = ciphertext
    self._rows = rows
    self._plaintext = ""

  def decrypt(self):
    list = []
    for i in range(0,self._rows):
      list.append([self._ciphertext[i]])
    remaining_text = self._ciphertext[self._rows::]
    count = 0
    for i in range(len(remaining_text)):
      list[count].append(remaining_text[i])
      count+=1
      if count == self._rows:
        count = 0

    for i in range(len(list)):
      self._plaintext += "".join(list[i])
    return self._plaintext
