# Description:
# Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 strings and return the one who's stronger.
#
# Rules:
# Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
# Strings will consist of uppercase letters only
# Only two groups to a fight.
# Group whose total power (A + B + C + ...) is bigger wins.
# If the powers are equal, it's a tie.
# Examples:
#       * "ONE", "TWO"  -> "TWO"`
#       * "ONE", "NEO"  -> "Tie!"
# Related kata:
# Battle of the characters (Medium)
# ALGORITHMS
# Solution
def battle(x, y):
    s = [sum([ord(i)-64 for i in x]), sum([ord(i)-64 for i in y])]
    return x if s[0] > s[1] else y if s[1] > s[0] else 'Tie!'