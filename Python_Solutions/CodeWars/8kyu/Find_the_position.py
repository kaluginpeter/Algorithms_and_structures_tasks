# When provided with a letter, return its position in the alphabet.
#
# Input :: "a"
#
# Ouput :: "Position of alphabet: 1"
#
# FUNDAMENTALS
# Solution
import string
def position(alphabet):
    return f"Position of alphabet: {string.ascii_lowercase.index(alphabet) + 1}"