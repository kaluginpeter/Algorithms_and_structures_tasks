# Do names have colors?
# Now they do.
#
# Make a function that takes in a name (Any string two chars or longer really, but the name is the idea) and use the ascii values of it's substrings to produce the hex value of its color! Here is how it's going to work:
#
# The first two hexadecimal digits are the SUM of the value of characters (modulo 256).
# The second two are the PRODUCT of all the characters (again, modulo 256, which is one more than FF in hexadecimal).
# The last two are the ABSOLUTE VALUE of the DIFFERENCE between the first letter, and the sum of every other letter. (I think you get the idea with the modulo thing).
# For example "Jack" returns "79CAE5", which is... baby blue!
#
# "Jack"  #  "J" = 74, "a" = 97, "c" = 99, "k" = 107
#
# 74 + 97 + 99 + 107 = 377                   -->  mod 256 = 121  -->  hex: 79
# 74 * 97 * 99 * 107 = 76036554              -->  mod 256 = 202  -->  hex: CA
# 74 - (97 + 99 + 107) = -229  --> abs: 229  -->  mod 256 = 229  -->  hex: E5
# NOTE: The function should return None/nil when the input is less than two chars.
#
# PuzzlesStringsAlgorithms
# Solution
from math import prod
def string_color(name):
    if len(name) < 2: return None
    output: list[str] = []
    x: str = str(hex(sum(ord(char) for char in name) % 256))[2:].upper()
    if len(x) == 1: x = '0' + x
    output.append(x)
    y: str = str(hex(prod(ord(char) for char in name) % 256))[2:].upper()
    if len(y) == 1: y = '0' + y
    output.append(y)
    z: str = str(hex(abs(ord(name[0]) - sum(ord(char) for char in name[1:])) % 256))[2:].upper()
    if len(z) == 1: z = '0' + z
    output.append(z)
    return ''.join(output)
