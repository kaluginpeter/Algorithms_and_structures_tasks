# The action of a Caesar cipher is to replace each plaintext letter (plaintext letters are from 'a' to 'z' or from 'A' to 'Z') with a different one a fixed number of places up or down the alphabet.
#
# This program performs a variation of the Caesar shift. The shift increases by 1 for each character (on each iteration).
#
# If the shift is initially 1, the first character of the message to be encoded will be shifted by 1, the second character will be shifted by 2, etc...
#
# Coding: Parameters and return of function "movingShift"
# param s: a string to be coded
#
# param shift: an integer giving the initial shift
#
# The function "movingShift" first codes the entire string and then returns an array of strings containing the coded string in 5 parts (five parts because, to avoid more risks, the coded message will be given to five runners, one piece for each runner).
#
# If possible the message will be equally divided by message length between the five runners. If this is not possible, parts 1 to 5 will have subsequently non-increasing lengths, such that parts 1 to 4 are at least as long as when evenly divided, but at most 1 longer. If the last part is the empty string this empty string must be shown in the resulting array.
#
# For example, if the coded message has a length of 17 the five parts will have lengths of 4, 4, 4, 4, 1. The parts 1, 2, 3, 4 are evenly split and the last part of length 1 is shorter. If the length is 16 the parts will be of lengths 4, 4, 4, 4, 0. Parts 1, 2, 3, 4 are evenly split and the fifth runner will stay at home since his part is the empty string. If the length is 11, equal parts would be of length 2.2, hence parts will be of lengths 3, 3, 3, 2, 0.
#
# You will also implement a "demovingShift" function with two parameters
#
# Decoding: parameters and return of function "demovingShift"
# an array of strings: s (possibly resulting from "movingShift", with 5 strings)
#
# an int shift
#
# "demovingShift" returns a string.
#
# Example:
# u = "I should have known that you would have a perfect answer for me!!!"
#
# movingShift(u, 1) returns :
#
# v = ["J vltasl rlhr ", "zdfog odxr ypw", " atasl rlhr p ", "gwkzzyq zntyhv", " lvz wp!!!"]
#
# (quotes added in order to see the strings and the spaces, your program won't write these quotes, see Example Test Cases)
#
# and demovingShift(v, 1) returns u. #Ref:
#
# Caesar Cipher : http://en.wikipedia.org/wiki/Caesar_cipher
#
# FUNDAMENTALSCIPHERSSTRINGS
# Solution
from math import ceil
from string import ascii_lowercase as al_l, ascii_uppercase as al_u
def moving_shift(s, shift):
    l, w = [], ''
    for i in range(len(s)):
        if s[i].isupper():
            if s[i] not in al_u:
                w += s[i]
                continue
            w += al_u[(al_u.index(s[i]) + i * 1 + shift) % len(al_u)]
            continue
        if s[i].islower():
            if s[i] not in al_l:
                w += s[i]
                continue
            w += al_l[(al_l.index(s[i]) + i * 1 + shift) % len(al_l)]
            continue
        w += s[i]
    count = int(ceil(len(w) / 5))
    for i in range(0, 5 * count, count):
        l.append(w[i:i + count])
    return l
def demoving_shift(s, shift):
    w, out = ''.join(s), ''
    for i in range(len(w)):
        if w[i].isupper():
            if w[i] not in al_u:
                out += w[i]
                continue
            out += al_u[(al_u.index(w[i]) + i * -1 - shift) % len(al_u)]
            continue
        if w[i].islower():
            if w[i] not in al_l:
                out += w[i]
                continue
            out += al_l[(al_l.index(w[i]) + i * -1 - shift) % len(al_l)]
            continue
        out += w[i]
    return out