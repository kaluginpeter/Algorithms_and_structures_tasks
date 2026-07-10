# Given a non-negative number, return the next bigger polydivisible number, or an empty value like null or Nothing.
#
# A number is polydivisible if its first digit is cleanly divisible by 1, its first two digits by 2, its first three by 3, and so on. There are finitely many polydivisible numbers.
#
# Algorithms
# Solution
from bisect import bisect_right

nums = []

def dfs(prefix, length):
    if length > 25: return
    if length: nums.append(prefix)
    for d in range(10):
        if length == 0 and d == 0: continue
        x = prefix * 10 + d
        if x % (length + 1) == 0: dfs(x, length + 1)

dfs(0, 0)
nums.sort()
def next_num(n):
    i = bisect_right(nums, n)
    if i == len(nums): return None
    return nums[i]