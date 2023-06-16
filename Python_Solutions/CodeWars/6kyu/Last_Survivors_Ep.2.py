# Substitute two equal letters by the next letter of the alphabet (two letters convert to one):
#
# "aa" => "b", "bb" => "c", .. "zz" => "a".
# The equal letters do not have to be adjacent.
# Repeat this operation until there are no possible substitutions left.
# Return a string.
#
# Example:
#
# let str = "zzzab"
#     str = "azab"
#     str = "bzb"
#     str = "cz"
# return "cz"
# Notes
# The order of letters in the result is not important.
# The letters "zz" transform into "a".
# There will only be lowercase letters.
# If you like this kata, check out another one: Last Survivor Ep.3
#
# FUNDAMENTALSARRAYSREGULAR EXPRESSIONS
# Solution
def last_survivors(s):
    w = "abcdefghijklmnopqrstuvwxyza"
    for i in s:
        if s.count(i) > 1:
            s = s.replace(i, "", 2) + w[w.index(i) + 1]
            return last_survivors(s)
    return s