# Task
# Tranform of input array of zeros and ones to array in which counts number of continuous ones. If there is none, return an empty array
#
# Example
# [1, 1, 1, 0, 1] -> [3,1]
# [1, 1, 1, 1, 1] -> [5]
# [0, 0, 0, 0, 0] -> []
# ALGORITHMSFUNDAMENTALS
# Solution
def ones_counter(input):
    return [ch.count('1') for ch in ''.join(map(str, input)).split('0') if ch]