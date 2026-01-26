# Previous Kata
# This kata is a harder version of This Kata. Be sure to check that one out first.
#
# Faro Shuffle
# A Faro Shuffle is a way of shuffling a deck of cards. It can be performed in two ways: in-shuffle and out-shuffle. For this kata, we will only consider the out-shuffle.
#
# An out-shuffle is performed by splitting the deck into two equal halves and then interleaving the cards from each half, starting with the top card of the first half. For example, if we have a deck of 8 cards numbered from 1 to 8, the out-shuffle would look like this:
#
# 1 2 3 4 5 6 7 8 ->
# 1 5 2 6 3 7 4 8 ->
# 1 3 5 7 2 4 6 8 ->
# 1 2 3 4 5 6 7 8
# Notice that after 3 shuffles, the deck returns to its original order. This is a property of the out-shuffle, for a standard deck of 52 cards, it takes 8 shuffles to return to the original order.
#
# Task
# Given the size of a deck of cards n, return the minimum number of out-shuffles required to return the deck to its original order. Consider that the deck is numbered from 1 to n and that n is a positive even number.
#
# A brute force solution with O(n) or worse complexity will not pass. You are expected to handle large values of n efficiently. More information about the tests will be provided in the Solution Setup.
#
# Examples
# # (1 2 -> 1 2)
# 2 -> 1
#
# # (1 2 3 4 -> 1 3 2 4 -> 1 2 3 4)
# 4 -> 2
#
# # (1 2 3 4 5 6 -> 1 4 2 5 3 6 -> 1 5 4 3 2 6 -> 1 3 5 2 4 6 -> 1 2 3 4 5 6)
# 6 -> 4
#
# 10 ** 14 -> 2565451980
# MathematicsNumber TheoryPerformance