# Given a possibly empty list of strictly positive numbers and a non-negative target number, return either a subset of the list summing to the target, or null or a similar empty value if no such subset exists.
#
# The subset must consist of unique ( by index ) list elements.
# If a particular value occurs more than once in the input list, you can use it up to as many times as it occurs.
# The empty subset sums to 0.
# If multiple valid subsets exist, return any one of them.
#
# The target will never be much bigger than the sum of the input list, and often quite a bit smaller.
#
# Performance
# Solution
def subset_sum(numbers,target):
    if target == 0: return []
    dp = {0: []}
    for num in numbers:
        for s in list(dp.keys()):
            new_sum = s + num
            if new_sum <= target and new_sum not in dp:
                dp[new_sum] = dp[s] + [num]
                if new_sum == target:
                    return dp[new_sum]
    return None if target not in dp else dp[target]