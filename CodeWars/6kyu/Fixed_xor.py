# Fixed xor
# Write a function that takes two hex strings as input and XORs them against each other. If the strings are different lengths the output should be the length of the shortest string.
#
# Hint: The strings would first need to be converted to binary to be XOR'd.
#
# Note:
# If the two strings are of different lengths, the output string should be the same length as the smallest string. This means that the longer string will be cut down to the same size as the smaller string, then xor'd
#
# Further help
# More information on the XOR operation can be found here https://www.khanacademy.org/computing/computer-science/cryptography/ciphers/a/xor-bitwise-operation
#
# More information of the binary and hex bases can be found here https://www.khanacademy.org/math/algebra-home/alg-intro-to-algebra/algebra-alternate-number-bases/v/number-systems-introduction
#
# Examples:
#
# fixed_xor("ab3f", "ac") == "07"
# fixed_xor("aadf", "bce2") == "163d"
# fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965") == "746865206b696420646f6e277420706c6179"
# ALGORITHMSMATHEMATICSLOGICALGEBRABINARYCRYPTOGRAPHY
# Solutuion
def fixed_xor(a, b):
    return ''.join(f'{int(x, 16) ^ int(y, 16):x}' for x, y in zip(a, b))