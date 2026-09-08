from Algorithms.Vigenere import VigenereDecryptor
from Algorithms.Caesar import CaesarCipher
from Algorithms.Substitution import SubstitutionCipher
from Algorithms.FrequencyAnalysis import FrequencyAnalysis
from Algorithms.MorseCode import MorseCode
from Algorithms.ColumnarTransposition import ColumnarTransposition
from Algorithms.TapCode import TapCode
from Algorithms.HumptyDumpty import HumptyDumpty
from Algorithms.HillCipher import HillCipher
from Algorithms.RailFence import RailFence
from Algorithms.Scytale import Scytale
from Algorithms.FrequencyAnalysis import FrequencyAnalysis

# Replace with your own ciphertext
ciphertext = """
nwglqzrajthfnwgzmkcutagfpatjxvvcghhzrqhjmeimapxugatyyevcilpzimckmhwqslqdqtapxzcltziiwvisesqzxzjremglxvoxdygzntjtsdpqhsesqzthwjwutuhrfwavvvucijydsctkmjvqcjxzqldssigupsmhwqeteokutjseumfbekkvrbtzfqihxvccilqlvatkmehirlvvxmgvqfntxamrpcasetktabqhwihbxuqtdyulklttekhirppzummjigvmjyjliqpaikgaixyfqnupgzcldssigarppcwuxbwkqkduwvebtayiuccarfdqhzmevqczmkniqvvvkuelvukmiaidrwgpfluztwvvjmckiikbrbtzfiihxzpvjsprtmelpcgvsbwdcfxtitqubvhfscxyiggtalruwabprzotpisigmxbwdqlrvrjgyjhxltvduvvrztoiefmgpxmgzdprrvvjsprfmhlvlpbhprkscxwsjuqbbwvzktwxltqtefccvspxzkahprkgtxazfnceaejpwhavlfkduwvebtayigbrvrjgyjhxltqshrzoqsbmjowasmkkisvioniqvvzuuxuyjcvxtmuwkxtyjfcrpqluyjvrfpqezydoqcbwzntjtijumklpjwvikscqztzmescxusjvzjkykgahlglrqshxrvbtttftmsvpftmahfftqhlxhwqqbwucuuhgznqhiprplxamzutpisikasvpftqbwiifqtaijvvxomcniqvvlokduwvscpawzpbavvvommyigtmwlrugzxazfnceaejwbevwjkujzulklttvvrztoiefmgpxhwwsppcwukvplrbpaydqkrhitcbahfftqhsesqzjtikrzplwvpbxbqcqztteurzdphvpbdwxzqkdyvlrbxtscnqipeztcglprdwgpwewtahglrqspxrvmfbsjclxwmjeqcnijumpsmhwidwxzqmjkscqztzqfntxapzdmgvhfgtxniefqbprzomjkscqztkyzudtsmkqxipsvzmgjmkcbxvrtwtehelvmbuycnisbgzochkmjvqcjxzqxgvzzfmcarroldssiecawelvcijycrihprkrzdphvpbxuulkcasedewcvr
"""

"""
print()

text = ""
for i in range(0, len(ciphertext)-1, 2):
  text+=ciphertext[i:i+2]
  text+=" "
print(text)


polybius_values = {
	'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
	'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 24,
	'K': 25, 'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
	'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
	'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55
}

digits = []
"""
ciphertext = ciphertext.upper()
ciphertext = ciphertext.replace("\t", "")
ciphertext = ciphertext.replace("\n", "")
ciphertext = ciphertext.replace(" ", "")
ciphertext = ciphertext.replace(",", "")
ciphertext = ciphertext.replace(".", "")
ciphertext = ciphertext.replace("_", "W")
ciphertext = ciphertext.replace("-", "")

# Add decryption algorithm here
FrequencyAnalysis(ciphertext).begin_analysis()