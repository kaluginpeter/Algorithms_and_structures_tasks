# Generala is a dice game popular in South America. It's very similar to Yahtzee but with a different scoring approach. It is played with 5 dice, and the possible results are:
#
# Result	Points	Rules	Samples
# GENERALA	50	When all rolled dice are of the same value.	66666, 55555, 44444, 11111, 22222, 33333.
# POKER	40	Four rolled dice are of the same value.	44441, 33233, 22262.
# FULLHOUSE	30	Three rolled dice are of the same value, the remaining two are of a different value, but equal among themselves.	12121, 44455, 66116.
# STRAIGHT	20	Rolled dice are in sequential order. Dice with value 1 is a wildcard that can be used at the beginning of the straight before a 2, or at the end of it after a 6.	12345, 23456, 34561, 13654, 62534.
# Anything else	0	Anything else will return 0 points.	44421, 61623, 12346.
# Please note that dice are not in order; for example 12543 qualifies as a STRAIGHT. Also, No matter what string value you get for the dice, you can always reorder them any order you need to make them qualify as a STRAIGHT. I.E. 12453, 16543, 15364, 62345 all qualify as valid STRAIGHTs.
#
# Complete the function that is given the rolled dice as a string of length 5 and return the points scored in that roll. You can safely assume that provided parameters will be valid:
#
# String of length 5,
# Each character will be a number between 1 and 6
# GamesAlgorithms
# Solution
def points(dice):
    s_d: set[str] = set(dice)
    if len(s_d) == 1: return 50
    if any(dice.count(d) == 4 for d in s_d): return 40
    if len(s_d) == 2 and any(dice.count(d) == 3 for d in s_d): return 30
    ordering: list[str] = sorted(s_d)
    if len(s_d) == 5:
        if ordering[0] == '1': ordering.pop(0)
        return 20 if all(int(y) - int(x) == 1 for x, y in zip(ordering, ordering[1:])) else 0
    return 0