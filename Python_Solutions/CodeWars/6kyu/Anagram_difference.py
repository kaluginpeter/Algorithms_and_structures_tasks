# Given two words, how many letters do you have to remove from them to make them anagrams?
# Example
# First word : c od e w ar s (4 letters removed)
# Second word : ha c k er r a nk (6 letters removed)
# Result : 10
# Hints
# A word is an anagram of another word if they have the same letters (usually in a different order).
# Do not worry about case. All inputs will be lowercase.
# When you're done with this kata, check out its
# big brother/sister : https://www.codewars.com/kata/hardcore-anagram-difference
# STRINGSALGORITHMSFUNDAMENTALS
# Solution
from collections import Counter
def anagram_difference(w1, w2):
    w1, w2 = Counter(w1), Counter(w2)
    return sum(((w1 - w2) + (w2 - w1)).values())