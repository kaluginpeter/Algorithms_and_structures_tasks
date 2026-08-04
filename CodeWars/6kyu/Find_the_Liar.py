# # #
# Situation
# Alice and Bob work in an office. Sometimes they play word-games when the boss is out, but yesterday (Tuesday) their boss sent out a surprise memo to the entire office (be sure to also solve the previous kata about yesterday's memo), and so they actually ended up with some actual "work" to do.
#
# The memo instructed each employee to document a list of co-workers with whom they had happened to speak at the meeting yesterday (Monday). Meanwhile, the memo was oddly urgent about one particular matter: the order of the list should be based not on when employees spoke, but instead on what time they had actually arrived to the meeting.
#
# Lasty, the memo stated that there would be a hearing held the following day (Wednesday) to vet the data. And so that day is today and it is now time for the hearing to commence. What the employees didn't realize is that the boss is certain that exactly one employee will not tell the truth. And now all that remains to reveal the liar is to carefully compare employee submissions.
#
#
# Task
# Given a two-dimentional (list) of numbers representing employee testimonies as (list)s of employee ID's, determine which sub-(list) does not have all of its numbers in an order that conforms to the orders of the numbers in all other (list)s.
#
#
# Notes
# The sub-(list)s of ID numbers will always be created in such a way that there is guaranteed to be exactly one (1) sub-(list) that does not agree with others.
# It is further guaranteed that there will be sufficient evidence provided within the sub-(list)s to be able to determine which one does not agree.
# As part of making the actual task of finding the liar much more simple, the boss purposely went back a step in preparing their entire strategy by assigning meetings to specific employees such that the discovery would always be possible with an explicit determination. This means that for any one liar, there are guaranteed to have been scheduled at least two other employees' meetings arranged which have a direct disagreement with the liar on at least one pair of ID numbers. This means that for what could have been a potential test case like this
# office = ((1, 2),
#           (1, 2),
#           (2, 3),
#           (2, 3),
#           (3, 1))  #  <----- the liar!
# the result can be found only via an implicit determination, given that no two employees have any actual disagreement with each others' (list) orderings. Thus, due to the boss and his careful scheming, tests of this nature are guaranteed not be part of solving this kata.
#
# Example
# Given the (list)s:
#
# office = ((2, 9, 6),
#           (9, 5, 6),  #  <----  the liar!
#           (2, 9, 5),
#           (9, 6, 5),
#           (2, 6, 5))
# the sub-(list) located at index 1 (9, 5, 6) does not agree with the others because the number 5 appears before the number 6, where as 5 appears after 6 in all other sub-(list)s that contain both of these numbers.
#
#
# Input
# A two-dimentional (array, list, tuple, or vector) of (arrays, lists, tuples, or vectors) of unsigned integers.
#
#
# Output
# The index of the sub-(list) within the primary (list) which does not agree with the others according to the ordering of their numbers throughout all sub-(list)s.
#
#
# Enjoy!
# You may consider one of the following kata to solve next:
#
# Is Sator Square?
# Playing With Toy Blocks ~ Can you build a 4x4 square?
# Four Letter Words ~ Mutations
# Crossword Puzzle! (2x2)
# Interlocking Binary Pairs
# Setting Places for the Dead
# Four Letter Words ~ Anagrams
# Shuffle an Integer
# Minimum Percentage of Visitors that Ate All Foods
# The Jumbler
# Do They Agree?