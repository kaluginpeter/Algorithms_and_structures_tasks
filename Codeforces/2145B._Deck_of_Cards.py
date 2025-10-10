# B. Deck of Cards
# time limit per test2 seconds
# memory limit per test256 megabytes
# Monocarp has a deck of cards numbered from 1
#  to n
# . Initially, the cards are arranged from smallest to largest, with 1
#  on top and n
#  at the bottom.
#
# Monocarp performed k
#  actions on the deck. Each action was one of three types:
#
# remove the top card;
# remove the bottom card;
# remove either the top or bottom card.
# Your task is to determine the fate of each card: whether it remains in the deck, has been removed, or might be both.
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤k≤n≤2⋅105
# ).
#
# The second line contains a string s
#  of length k
# , consisting of characters 0, 1, and/or {2}. This string describes Monocarp's actions. If the i
# -th character is 0, Monocarp removes the top card on the i
# -th action. If it's 1, he removes the bottom card. If it's 2, either the top or bottom card can be removed.
#
# Additional constraint on the input: the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, print a string consisting of n
#  characters. The i
# -th character should be + (plus sign) if the i
# -th card is still in the deck, - (minus sign) if it has been removed, or ? (question mark) if its state is unknown.
#
# Example
# InputCopy
# 4
# 4 2
# 01
# 3 2
# 22
# 1 1
# 2
# 7 5
# 01201
# OutputCopy
# -++-
# ???
# -
# --?+?--