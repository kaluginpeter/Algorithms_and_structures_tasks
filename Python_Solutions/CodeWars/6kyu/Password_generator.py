# You need to write a password generator that meets the following criteria:
#
# 6 - 20 characters long
# contains at least one lowercase letter
# contains at least one uppercase letter
# contains at least one number
# contains only alphanumeric characters (no special characters)
# Return the random password as a string.
#
# Note: "randomness" is checked by counting the characters used in the generated passwords -
# all characters should have less than 50% occurance. Based on extensive tests, the normal rate is around 35%.
#
# REGULAR EXPRESSIONSSECURITYFUNDAMENTALS
# Solution
from string import ascii_lowercase as LOWER, ascii_uppercase as UPPER, digits as DIGITS
from random import choice, shuffle, randint
def password_gen():
    w = [choice(UPPER), choice(LOWER), choice(DIGITS)] + [choice(UPPER+LOWER+DIGITS) for i in range(randint(3, 17))]
    shuffle(w)
    return "".join(w)