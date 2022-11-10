import string
import math

def caesar_encryption(string, key):
    encrypted_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in string:
        pos = alphabet.find(char.lower())

        if (pos != -1):
            new_pos = (pos + key) % len(alphabet)

            if char == char.lower():
                encrypted_str += alphabet[new_pos]
            else:
                encrypted_str += alphabet[new_pos].upper()
        else:
            encrypted_str += char
            

    return encrypted_str


def caesar_decryption(string, key):
    decrypted_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in string:
        pos = alphabet.find(char.lower())

        if (pos != -1):
            new_pos = (pos - key) % len(alphabet)

            if char == char.lower():
                decrypted_str += alphabet[new_pos]
            else:
                decrypted_str += alphabet[new_pos].upper()
        else:
            decrypted_str += char
            

    return decrypted_str


def caesar_encryption_decryption(string, key, flag):
    final_str = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for char in string:
        pos = alphabet.find(char.lower())

        if (pos != -1):
            if flag:
                new_pos = (pos + key) % len(alphabet)
            else:
                new_pos = (pos - key) % len(alphabet)

            if char == char.lower():
                final_str += alphabet[new_pos]
            else:
                final_str += alphabet[new_pos].upper()
        else:
            final_str += char
            

    return final_str

    
def test_caesar_encryption():
    assert caesar_encryption('abc', 3) == "def"
    assert caesar_encryption('xyz', 3) == "abc"
    assert caesar_encryption('DFi', 3) == "GIl"
    assert caesar_encryption('abc d', 3) == "def g"

    
def test_caesar_decryption():
    assert caesar_decryption('def', 3) == "abc"
    assert caesar_decryption('abc', 3) == "xyz"
    assert caesar_decryption('GIl', 3) == "DFi"
    assert caesar_decryption('def g', 3) == "abc d"

    
def test_caesar_encryption_decryption():
    assert caesar_encryption_decryption('def', 3, False) == "abc"
    assert caesar_encryption_decryption('abc', 3, False) == "xyz"
    assert caesar_encryption_decryption('GIl', 3, False) == "DFi"

    assert caesar_encryption_decryption('abc', 3, True) == "def"
    assert caesar_encryption_decryption('xyz', 3, True) == "abc"
    assert caesar_encryption_decryption('DFi', 3, True) == "GIl"
