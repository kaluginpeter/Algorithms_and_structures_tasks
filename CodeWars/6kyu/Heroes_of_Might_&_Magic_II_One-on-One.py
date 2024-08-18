# Inspired by another Kata - Heroes of Might & Magic II: Chain Lightning by Firefly2002, I thought I
# might have a go at another Kata related to this game.
#
# In this Kata, two groups of monsters will attack each other, and your job is to find out who wins.
# Each group will have a stat for each of the following: number of units, hitpoints per unit, damage
# per unit, and monster type.
#
# If you are not familiar with the game, just think of each group as standing in a line so that
# when they are attacked the unit at the front of the line takes the hit before the others, and if
# he dies the remaining damage will hit the next unit and so on. Therefore multiple units
# (or even the whole group) can die in one attack.
#
# Each group takes turns attacking, and does so until only one remains. In this kata, the first entry
# in the input array is the first to attack.
#
# The inputs for this game will be two dictionaries, each with the stats of each monster.
# Using these stats, calculate which group wins, and how many units in that group stay alive
# (unless they are undead :P), and return it as a string - formatted as below:
#
# Input:
# mon1 = {"type": "Roc",     "hitpoints": 40, "number": 6, "damage" : 8 }
# mon2 = {"type": "Unicorn", "hitpoints": 40, "number": 4, "damage" : 13}
#
# Output:
# "[NUMBER] [TYPE](s) won"   # in this case "5 Roc(s) won"
# The damage of each attack is calculated simply as (number of units) * (damage per unit).
#
# You must also take into account that the first unit in the group may injured BUT he still attacks with full strength.
#
# Fighting mechanics explanation:
#
# mon1 = {"type": "Roc",     "hitpoints": 40, "number": 6, "damage":8 }
# mon2 = {"type": "Unicorn", "hitpoints": 40, "number": 4, "damage":13}
#
# 1) The Rocs attack the Unicorns for 48 damage (6 * 8),
#    killing one and damaging the next - leaving it with 32/40 hitpoints.
# 2) The remaining 3 Unicorns attack the Rocs for 39 damage (3 * 13),
#    killing 0 but leaving the first one with only 1/40 hitpoints.
# 3) Repeat until one of the groups is left with 0 units in total.
# FUNDAMENTALS
# Solution
from math import ceil
def who_would_win(m1, m2):
    m1['allhit'] = m1['hitpoints'] * m1['number']
    m2['allhit'] = m2['hitpoints'] * m2['number']
    while True:
        m2['allhit'] = m2['allhit'] - m1['number'] * m1['damage']
        m2['number'] = ceil(m2['allhit'] / m2['hitpoints'])
        if not m2['number'] > 0: return f"{m1['number']} {m1['type']}(s) won"
        m1['allhit'] = m1['allhit'] - m2['number'] * m2['damage']
        m1['number'] = ceil(m1['allhit'] / m1['hitpoints'])
        if not m1['number'] > 0: return f"{m2['number']} {m2['type']}(s) won"