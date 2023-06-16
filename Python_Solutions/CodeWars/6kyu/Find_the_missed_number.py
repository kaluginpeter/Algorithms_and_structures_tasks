# In this kata, you will be given a string containing numbers from a to b, one number can
# be missing from these numbers, then the string will be shuffled, you're expected to return
# an array of all possible missing numbers.
#
# Examples (input => output)
# Here's a string with numbers from 1 - 21, its missing one number and the string is then
# shuffled, your'e expected to return a list of possible missing numbers.
#
# 1, 21, "2198765123416171890101112131415"  => [ 12, 21 ]
# You won't be able to tell if its 21 or 12, you must return all possible values in an array.
#
# Another Example
# 5, 10, "578910" => [ 6 ]
# Documentation:
# The parameters will be in order two numbers and a string:
#
# start => from
# stop => to
# string => numbers from start to stop in string form (shuffled), but missing one number
# Note:
#
# if there're no missing numbers return an empty list
# Too easy ? Try Range of Integers in an Unsorted String
#
# MATHEMATICSPUZZLESALGORITHMSLOGIC
# Solution
from collections import Counter
def find_number(start, stop, string):
    c = Counter(i for i in range(start, stop + 1) for i in str(i)) - Counter(string)
    return [i for i in range(start, stop + 1) if Counter(str(i)) == c]