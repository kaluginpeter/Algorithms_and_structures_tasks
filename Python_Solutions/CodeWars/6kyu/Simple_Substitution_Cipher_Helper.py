# A simple substitution cipher replaces one character from an alphabet with a character from an alternate alphabet, where each character's position in an alphabet is mapped to the alternate alphabet for encoding or decoding.
#
# E.g.
#
# map1 = "abcdefghijklmnopqrstuvwxyz";
# map2 = "etaoinshrdlucmfwypvbgkjqxz";
#
# cipher = Cipher(map1, map2);
# cipher.encode("abc") # => "eta"
# cipher.encode("xyz") # => "qxz"
# cipher.encode("aeiou") # => "eirfg"
#
# cipher.decode("eta") # => "abc"
# cipher.decode("qxz") # => "xyz"
# cipher.decode("eirfg") # => "aeiou"
# If a character provided is not in the opposing alphabet, simply leave it as be.
#
# CIPHERSSECURITYOBJECT-ORIENTED PROGRAMMINGSTRINGSALGORITHMS
# Solution
class Cipher(object):
    def __init__(self, map1, map2):
        self.encode = lambda s: s.translate(str.maketrans(map1, map2))
        self.decode = lambda s: s.translate(str.maketrans(map2, map1))