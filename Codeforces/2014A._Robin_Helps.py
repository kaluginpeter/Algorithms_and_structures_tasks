# A. Robin Helps
# time limit per test1 second
# memory limit per test256 megabytes
# There is a little bit of the outlaw in everyone, and a little bit of the hero too.
# The heroic outlaw Robin Hood is famous for taking from the rich and giving to the poor.
#
# Robin encounters n
#  people starting from the 1
# -st and ending with the n
# -th. The i
# -th person has ai
#  gold. If ai≥k
# , Robin will take all ai
#  gold, and if ai=0
# , Robin will give 1
#  gold if he has any. Robin starts with 0
#  gold.
#
# Find out how many people Robin gives gold to.
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
# , k
#  (1≤n≤50,1≤k≤100
# ) — the number of people and the threshold at which Robin Hood takes the gold.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (0≤ai≤100
# ) — the gold of each person.
#
# Output
# For each test case, output a single integer, the number of people that will get gold from Robin Hood.
#
# Example
# InputCopy
# 4
# 2 2
# 2 0
# 3 2
# 3 0 0
# 6 2
# 0 3 0 0 0 0
# 2 5
# 5 4
# OutputCopy
# 1
# 2
# 3
# 0
# Note
# In the first test case, Robin takes 2
#  gold from the first person and gives a gold to the second person.
#
# In the second test case, Robin takes 3
#  gold and gives 1
#  gold to each of the next 2
#  people.
#
# In the third test case, Robin takes 3
#  gold and so only gives gold to 3
#  other people.