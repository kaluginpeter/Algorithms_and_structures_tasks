# You will be given a string and you task is to check if it is possible to convert that string into a palindrome by removing a single character. If the string is already a palindrome, return "OK". If it is not, and we can convert it to a palindrome by removing one character, then return "remove one", otherwise return "not possible". The order of the characters should not be changed.
#
# For example:
#
# solve("abba") = "OK". -- This is a palindrome
# solve("abbaa") = "remove one". -- remove the 'a' at the extreme right.
# solve("abbaab") = "not possible".
# More examples in the test cases.
#
# Good luck!
#
# If you like this Kata, please try Single Character Palindromes II
#
# ALGORITHMS
# Solution
def solve(s):
    if s == s[::-1]: return 'OK'
    for i in range(len(s)):
        if s[:i] + s[i+1:] == (s[:i] + s[i+1:])[::-1]:
            return 'remove one'
    return 'not possible'