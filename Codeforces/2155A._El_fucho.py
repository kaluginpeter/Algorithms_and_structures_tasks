# A. El fucho
# time limit per test1 second
# memory limit per test256 megabytes
# Juan and his friends are going to split themselves into n
#  teams and play a modified double-elimination football tournament, consisting of a winners' group and a losers' group. Initially, all teams belong to the winners' group.
#
# In each round of the tournament, the following happens as long as one of the groups has at least two teams:
#
# All teams in the winners' group pair up.
# If there is an odd number of teams in the winners' group, there would be a team that didn't get paired up (and wouldn't play a match). That team stays in the winners' group.
# For teams in the winners' that got paired up, each pair plays a football match in which there are no ties.
# If a team wins, it stays in the winners' group.
# If a team loses, it drops down to the losers' group in the next round.
# All teams in the losers' group pair up.
# If there is an odd number of teams in the losers' group, there would be a team that didn't get paired up (and wouldn't play a match). That team stays in the losers' group.
# For teams in the losers' that got paired up, each pair plays a football match in which there are no ties.
# If a team wins, it stays in the losers' group.
# If a team loses, it gets eliminated from the tournament.
# Note that in the above process, when a team loses a match in the winners' group, it drops down to the losers' group in the next round. That means, it is not considered for the pairing process in the current round's losers' group.
#
# After multiple iterations of the aforementioned process, both groups end up with a single team each. When this happens, both teams face off against each other in a match and a victor emerges.
#
# Determine how many matches were played in total. It can be proved that no matter how the teams are paired up and which ones win and lose, the answer remains the same.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The only line of each test case contains one positive integer n
#  (2≤n≤500
# ) — the number of teams.
#
# Output
# For each test case, print the total number of matches played during the tournament.
#
# Example
# InputCopy
# 2
# 2
# 3
# OutputCopy
# 2
# 4
# Note
# In the first test case, it can be proved that exactly 2
#  matches are played before a victor is declared.
#
# In the second test case, the image below shows one possible tournament. Notice that 4
#  matches were played in total.