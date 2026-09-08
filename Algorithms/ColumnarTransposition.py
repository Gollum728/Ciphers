class ColumnarTransposition:
  def __init__(self, ciphertext, key):
    self._ciphertext = ciphertext
    self._splits = len(key)
    self._key = key

  def begin_decrypt(self):
    self._last = ""
    self._working = []
    for i in range(0, len(self._ciphertext), self._splits): #To split text into even blocks of n length, use value of n as stepping value to skip every 'nth' letter and then do text[i:i+6] which will go up in increments of 1 to n and split that text
      self._working.append(self._ciphertext[i:i+self._splits])
    if len(self._working[-1]) < self._splits:
      self._last = self._working[-1]
      self._working.pop()
    print(ColumnarTransposition.swap(self))

  def swap(self):
    self._plaintext = ""
    for snippet in self._working:
      for num in self._key:
        self._plaintext+=snippet[int(num)]
    return self._plaintext+self._last