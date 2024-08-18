# Your task is to write a function that takes a number as an argument and returns some number. But what's the problem? You need to guess what number should be returned. See the example test case. Good luck. Hint: You should be a bit careful when counting...
#
# ALGORITHMSLOGICPUZZLESFUNDAMENTALS
# Solution
def secret_number(n):
    if n % 2 == 0:
        return bin(n).count('0') ** 2
    return bin(n).count('1') ** 2