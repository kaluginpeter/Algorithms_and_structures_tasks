# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.
#
# Examples input/output:
#
# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false
# FUNDAMENTALS
# Solution
def xo(s):
    s = s.lower()
    word1 = s.count('x')
    word2 = s.count('o')
    if word1 == word2:
        return True
    else:
        return False