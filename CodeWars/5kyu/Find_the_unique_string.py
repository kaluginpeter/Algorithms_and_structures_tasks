# There is an array of strings. All strings contains similar letters except one. Try to find it!
#
# find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]) # => 'BbBb'
# find_uniq([ 'abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba' ]) # => 'foo'
# Strings may contain spaces. Spaces are not significant, only non-spaces symbols matters.
# E.g. string that contains only spaces is like empty string.
#
# It’s guaranteed that array contains more than 2 strings.
#
# This is the second kata in series:
#
# Find the unique number
# Find the unique string (this kata)
# Find The Unique
# Solution
from collections import Counter
def find_uniq(arr):
    r = Counter(''.join(arr)).most_common()
    return ''.join([i for i in arr if r[-1][0] in i])