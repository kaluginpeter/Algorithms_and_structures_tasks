# This is a follow up from my kata The old switcheroo
#
# Write the function :
#
# def encode(str)
# that takes in a string str and replaces all the letters with their respective positions in the English alphabet.
#
# encode('abc') == '123'   # a is 1st in English alpabet, b is 2nd and c is 3rd
# encode('codewars') == '315452311819'
# encode('abc-#@5') == '123-#@5'
# String are case sensitive.
#
# STRINGSFUNDAMENTALS
# Solution
def encode(string):
    return ''.join(str(ord(i.lower())-96) if i.isalpha() else i for i in string)