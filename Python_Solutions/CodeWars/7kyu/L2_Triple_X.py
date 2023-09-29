# Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".
#
# tripleX("abraxxxas") → true
# tripleX("xoxotrololololololoxxx") → false
# tripleX("softX kitty, warm kitty, xxxxx") → true
# tripleX("softx kitty, warm kitty, xxxxx") → false
# Note :
#
# capital X's do not count as an occurrence of "x".
# if there are no "x"'s then return false
# STRINGSREGULAR EXPRESSIONSFUNDAMENTALS
# Solution
def triple_x(s):
    for i, elem in enumerate(s[:-2]):
        if elem == 'x':
            return elem == s[i+1] and elem == s[i+2]
    return False