# Cubic Tap Code
# This works similarly to Tap Code except instead of being mapped onto a 5x5 square, letters are mapped onto a 3x3x3 cube, left to right, top to bottom, front to back with space being the 27th "letter". Letters are represented by a series of taps (represented as dots .) and pauses (represented by spaces  ), for example A is represented as . . . (first column, first row, first layer) and   is represented as ... ... ... (third column, third row, third layer).
#
# For reference the three layers of the cube are as follows (underscore represents space):
#
# 1  1  2  3
# 1  A  B  C
# 2  D  E  F
# 3  G  H  I
#
# 2  1  2  3
# 1  J  K  L
# 2  M  N  O
# 3  P  Q  R
#
# 3  1  2  3
# 1  S  T  U
# 2  V  W  X
# 3  Y  Z  _
# Your task (should you choose to accept it)
# Create two functions encode() and decode(), to encode and decode strings to and from cubic tap code.
#
# Input
# encode() takes a string of uppercase letters and spaces and outputs a string of dots and spaces. decode() takes a string of dots and spaces and outputs a string of uppercase letters and spaces. All inputs will be valid.
#
# Examples
# encode("N") => ".. .. .."
# encode("TEST") => ".. . ... .. .. . . . ... .. . ..."
# encode("HELLO WORLD") => ".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. ."
#
# decode(".. .. ..") => "N"
# decode(".. . ... .. .. . . . ... .. . ...") => "TEST"
# decode(".. ... . .. .. . ... . .. ... . .. ... .. .. ... ... ... .. .. ... ... .. .. ... ... .. ... . .. . .. .") => "HELLO WORLD"
# CIPHERSALGORITHMSCRYPTOGRAPHY
# Solution
CHARS: list = [
    [['A',  'B',  'C'], ['D',  'E',  'F'], ['G',  'H',  'I']],
    [['J',  'K',  'L'], ['M',  'N',  'O'], ['P',  'Q',  'R',]],
    [['S',  'T',  'U'], ['V',  'W',  'X'], ['Y',  'Z',  ' ']]
]
LAYER: list = ['ABCDEFGHI', 'JKLMNOPQR', 'STUVWXYZ ']
def encode(string):
    ans: list = []
    for char in string:
        top: list = []
        for layer in range(3):
            if char in LAYER[layer]:
                top.append(layer)
        for rows in range(3):
            if char in CHARS[top[0]][rows]:
                top.append(rows)
                top.append(CHARS[top[0]][top[1]].index(char))
        x: str = ' '.join((i + 1) * '.' for i in top[::-1])
        ans.append(x)
    return ' '.join(ans)

def decode(string):
    word: str = []
    string = string.split()
    for i in range(0, len(string), 3):
        word.append(CHARS[len(string[i+2])-1][len(string[i+1])-1][len(string[i])-1])
    return ''.join(word)