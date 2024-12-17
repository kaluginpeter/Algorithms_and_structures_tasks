# Task
# Given an non-empty list or array (depending on language) of non-empty uppercase words, compute the minimum number of words, which, when removed from the list, leaves the rest of the list in strictly ascending lexicographic order.
#
# Examples:
# ["THE","QUICK","BROWN","FOX","JUMPS","OVER","THE","LAZY","DOG"] should return 4, because removing "THE", "QUICK", "LAZY" & "DOG" leaves the sorted list ["BROWN","FOX","JUMPS","OVER","THE"].
#
# ["JACKDAW","LOVE","MY","BIG","SPHINX","OF","QUARTZ"] should return 2, because removing "BIG" & "SPHINX" leaves the sorted list ["JACKDAW","LOVE","MY","OF","QUARTZ"].
#
# ["A","A","A","A"] should return 3, because equal elements are NOT regarded as sorted, so all but one of them need to be removed.
#
# Source: Midwest Instructional Computing Symposium 2011 http://micsymposium.org/
# Somewhat similar, but harder, kata are Make an increasing sequence and Find the Longest Increasing or Decreasing Combination in an Array
#
# SortingAlgorithmsDynamic Programming
# Solution
def sort_by_exclusion(words):
    n: int = len(words)
    dp: list[int] = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            if words[j - 1] < words[i - 1] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1
    return n - max(dp)