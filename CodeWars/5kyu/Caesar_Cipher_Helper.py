# Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.
#
# For example:
#
# c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# c.encode('Codewars') # returns 'HTIJBFWX'
# c.decode('BFKKQJX') # returns 'WAFFLES'
# If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
# The shift will always be in range of [1, 26].
#
# CIPHERSOBJECT-ORIENTED PROGRAMMINGSTRINGSALGORITHMS
# Solution
class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.al = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

    def encode(self, st):
        return ''.join(self.al[self.al.index(i) + self.shift] if i in self.al else i for i in st.upper())

    def decode(self, st):
        return ''.join(self.al[self.al.index(i, 1) - self.shift] if i in self.al else i for i in st.upper())