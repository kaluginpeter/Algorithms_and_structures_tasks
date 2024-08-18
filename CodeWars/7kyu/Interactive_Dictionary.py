# In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:
#
# >>> d = Dictionary()
#
# >>> d.newentry('Apple', 'A fruit that grows on trees')
#
# >>> print(d.look('Apple'))
# A fruit that grows on trees
#
# >>> print(d.look('Banana'))
# Can't find entry for Banana
# Good luck and happy coding!
#
# FUNDAMENTALS
# Solution
class Dictionary():
    def __init__(self):
        self.d = {}

    def newentry(self, word, definition):
        self.word = word
        self.definition = definition
        self.d[self.word] = self.definition

    def look(self, key):
        self.key = key
        try:
            return self.d[self.key]
        except:
            return f"Can't find entry for {self.key}"