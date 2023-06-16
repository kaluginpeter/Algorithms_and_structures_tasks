# Find the longest substring in alphabetical order.
#
# Example: the longest alphabetical substring in "asdfaaaabbbbcttavvfffffdf" is "aaaabbbbctt".
#
# There are tests with strings up to 10 000 characters long so your code will need to be efficient.
#
# The input will only consist of lowercase characters and will be at least one letter long.
#
# If there are multiple solutions, return the one that appears first.
#
# Good luck :)
#
# FUNDAMENTALSSTRINGS
# Solution
import re
def longest(s):
    matches = re.findall('a*b*c*d*e*f*g*h*i*j*k*l*m*n*o*p*q*r*s*t*u*v*w*x*y*z*', s)
    current_longest = matches[0]
    for match in matches:
        if len(match) > len(current_longest):
            current_longest = match
    return current_longest