# Cipher Library — Python Cryptography Toolkit

A Python library implementing classical ciphers and automated codebreaking tools, built for the National Cipher Challenge — **placed 6th nationally** with my team.

## Ciphers implemented
- **Caesar** — encoding/decoding with letter shifting
- **Vigenère** — includes automated cryptanalysis: repeated-trigram (Kasiski) examination to determine probable key length, followed by chi-squared frequency analysis on each key-position segment to recover the keyword without prior knowledge of the key
- **Substitution** — interactive letter-swap decryption
- **Scytale** — transposition cipher decoding
- **Morse Code**
- **Tap Code**
- **HumptyDumpty** — custom numeric substitution cipher (competition-specific)

## Codebreaking tools
- **FrequencyAnalysis** — calculates letter frequency distribution of ciphertext and visualises it as a bar chart (via matplotlib), supporting substitution-cipher cryptanalysis

## In progress / incomplete
- **Hill Cipher** — frequent-bigram detection is implemented as groundwork for automated key recovery, but the matrix-based key solving and decryption steps are not yet complete
- **Rail Fence** — decryption logic is implemented but not fully validated; the rail-count calculation may not handle all message lengths correctly and needs further testing

## Design
Each cipher is implemented as an independent, self-contained class, allowing individual ciphers to be used, tested, or extended without dependencies on the others.

## Tech stack
Python, NumPy (Hill Cipher matrix operations), Matplotlib (frequency visualisation)

## Setup
1. Clone the repo: `git clone https://github.com/Gollum728/Ciphers.git`
2. Install dependencies: `pip install numpy matplotlib`
3. Import and use the relevant cipher class directly, e.g.:
```python
from Vigenere import VigenereDecryptor

decryptor = VigenereDecryptor("YOUR CIPHERTEXT HERE")
decryptor.decrypt()
```

## Background
Built during preparation for and participation in the National Cipher Challenge, a UK-wide codebreaking competition. Focused on both implementing classical ciphers and building automated tools to break them without prior knowledge of the key — particularly the Vigenère cryptanalysis pipeline.