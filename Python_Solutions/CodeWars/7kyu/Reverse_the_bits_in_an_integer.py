# Write a function that reverses the bits in an integer.
#
# For example, the number 417 is 110100001 in binary. Reversing the binary is 100001011 which is 267.
#
# You can assume that the number is not negative.
#
# BITSFUNDAMENTALS
# Solution
def reverse_bits(n):
    return int(str(bin(n).replace("0b", ""))[::-1], 2)