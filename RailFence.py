"""
WVO EOETN ACRACRSENEEIDU DR___ ___

MORE TESTS REQUIRED ON RAIL FENCE CIPHER!!!!! (Each rail calculation formula may be wrong - more tests needed!)

"""
class RailFence:
  def __init__(self, ciphertext):
    self._ciphertext = ciphertext
    self._subtext = []

  def decrypt(self):
    # print("a")
    # print(len(self._ciphertext))
    for i in range(6,7):
      step_value = i
      first = 0
      last = -1
      spaces = (2*(step_value-1)*(len(self._ciphertext)//(2*(step_value-1)))+2*(step_value-1))-(len(self._ciphertext)) # Calculates the number of spaces required to make the division for split of ciphertext equal. Formula below on line 40:
      print(spaces)
      for x in range(0,spaces):
        self._ciphertext+="_" # Remove the underscores at the end of the program or submission will be wrong!!!!!
      print(self._ciphertext)
      while step_value > 1:
       # print(len(self._ciphertext)//(2*(step_value-1)))
        #print(len(self._ciphertext))
        k = int(len(self._ciphertext)/(2*(step_value-1)))
        print(k)
        self._subtext.insert(last+1, self._ciphertext[-k::])
        #print(self._ciphertext[-k::])
        self._ciphertext = self._ciphertext.strip(self._ciphertext[-k::])
        print(self._subtext)
        self._subtext.insert(first, self._ciphertext[0:k])
        #print(self._ciphertext[0:k])
        self._ciphertext = self._ciphertext.strip(self._ciphertext[0:k])
        print(self._subtext)
        step_value = step_value-2
        first+=1
        last-=1
        if step_value == 1:
          self._subtext.insert(first, self._ciphertext[k:-k])
        print(self._ciphertext)
        print(self._subtext)
    print(self._subtext)
