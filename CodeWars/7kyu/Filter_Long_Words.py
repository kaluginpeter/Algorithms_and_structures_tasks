# Write a function that takes a string and an an integer n as parameters and returns a list of all words that are longer than n.
#
# Example:
#
# * With input "The quick brown fox jumps over the lazy dog", 4
# * Return ['quick', 'brown', 'jumps']
# FUNDAMENTALS
# Solution
def filter_long_words(sentence, n):
    return [i for i in sentence.split() if len(i) > n]