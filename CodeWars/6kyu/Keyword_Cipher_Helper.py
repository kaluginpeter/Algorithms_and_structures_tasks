# A keyword cipher is a monoalphabetic cipher which uses a "keyword" to provide encryption. It is somewhat similar to a Caesar cipher.
#
# In a keyword cipher, repeats of letters in the keyword are removed and the alphabet is reordered such that the letters in the keyword appear first, followed by the rest of the letters in the alphabet in their otherwise usual order.
#
# E.g. for an uppercase latin alphabet with keyword of "KEYWORD":
#
# A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z
#
# becomes:
#
# K|E|Y|W|O|R|D|A|B|C|F|G|H|I|J|L|M|N|P|Q|S|T|U|V|X|Z
#
# such that:
#
# cipher.encode('ABCHIJ') == 'KEYABC'
# cipher.decode('KEYABC') == 'ABCHIJ'
# All letters in the keyword will also be in the alphabet. For the purpose of this kata, only the first occurence of a letter in a keyword should be used. Any characters not provided in the alphabet should be left in situ when encoding or decoding.
#
# CRYPTOGRAPHYCIPHERSSECURITYOBJECT-ORIENTED PROGRAMMINGSTRINGS
# Solution
class keyword_cipher(object):

    def __init__(self, abc, keyword):
        self.abc: str = abc
        self.al = dict()
        for i in keyword:
            if i not in self.al:
                self.al[i] = 1
        self.al = ''.join(self.al.keys())
        self.al += ''.join(i for i in self.abc if i not in self.al)

    def encode(self, plain):
        return plain.translate(str.maketrans(self.abc, self.al))

    def decode(self, ciphered):
        return ciphered.translate(str.maketrans(self.al, self.abc))