
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

    ciphertext = ""
    plaintext = "".join(plaintext.split())
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


print(vigenere('secret message', 'hidden', 'kryptos'))
