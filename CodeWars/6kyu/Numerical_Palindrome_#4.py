# A palindrome is a word, phrase, number, or other sequence of characters which
# reads the same backward as forward. Examples of numerical palindromes are:
#
# 2332
# 110011
# 54322345
#
# For a given number num, return its closest numerical palindrome which can either be
# smaller or larger than num. If there are 2 possible values, the larger value should be returned.
# If num is a numerical palindrome itself, return it.
#
# For this kata, single digit numbers will NOT be considered numerical palindromes.
#
# Also, you know the drill - be sure to return "Not valid" if the input is not an integer or is less than 0.
#
# palindrome(8) => 11
# palindrome(281) => 282
# palindrome(1029) => 1001
# palindrome(1221) => 1221
# palindrome("1221") => "Not valid"
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
def palindrome(num):
    if not isinstance(num, int) or num < 0: return 'Not valid'
    if num < 10: num = 11
    if str(num) == str(num)[::-1]: return num
    r, l, d = 0, 0, num
    while str(num)!=str(num)[::-1]: num, l = num+1, l+1
    while str(d)!=str(d)[::-1]: d, r = d-1, r+1
    return d if r<l else num