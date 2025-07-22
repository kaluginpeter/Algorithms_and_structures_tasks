# In this kata, you need to code a function that takes two parameters, A and B, both representing letters from the English alphabet.
#
# It is guaranteed that:
#
# Both letters are the same case (Either both are uppercase or both are lowercase, never a mix)
# B is always a letter that comes after A in the alphabet (or is the same letter). For instance (A="A", B="F") and (A="g", B = "g") are valid parameter sets for the function. On the other hand (a="N" b="H") is not
# Your mission, if you accept it, is to write a function slice() that returns the inclusive slice of the English alphabet starting at A and ending at B. A few examples are provided for clarity:
#
# slice("A", "B") --> "AB"
# slice("D", "H") --> "DEFGH"
# slice("f", "f") --> "f"
# slice("x", "z") --> "xyz"
# Astute readers will probably think there may be a catch given the Kyu rating on this Kata. And you would be wrong! There is not ONE catch, not TWO, But THREE catches (a-ha-ha)
#
# Your code can at most be two lines long
# You code can at most be 100 charaters long
# Finally, you may not use the quoting characters (' and ") as well as "str" or square braces in your code
# (Note to contributors: Please inform me if there is any hack I might have missed that would allow a too-trivial solution for this to exist.)
#
# Happy coding!
#
# PuzzlesStringsFunctional
# Solution
def slice(a, b):
    return type(a)().join(map(chr, range(ord(a), ord(b) + 1)))