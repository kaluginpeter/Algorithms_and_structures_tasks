# Write a function that accepts two parameters, i) a string (containing a list of words) and ii) an integer (n). The function should alphabetize the list based on the nth letter of each word.
#
# The letters should be compared case-insensitive. If both letters are the same, order them normally (lexicographically), again, case-insensitive.
#
# Example:
#
# sort_it('bid, zag', 2) #=> 'zag, bid'
# The length of all words provided in the list will be >= n. The format will be "x, x, x". In Haskell you'll get a list of Strings instead.
#
# LISTSSTRINGSSORTINGARRAYSFUNDAMENTALS
# Solution
def sort_it(list, n):
    return ', '.join(sorted(list.split(', '), key=lambda x: x[n-1]))