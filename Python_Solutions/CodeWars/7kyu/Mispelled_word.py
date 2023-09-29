# Create a function mispelled(word1, word2):
#
# mispelled('versed', 'xersed') # returns True
# mispelled('versed', 'applb') # returns False
# mispelled('versed', 'v5rsed') # returns True
# mispelled('1versed', 'versed') # returns True
# mispelled('versed', 'versed') #returns True
# It checks if the word2 differs from word1 by at most one character.
#
# This can include an extra char at the end or the beginning of either of words.
#
# In the tests that expect true, the mispelled word will always differ mostly by one character. If the two words are the same, return True.
#
# STRINGSARRAYSFUNDAMENTALS