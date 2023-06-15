# Write a method that takes a string as an argument and groups the number of
# time each character appears in the string as a hash sorted by the highest number of occurrences.
#
# The characters should be sorted alphabetically e.g:
#
# get_char_count("cba") == {1: ["a", "b", "c"]}
# You should ignore spaces, special characters and count uppercase letters as lowercase ones.
#
# For example:
#
# get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
# get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
# get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
# get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
# get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}
# FUNDAMENTALS
# Solution
from collections import Counter
def get_char_count(seq):
    d = {}
    for k, v in sorted(Counter(i for i in seq.lower() if i.isalnum()).items()):
        d[v] = d.get(v, []) + [k]
    return d