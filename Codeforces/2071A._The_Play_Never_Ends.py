# A. The Play Never Ends
# time limit per test1 second
# memory limit per test256 megabytes
# Let's introduce a two-player game, table tennis, where a winner is always decided and draws are impossible.
#
# Three players, Sosai, Fofo, and Hohai, want to spend the rest of their lives playing table tennis. They decided to play forever in the following way:
#
# In each match, two players compete while the third spectates.
#
# To ensure fairness, no player can play three times in a row. The player who plays twice in a row must sit out as a spectator in the next match, which will be played by the other two players. Otherwise, the winner and the spectator will play in the next match, while the loser will spectate.
# Now, the players, fully immersed in this infinite loop of matches, have tasked you with solving the following problem:
#
# Given an integer k
# , determine whether the spectator of the first match can be the spectator in the k
# -th match.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤1000
# ). The description of the test cases follows.
#
# The only line of each test case contains one integer k
#  (1≤k≤109
# ).
#
# Output
# For each test case, print "YES" (without quotes) if the spectator of the first match can be the spectator of the k
# -th match, and "NO" (without quotes) otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 4
# 1
# 2
# 333
# 1000000000
# OutputCopy
# YES
# NO
# NO
# YES
# Note
# In the first test case, the spectator of the first match is already a spectator in the 1
# st match.
#
# In the second test case, the spectator of the first match will play in the 2
# nd match regardless of the result of the first match.