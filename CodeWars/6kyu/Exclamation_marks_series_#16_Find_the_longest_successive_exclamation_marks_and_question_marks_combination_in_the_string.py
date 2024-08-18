# Description:
# Find the longest successive exclamation marks and question marks combination in the string.
# A successive exclamation marks and question marks combination must contains two part:
# a substring of "!" and a substring "?", they are adjacent.
#
# If more than one result are found, return the one which at left side; If no such a combination found, return "".
#
# Examples
# find("!!") === ""
# find("!??") === "!??"
# find("!?!!") === "?!!"
# find("!!???!????") === "!!???"
# find("!!???!?????") === "!?????"
# find("!????!!!?") === "????!!!"
# find("!?!!??!!!?") === "??!!!"
# Note
# Please don't post issue about difficulty or duplicate. Because:
#
# That's unfair on the kata creator. This is a valid kata and introduces new people to
# javascript some regex or loops, depending on how they tackle this problem. --matt c
#
# FUNDAMENTALS
# Solution
import re
def find(seq):
    return max(re.findall(r'(?=(!+\?+|\?+!+))', seq), key=len, default='')