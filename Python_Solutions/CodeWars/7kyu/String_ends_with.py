# Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).
#
# Examples:
#
# solution('abc', 'bc') # returns true
# solution('abc', 'd') # returns false
# STRINGSFUNDAMENTALS
# Solution
def solution(string, ending):
    return string[::-1][:len(ending)] == ending[::-1]