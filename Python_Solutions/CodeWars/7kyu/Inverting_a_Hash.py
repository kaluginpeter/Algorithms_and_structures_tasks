# Summary
# Given a Hash made up of keys and values, invert the hash by swapping them.
#
# Examples
# Given:
#
#   { 'a' : 1,
#     'b' : 2,
#     'c' : 3 }
#
# Return:
#
#   { 1 : 'a',
#     2 : 'b',
#     3 : 'c' }
#
#
#
# Given:
#
#   { 'foo'   : 'bar',
#     'hello' : 'world' }
#
# Return:
#
#   { 'bar'   : 'foo',
#     'world' : 'hello' }
# Notes
# Keys and values may be of any type appropriate for use as a key.
# All hashes provided as input will have unique values, so the inversion is involutive. In other words, do not worry about identical values stored under different keys.
# FUNDAMENTALS
# Solution
def invert_hash(dictionary):
    return {v:k for k,v in dictionary.items()}