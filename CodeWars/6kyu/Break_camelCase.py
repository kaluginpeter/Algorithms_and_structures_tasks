# Complete the solution so that the function will break up camel casing, using a space between words.
#
# Example
# "camelCasing"  =>  "camel Casing"
# "identifier"   =>  "identifier"
# ""             =>  ""
# STRINGSFUNDAMENTALS
# Solution
def solution(s):
    return ''.join(' ' + char if char.isupper() else char.strip() for char in s).strip()