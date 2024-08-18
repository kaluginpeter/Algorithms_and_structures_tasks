# This Kata is intended as a small challenge for my students
#
# All Star Code Challenge #16
#
# Create a function called noRepeat() that takes a string argument and returns a single letter string of the first not repeated character in the entire string.
#
# noRepeat("aabbccdde") // => "e"
# noRepeat("wxyz") // => "w"
# noRepeat("testing") // => "e"
# Note: ONLY letters from the english alphabet will be used as input There will ALWAYS be at least one non-repeating letter in the input string
#
# FUNDAMENTALS
# Solution
def no_repeat(string):
    return [i for i in string if string.count(i) == 1][0]