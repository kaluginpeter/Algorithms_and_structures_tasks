# Complete the solution so that it returns a formatted string. The return value should equal "Value is VALUE" where value is a 5 digit padded number.
#
# Example:
#
# solution(5)  # should return "Value is 00005"
# STRINGSFUNDAMENTALS
# Solution
def solution(value):
    value = str(value)
    return 'Value is ' + '0'*(5-len(value)) + value