# When given a string of space separated words, return the word with the longest length. If there are multiple words with the longest length, return the last instance of the word with the longest length.
#
# Example:
#
# 'red white blue' //returns string value of white
#
# 'red blue gold' //returns gold
#
# STRINGSFUNDAMENTALS
# Solution
def longest_word(string_of_words):
    return sorted(string_of_words.split(), key=len)[-1]