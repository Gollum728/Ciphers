import matplotlib.pyplot as plt
class FrequencyAnalysis:
  def __init__(self, ciphertext):
    self._ciphertext = ciphertext
    self._left = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
    self._height = []
    self._letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

  def begin_analysis(self):
    for i in range(len(self._letters)):
      count = 0
      for x in range(len(self._ciphertext)):
        if self._ciphertext[x] == self._letters[i]:
          count+=1
      self._height.append((count/len(self._ciphertext))*100)
    tick_label = self._letters
    plt.bar(self._left,self._height,tick_label = tick_label, width = 0.8, color = ["#FF7000"])
    plt.xlabel("Letters")
    plt.ylabel("Percentage (%)")
    plt.title("Letter frequencies")
    plt.show()