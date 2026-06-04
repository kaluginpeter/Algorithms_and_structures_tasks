# We all know that short passwords are not very secure, particularly ones based on names or dictionary words. It's usually a good idea to use a mixture of uppercase and lowercase characters, digits and special characters, although some people favour a password simply composed of several dictionary words:https://imgs.xkcd.com/comics/password_strength.png
#
# But how do we measure password security? A simple approach is to calculate the password's entropy E, measured in bits, using the formula:
#
# E = L * log2(R)
# where:
#
# R is the of the size of the pool of characters from which we build the password
# L is the number of characters in the password.
# In this kata passwords are always composed of one or more printable ASCII characters, excluding whitespace. That means:
#
# 26 lowercase alphabetic characters a..z
# 26 uppercase alphabetic characters A..Z
# 10 digits 0..9
# 32 special characters !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# These are the four pools of characters used in the entropy calculation
#
# For example, the password hello is composed entirely of lowercase alphabetic characters, so the pool size is 26 and the password length is 5. This gives:
#
# E = 5 * log2(26) ≈ 23.50 bits
# As another example, the password Tr0ub4dor&3 uses characters from all four pools, so the combined pool size is 94 and the password length is 11. This gives:
#
# E = 11 * log2(94) ≈ 72.10 bits
# Task
# Write a function entropy which takes as its input a valid password and returns the entropy of the password, calculated using the formula above.
#
# MathematicsStrings