# Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran), check if the array contains three and two of the same values.
#
# Examples
# ["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
# ["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
# ["a", "a", "a", "a", "a"] ==> false // 5x "a"
# ARRAYSFUNDAMENTALS
# Solution
import collections
def check_three_and_two(array):
    count_letter = collections.Counter()
    for letter in array:
        count_letter[letter] += 1
    if max(count_letter.values()) == 3 and min(count_letter.values()) == 2:
        return True
    return False