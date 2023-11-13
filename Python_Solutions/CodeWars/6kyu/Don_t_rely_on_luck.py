# The test fixture I use for this kata is pre-populated.
#
# It will compare your guess to a random number generated using:
#
# randint(1,100)
# You can pass by relying on luck or skill but try not to rely on luck.
#
# "The power to define the situation is the ultimate power." - Jerry Rubin
#
# Good luck!
#
# GAMESPUZZLES
# Solution
from random import randint,seed
seed(1)
guess = randint(1,100)
seed(1)