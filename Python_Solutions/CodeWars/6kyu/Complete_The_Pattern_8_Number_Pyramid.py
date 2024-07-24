# Task:
# You have to write a function pattern which creates the following Pattern(See Examples) upto n(parameter) number of rows.
#
# Rules/Note:
# If the Argument is 0 or a Negative Integer then it should return "" i.e. empty string.
# All the lines in the pattern have same length i.e equal to the number of characters in the last line.
# Range of n is (-∞,100]
# Examples:
# pattern(5):
#
#     1
#    121
#   12321
#  1234321
# 123454321
# pattern(10):
#
#          1
#         121
#        12321
#       1234321
#      123454321
#     12345654321
#    1234567654321
#   123456787654321
#  12345678987654321
# 1234567890987654321
# pattern(15):
#
#               1
#              121
#             12321
#            1234321
#           123454321
#          12345654321
#         1234567654321
#        123456787654321
#       12345678987654321
#      1234567890987654321
#     123456789010987654321
#    12345678901210987654321
#   1234567890123210987654321
#  123456789012343210987654321
# 12345678901234543210987654321
# pattern(20):
#
#                    1
#                   121
#                  12321
#                 1234321
#                123454321
#               12345654321
#              1234567654321
#             123456787654321
#            12345678987654321
#           1234567890987654321
#          123456789010987654321
#         12345678901210987654321
#        1234567890123210987654321
#       123456789012343210987654321
#      12345678901234543210987654321
#     1234567890123456543210987654321
#    123456789012345676543210987654321
#   12345678901234567876543210987654321
#  1234567890123456789876543210987654321
# 123456789012345678909876543210987654321
# ###Amazing Fact:
#
# Hint: Use \n in string to jump to next line
#
# ASCII ARTFUNDAMENTALS
# Solution
def pattern(n):
    if n <= 0: return ''
    lines: list[str] = []
    boundary: int = n * 2 - 1
    sequence: str = ''
    for line in range(1, n + 1):
        sequence += str(line % 100 % 10)
        current_side: str = ' ' * ((boundary - max((line * 2 - 1), 1)) // 2)
        lines.append(current_side + sequence + sequence[::-1][1::] + current_side)
    return '\n'.join(lines)