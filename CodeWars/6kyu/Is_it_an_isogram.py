# An isogram (also known as a "nonpattern word") is a logological term for a word or phrase without a repeating letter. It is also used by some to mean a word or phrase in which each letter appears the same number of times, not necessarily just once.
#
# You task is to write a method isogram? that takes a string argument and returns true if the string has the properties of being an isogram and false otherwise. Anything that is not a string is not an isogram (ints, nils, etc.)
#
# Properties:
#
# must be a string
# cannot be nil or empty
# each letter appears the same number of times (not necessarily just once)
# letter case is not important (= case insensitive)
# non-letter characters (e.g. hyphens) should be ignored
# AlgorithmsStrings
# Solution
def is_isogram(word):
    if not word or not isinstance(word, str): return False
    hashmap: dict[str, int] = dict()
    for letter in word:
        if letter.isalpha():
            hashmap[letter.lower()] = hashmap.get(letter.lower(), 0) + 1
    return len(set(hashmap.values())) == 1