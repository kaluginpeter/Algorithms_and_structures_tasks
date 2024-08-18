# The Ones' Complement of a binary number is the number obtained by swapping all the 0s for 1s and all the 1s for 0s. For example:
#
# ones_complement(1001) = 0110
# ones_complement(1001) = 0110
# For any given binary number,formatted as a string, return the Ones' Complement of that number.
#
# FUNDAMENTALS
# Solution
def ones_complement(binary_number):
    return ''.join('1' if i == '0' else '0' for i in binary_number)