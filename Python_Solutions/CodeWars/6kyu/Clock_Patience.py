# In this Kata you will be playing Clock Patience which is a single-player card game of chance requiring zero skill.
#
# Input
# cards a shuffled deck of 52 playing cards represented as a string array
# card values are A,2,3,4,5,6,7,8,9,10,J,Q,K (suits are not relevant)
# Process
# Within the Kata method you will need to:
#
# "Deal" the cards face down one at a time into clock positions
#
# First card at 1 o'clock position, 2nd at 2 o'clock... 12th at 12 o'clock, 13th card in the centre
#
# Repeat 4 times.
#
# When all cards are dealt there will be 13 piles of 4 cards each
#
# See here for the general idea (but use this Kata's dealing rules)
#
# "Play" the game according to these RULES
#
# Start by turning over the top card in the clock centre
#
# Place that card face up at the clock position associated with its card-value:
#
# A at 1 o'clock
# 2 at 2 o'clock
# 3 at 3 o'clock
# ...
# Q at 12 o'clock
# K in the centre
# Next turn over the top card of the pile at this new clock position
#
# REPEAT until no more moves are possible
#
# This happens only when the 4th King (K) is revealed
# See here for clarification of these rules
#
# Kata Task
# Return the number of cards still remaining face down when the game ends (a winning game would return 0)
#
# ALGORITHMS