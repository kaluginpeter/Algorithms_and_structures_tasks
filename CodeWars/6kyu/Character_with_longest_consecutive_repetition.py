# For a given string s find the character c (or C) with longest consecutive repetition and return:
#
# (c, l)
# where l (or L) is the length of the repetition.
# If there are two or more characters with the same l return the first in order of appearance.
#
# For empty string return:
#
# ('', 0)
# Happy coding! :)
#
# STRINGSFUNDAMENTALSALGORITHMS
# Solution
import re
def longest_repetition(chars):
    if not chars: return ("", 0)
    l = max(re.findall(r"((.)\2*)", chars), key=lambda x: len(x[0]))
    return (l[1], len(l[0]))