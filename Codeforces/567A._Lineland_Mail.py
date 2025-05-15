# A. Lineland Mail
# time limit per test3 seconds
# memory limit per test256 megabytes
# All cities of Lineland are located on the Ox coordinate axis. Thus, each city is associated with its position xi — a coordinate on the Ox axis. No two cities are located at a single point.
#
# Lineland residents love to send letters to each other. A person may send a letter only if the recipient lives in another city (because if they live in the same city, then it is easier to drop in).
#
# Strange but true, the cost of sending the letter is exactly equal to the distance between the sender's city and the recipient's city.
#
# For each city calculate two values ​​mini and maxi, where mini is the minimum cost of sending a letter from the i-th city to some other city, and maxi is the the maximum cost of sending a letter from the i-th city to some other city
#
# Input
# The first line of the input contains integer n (2 ≤ n ≤ 105) — the number of cities in Lineland. The second line contains the sequence of n distinct integers x1, x2, ..., xn ( - 109 ≤ xi ≤ 109), where xi is the x-coordinate of the i-th city. All the xi's are distinct and follow in ascending order.
#
# Output
# Print n lines, the i-th line must contain two integers mini, maxi, separated by a space, where mini is the minimum cost of sending a letter from the i-th city, and maxi is the maximum cost of sending a letter from the i-th city.
#
# Examples
# InputCopy
# 4
# -5 -2 2 7
# OutputCopy
# 3 12
# 3 9
# 4 7
# 5 12
# InputCopy
# 2
# -1 1
# OutputCopy
# 2 2
# 2 2