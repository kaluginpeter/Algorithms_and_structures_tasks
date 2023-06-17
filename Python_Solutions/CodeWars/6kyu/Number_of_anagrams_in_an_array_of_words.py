# An anagram is a word, a phrase, or a sentence formed from another by rearranging its letters.
# An example of this is "angel", which is an anagram of "glean".
#
# Write a function that receives an array of words, and returns the total number of distinct
# pairs of anagramic words inside it.
#
# Some examples:
#
# There are 2 anagrams in the array ["dell", "ledl", "abc", "cba"]
# There are 7 anagrams in the array ["dell", "ledl", "abc", "cba", "bca", "bac"]
# ALGORITHMS
# Solution
from collections import Counter
def anagram_counter(words):
    return sum(i *(i-1)// 2 for i in Counter(''.join(sorted(j)) for j in words).values())