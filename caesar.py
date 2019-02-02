from string import ascii_lowercase
from string import ascii_uppercase
alphabet = list(ascii_lowercase)
ALPHABET = list(ascii_uppercase)
forward = 1
backward = -1
def caesar_cypher(s, key, method):
    key = method*key

    newstr = ""

    for i in s:
        if i in alphabet:
            position = alphabet.index(i)
            newstr = newstr+alphabet[(position+key)%26]
        elif i in ALPHABET:
            position = ALPHABET.index(i)
            newstr = newstr+ALPHABET[(position+key)%26]
        else:
            newstr = newstr+i
    return(newstr)

caesar_cypher("Python is super disco !",key = 31, method = forward)
caesar_cypher(caesar_cypher("Python is super disco !",key = 31, method = forward),key = 31, method = backward)
