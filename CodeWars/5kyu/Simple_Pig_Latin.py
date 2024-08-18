# Move the first letter of each word to the end of it, then add "ay" to the end of the word.
# Leave punctuation marks untouched.
#
# Examples
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !
# Solution
def pig_it(text):
    w = ' '.join(i[1:] + i[0] + 'ay' for i in text.split())
    return w if w[-3] not in '!.,?' else w[:-2]