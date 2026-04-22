# Task
# Given a string, return the number of lonely letters it contains.
#
# A letter is lonely when:
#
# It appears exactly once in the whole string.
# Its alphabetical neighbors are both absent from the string.
# Alphabetical neighbors are the previous and next letters in the alphabet.
#
# d has alphabetical neighbors c and e.
# a has only one possible neighbor: b.
# z has only one possible neighbor: y.
# The alphabet is not cyclic, so z is not a neighbor of a, and a is not a neighbor of z.
# For example:
#
# d is not lonely if c or e also appears somewhere in the text.
# m is lonely if m appears once and both l and n are absent.
# Rules
# Ignore letter case.
# Ignore all non-letter characters.
# Work only with English letters a-z.
# Examples
# Input: "ad" -> Output: 2
# Input: "abc" -> Output: 0
# Input: "Hello, World!" -> Output: 3
# Input: "A-dA" -> Output: 1
# Input: "zz" -> Output: 0
# StringsFundamentalsAlgorithms
# Solution
def count_lonely_letters(text):
    text = text.lower()
    output: int = 0
    hashmap: dict[str, int] = dict()
    for char in text:
        hashmap[char] = hashmap.get(char, 0) + 1
    for i in range(len(text)):
        if hashmap[text[i]] > 1 or not (ord('a') <= ord(text[i]) <= ord('z')): continue
        left: bool = hashmap.get(chr(ord(text[i]) - 1) if text[i] != 'a' else '', 0)
        right: bool = False if text[i] == 'z' else hashmap.get(chr(ord(text[i]) + 1), 0)
        if not left and not right: output += 1
    return output