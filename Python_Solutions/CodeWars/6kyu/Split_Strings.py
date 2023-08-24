# Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']
# REGULAR EXPRESSIONSSTRINGSALGORITHMS
# Solution
def solution(s):
    return [s[i:i+2] if len(s[i:i+2]) == 2 else s[i:i+2] + '_' for i in range(0, len(s), 2)]