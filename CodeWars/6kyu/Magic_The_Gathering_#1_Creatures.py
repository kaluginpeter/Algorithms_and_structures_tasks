# Magic The Gathering is a collectible card game that features wizards battling against
# each other with spells and creature summons. The game itself can be quite complicated to learn.
# In this series of katas, we'll be solving some of the situations that arise during gameplay.
# You won't need any prior knowledge of the game to solve these contrived problems,
# as I will provide you with enough information.
#
# Creatures
# Each creature has a power and toughness. We will represent this in an array.
# [2, 3] means this creature has a power of 2 and a toughness of 3.
#
# When two creatures square off, they each deal damage equal to their power
# to each other at the same time. This only happens once. If a creature takes
# on damage greater than or equal to their toughness, they die.
#
# Examples:
#
# Creature 1 - [2, 3]
# Creature 2 - [3, 3]
# Creature 3 - [1, 4]
# Creature 4 - [4, 1]
# If creature 1 battles creature 2, creature 1 dies, while 2 survives. If creature
# 3 battles creature 4, they both die, as 3 deals 1 damage to 4, but creature 4 only has a toughness of 1.
#
# Write a function battle(player1, player2) that takes in 2 arrays of creatures.
# Each players' creatures battle each other in order (player1[0] battles the creature
# in player2[0]) and so on. If one list of creatures is longer than the other,
# those creatures are considered unblocked, and do not battle.
#
# Your function should return an object (a hash in Ruby) with the keys player1
# and player2 that contain the power and toughness of the surviving creatures.
#
# Example:
#
# player1 = [[1, 1], [2, 1], [2, 2], [5, 5]];
# player2 = [[1, 2], [1, 2], [3, 3]];
# battle(player1, player2) ->
# { 'player1': [[5, 5]],
#   'player2': [[1, 2], [3, 3]] }
# Good luck with your battles!
#
# Check out my other Magic The Gathering katas:
# Magic The Gathering #1: Creatures
# Magic The Gathering #2: Mana
#
# ALGORITHMSFUNDAMENTALSARRAYSGAMES
# Solution
def battle(p1, p2):
    l1,l2 =p1[:], p2[:]
    for i,j in zip(p1, p2):
        if i[0]>=j[1] : l2.remove(j)
        if j[0]>=i[1] : l1.remove(i)
    return {'player1':l1,'player2':l2}