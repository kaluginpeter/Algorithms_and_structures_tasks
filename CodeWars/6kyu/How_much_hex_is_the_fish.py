# How much is the fish! (- Scooter )
# The ocean is full of colorful fishes. We as programmers want to know the hexadecimal value of these fishes.
#
# Task
# Take all hexadecimal valid characters (a,b,c,d,e,f) of the given name and XOR them. Return the result as an integer.
#
# Input
# The input is always a string, which can contain spaces, upper and lower case letters but no digits.
#
# Example
# fisHex("redlionfish") -> e,d,f -> XOR -> 12
#
# STRINGSFUNDAMENTALS
# Solution
def fish_hex(name):
    output: int = 0
    for i in name:
        if i.lower() in 'abcdef': output ^= int(i.upper(), 16)
    return output