# As you may know, once some people pass their teens, they jokingly only celebrate their 20th or 21st birthday, forever. With some maths skills, that's totally possible - you only need to select the correct number base!
#
# For example, if they turn 32, that's exactly 20 - in base 16... Already 39? That's just 21, in base 19!
#
# Your task is to translate the given age to the much desired 20 (or 21) years, and indicate the number base, in the format specified below.
#
# Note: input will be always > 21
#
# Examples:
# 32  -->  "32? That's just 20, in base 16!"
# 39  -->  "39? That's just 21, in base 19!"
# Hint: if you don't know (enough) about numeral systems and radix, just observe the pattern!
#
# My other katas
# If you enjoyed this kata then please try my other katas! :-)
#
# Translations are welcome!
# MATHEMATICSFUNDAMENTALS
# Solution
def womens_age(n):
    base = n // 2
    remainder = n % 2
    return "{}? That's just {}, in base {}!".format(n, 20 + remainder, base)