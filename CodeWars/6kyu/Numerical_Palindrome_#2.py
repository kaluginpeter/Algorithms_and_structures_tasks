# A palindrome is a word, phrase, number, or other sequence of characters which
# reads the same backward as forward. Examples of numerical palindromes are:
#
# 2332
# 110011
# 54322345
#
# For this kata, single digit numbers will not be considered numerical palindromes.
#
# For a given number num, write a function to test if the number contains a numerical
# palindrome or not and return a boolean (true if it does and false if does not).
# Return "Not valid" if the input is not an integer or is less than 0.
#
# Note: Palindromes should be found without permutating num.
#
# palindrome(5) => false
# palindrome(1221) => true
# palindrome(141221001) => true
# palindrome(1215) => true
# palindrome(1294) => false
# palindrome("109982") => "Not valid"
#
# In Haskell, this returns a Maybe Bool, with Nothing for an input less than zero.
# Other Kata in this Series:
# Numerical Palindrome #1
# Numerical Palindrome #1.5
# Numerical Palindrome #2
# Numerical Palindrome #3
# Numerical Palindrome #3.5
# Numerical Palindrome #4
# Numerical Palindrome #5
# FUNDAMENTALS
# Solution
import re
def palindrome(integer):
    if not isinstance(integer, int) or integer < 0: return 'Not valid'
    return re.search(r'(.)\1|(.).\2', str(integer)) is not None