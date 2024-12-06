# B. Grab the Candies
# time limit per test1 second
# memory limit per test256 megabytes
# Mihai and Bianca are playing with bags of candies. They have a row a
#  of n
#  bags of candies. The i
# -th bag has ai
#  candies. The bags are given to the players in the order from the first bag to the n
# -th bag.
#
# If a bag has an even number of candies, Mihai grabs the bag. Otherwise, Bianca grabs the bag. Once a bag is grabbed, the number of candies in it gets added to the total number of candies of the player that took it.
#
# Mihai wants to show off, so he wants to reorder the array so that at any moment (except at the start when they both have no candies), Mihai will have strictly more candies than Bianca. Help Mihai find out if such a reordering exists.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the number of bags in the array.
#
# The second line of each test case contains n
#  space-separated integers ai
#  (1≤ai≤100
# ) — the number of candies in each bag.
#
# Output
# For each test case, output "YES" (without quotes) if such a reordering exists, and "NO" (without quotes) otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 3
# 4
# 1 2 3 4
# 4
# 1 1 1 2
# 3
# 1 4 3
# OutputCopy
# YES
# NO
# NO
# Note
# In the first test case, Mihai can reorder the array as follows: [4,1,2,3]
# . Then the process proceeds as follows:
#
# the first bag has 4
#  candies, which is even, so Mihai takes it — Mihai has 4
#  candies, and Bianca has 0
# .
# the second bag has 1
#  candies, which is odd, so Bianca takes it — Mihai has 4
#  candies, and Bianca has 1
# .
# the third bag has 2
#  candies, which is even, so Mihai takes it — Mihai has 6
#  candies, and Bianca has 1
# .
# the fourth bag has 3
#  candies, which is odd, so Bianca takes it — Mihai has 6
#  candies, and Bianca has 4
# .
# Since Mihai always has more candies than Bianca, this reordering works.