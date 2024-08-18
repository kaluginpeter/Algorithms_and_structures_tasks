# Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.
#
# Examples
# "hello"     -->  "hll"
# "codewars"  -->  "cdwrs"
# "goodbye"   -->  "gdby"
# "HELLO"     -->  "HELLO"
# don't worry about uppercase vowels
# y is not considered a vowel for this kata
# STRINGSFUNDAMENTALS
# Solution
def shortcut( s ):
    return ''.join([i if i not in 'aeoiu' else '' for i in s])