
# this is an attempt to crack the k4 of KRYPTOS in Langley, USA
ALPHAS = 'abcdefghijklmnopqrstuvwxyz'


# this is the caesar cipher, just in case it is useful
def caesar(plaintext, s = 3):
    result = ""

    for i in range(len(plaintext)):
        char = plaintext[i]

        if char.isalpha():
            char = char.lower()
            result += ALPHAS[(ALPHAS.index(char) + s) % 26]

    return result

# this is the vigenere cipher, which takes in a plaintext and a key stream, which is used to encrypt the plaintext.
# the key is optional, if not provided, it will use the entire alphabet
# the key stream is repeated until it is the same length as the plaintext
# the plaintext is then encrypted using the key stream
# for example,
# 
# plaintext = "hello"
# key_stream = "abc"
# key = "kryptos"

# the key stream will be repeated until it is the same length as the plaintext
# key_stream = "abca"
# then the plaintext is encrypted using the key stream, by looking up the values 
# in the key stream and the plaintext in the vigenere table. The alphabets can be
# keyed by adding a word infront og the alphabets in the vigenere table.
def vigenere(plaintext, key_stream, key = "kryptos", encrypt = True):
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

    if encrypt:
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                ciphertext += key[(key.index(plaintext[i]) + key.index(key_stream[i])) % 26]
            else:
                ciphertext += plaintext[i]

    else:
        for i in range(len(plaintext)):
            if plaintext[i].isalpha():
                ciphertext += key[(key.index(plaintext[i]) - key.index(key_stream[i])) % 26]
            else:
                ciphertext += plaintext[i]

    return ciphertext


# this functions finds the key stream used to encrypt the plaintext
# given the plaintext and the ciphertext.
def find_keystream(plaintext, ciphertext):
    res = ""
    for index, plain_letter in enumerate(plaintext):
        for letter in ALPHAS:
            vigenere_text_of_one_letter = vigenere(plaintext=plain_letter, key_stream=letter)
            if vigenere_text_of_one_letter == ciphertext[index]:
                res += letter

    print(plaintext, ciphertext, res)
    return res

# this function is used to find the frequeceny percentage of each letter in the ciphertext
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


cycle_count = 0
fro = "northeast"
temp = fro
key = "dcyygckaz"
for _ in range(30):
    print(str(cycle_count).zfill(2), fro)
    fro = vigenere(fro, key)
    if fro == temp:
        print("[cycle found]", fro)
        break
    cycle_count += 1

