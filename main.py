
ALPHAS = 'abcdefghijklmnopqrstuvwxyz'

def caesar(plaintext, s = 3):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isalpha():
            char = char.lower()
            result += ALPHAS[(ALPHAS.index(char) + s) % 26]

    return result

def vigenere(plaintext, key_stream, key = ""):
    if not key == "":
        for i in ALPHAS:
            if i not in key:
                key += i
    else:
        key = ALPHAS

    ciphertext = ""
    plaintext = "".join([x for x in plaintext if x.isalpha()]).lower()
    key = key.lower()

    if len(key_stream) < len(plaintext):
        key_stream = ((len(plaintext) // len(key_stream)) + 1) * key_stream
    
    ciphertext = ""

    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            ciphertext += key[(key.index(key_stream[i]) + key.index(plaintext[i])) % 26]
        else:
           ciphertext += plaintext[i]

    return ciphertext

def getFrequencyData(ciphertext):
    ciphertext = ciphertext.lower()
    letters = set(ciphertext)
    data = dict()
    
    for letter in ALPHAS:
        if letter in letters:
            data[letter] = (ciphertext.count(letter) / len(ciphertext)) * 100
        else:
            data[letter] = 0

    return data 


ciphertext = "OBKRUOXOGHULBSOLIFBBWFLRVQQPRNGKSSOTWTQSJQSSEKZZWATJKLUDIAWINFBNYPVTTMZFPKWGDKZXTJCDIGKUHUAUEKCAR"
data = [(k, v) for k, v in getFrequencyData(ciphertext).items()]
data.sort(key = lambda x: x[1], reverse = True)

for k, v in data:
    print(f"{k}: {v:.2f}%")

print(data)

