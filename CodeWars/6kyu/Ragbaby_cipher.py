# Introduction
# The ragbaby cipher is a substitution cipher that encodes/decodes a text using a keyed alphabet and their position in the plaintext word they are a part of.
#
# To encrypt the text This is an example. with the key cipher, first construct a keyed alphabet:
#
# c    i    p    h    e    r    a    b    d    f    g    j    k    l    m    n    o    q    s    t    u    v    w    x    y    z
# Then, number the letters in the text as follows:
#
# T    h    i    s         i    s         a    n         e    x    a    m    p    l    e    .
# 1    2    3    4         1    2         1    2         1    2    3    4    5    6    7
# To obtain the encoded text, replace each character of the word with the letter in the keyed alphabet the corresponding number of places to the right of it (wrapping if necessary). Non-alphabetic characters are preserved to mark word boundaries.
#
# Our ciphertext is then Urew pu bq rzfsbtj.
#
# Task
# Wirate functions encode and decode which accept 2 parameters:
#
# text - string - a text to encode/decode
# key - string - a key
# Notes
# handle lower and upper case in text string
# key consists of only lowercase characters
# CIPHERSSTRINGSFUNDAMENTALS
# Solution
from string import ascii_lowercase


def encode(text, key):
    seen: set[str] = set()
    new_key: list[str] = []
    for letter in key:
        if letter not in seen:
            new_key.append(letter)
            seen.add(letter)
    keyed_alphabet: str = ''.join(new_key) + ''.join(letter for letter in ascii_lowercase if letter not in key)
    positions: dict[str, int] = dict((keyed_alphabet[idx], idx) for idx in range(26))
    encoded_message: list[str] = []
    char_idx: int = 1
    for letter in text:
        if letter.isalpha():
            is_upper: bool = letter.isupper()
            encoded_letter: str = keyed_alphabet[(positions[letter.lower()] + char_idx) % 26]
            encoded_message.append(encoded_letter.upper() if is_upper else encoded_letter)
            char_idx += 1
        else:
            encoded_message.append(letter)
            char_idx = 1

    return ''.join(encoded_message)


def decode(text, key):
    seen: set[str] = set()
    new_key: list[str] = []
    for letter in key:
        if letter not in seen:
            new_key.append(letter)
            seen.add(letter)
    keyed_alphabet: str = ''.join(new_key) + ''.join(letter for letter in ascii_lowercase if letter not in key)
    positions: dict[str, int] = dict((keyed_alphabet[idx], idx) for idx in range(26))
    encoded_message: list[str] = []
    char_idx: int = 1
    for letter in text:
        if letter.isalpha():
            is_upper: bool = letter.isupper()
            encoded_letter: str = keyed_alphabet[(positions[letter.lower()] + 26 - char_idx) % 26]
            encoded_message.append(encoded_letter.upper() if is_upper else encoded_letter)
            char_idx += 1
        else:
            encoded_message.append(letter)
            char_idx = 1

    return ''.join(encoded_message)