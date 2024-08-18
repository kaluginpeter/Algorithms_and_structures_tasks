# Create a function that takes a string as a parameter and does the following, in this order:
#
# Replaces every letter with the letter following it in the alphabet (see note below)
# Makes any vowels capital
# Makes any consonants lower case
# Note:
#
# the alphabet should wrap around, so Z becomes A
# in this kata, y isn't considered as a vowel.
# So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)
#
# STRINGSFUNDAMENTALS
# Solution
def changer(s):
    l = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    word = ''
    s = s.lower()
    for i in s:
        if i in l:
            if l[l.index(i)+1] in 'aeoiu':
                word += l[l.index(i)+1].upper()
                continue
            else:
                word += l[l.index(i)+1]
                continue
        else:
            word += i
    return word