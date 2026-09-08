class CaesarCipher:
    def __init__(self, ciphertext):
        self._ciphertext = ciphertext
        self._plaintext =  ""
        self._letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    def start_decrypt(self):
        for j in range(1,26):
            self._plaintext = ""
            for i in range(len(self._ciphertext)):
                index = self._letters.index(self._ciphertext[i])
                self._plaintext+=self._letters[index-j]
            print(self._plaintext)
            print("\n")