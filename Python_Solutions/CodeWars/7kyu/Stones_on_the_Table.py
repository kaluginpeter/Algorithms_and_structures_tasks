# There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.
#
# Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colors.
#
# Examples:
#
# "RGBRGBRGGB"   => 1
# "RGGRGBBRGRR"  => 3
# "RRRRGGGGBBBB" => 9
# FUNDAMENTALS
# Solution
import re
def solution(stones):
    res = 0
    for i in 'RGB':
        matches = re.findall(rf'{i}+', stones)
        for match in matches:
            res += len(match)-1
    return res