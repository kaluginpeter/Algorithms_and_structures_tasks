# Tandem Duplication on Binary Strings
# Let TD(l, r) denote the tandem duplication operation on a binary string. It duplicates the substring indexed by [l, r) (l inclusive and r exclusive) and inserts the duplicated substring immediately after its original occurrence.

# For example:

# 1100 = 1[10]0 --TD(1, 3)--> 1[10][10]0 = 110100
# 00110 = 00[110] --TD(2, 5)--> 00[110][110] = 00110110
# Given a target binary string S, determine whether it can be obtained from the initial string 01 by applying TD zero or more times.

# If it is possible, output any valid sequence of operations. Otherwise, output null.

# Input
# A single line containing a binary string S.

# 1 <= |S| < 10^5
# Output
# If the target is impossible to construct, output:

# null
# Otherwise output any valid operation sequence:

# [(l_0, r_0), (l_1, r_1), ..., (l_m, r_m)]
# where (l_i, r_i) means applying TD(l_i, r_i) at step i.

# Examples
# Example 1
# Input:

# 0101101
# One possible construction is:

# 01 = [01] --TD(0, 2)--> [01][01] = 0101
# 0101 = 0[101] --TD(1, 4)--> 0[101][101] = 0101101
# So a valid output is:

# [(0, 2), (1, 4)]
# Example 2
# Input:

# 111
# This string cannot be obtained from 01 using only TD operations.

# Output:

# null
# Optimal solution has time complexity O(N).

# AlgorithmsPerformance