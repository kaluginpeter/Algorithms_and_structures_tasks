# Subsequence Sums
# Task
# Given a sequence of integers named arr, find the number of continuous subsequences (sublist or subarray) in arr that sum up to s. A continuous subsequence can be defined as a sequence inbetween a start index and stop index (inclusive) of the sequence. For instance, [2, 3, 4] is a continuous subsequence of [1, 2, 3, 4, 5] , but [3, 5] and [4, 1] are not.
#
# PERFORMANCE REQUIREMENTS
#
# The length of arr is
# ≤
# ≤ 10,000. The contents of arr can range from -10000 to 10000.
#
# SAMPLE INPUTS & OUTPUTS
#
# arr = [1, 2, 3, -3, -2, -1], s = 0 -> 3
# # [3, -3], [2, 3, -3, -2], [1, 2, 3, -3, -2, -1]
# ------------------------------------------------------------
# arr = [1, 5, -2, 4, 0, -7, -3, 6], s = 4 -> 4
# # [1, 5, -2], [4], [4, 0], [1, 5, -2, 4, 0, -7, -3, 6]
# ------------------------------------------------------------
# arr = [9, -2, -5, 8, 6, -10, 0, -4], s = -1 -> 2
# # [-5, 8, 6, -10], [-5, 8, 6, -10, 0]
# Dynamic ProgrammingMathematicsAlgorithms
# Solution
def subsequence_sums(arr, s):
    cumulative_sum = 0
    sum_count = {0: 1}
    output = 0
    for num in arr:
        cumulative_sum += num
        if (cumulative_sum - s) in sum_count:
            output += sum_count[cumulative_sum - s]
        if cumulative_sum in sum_count:
            sum_count[cumulative_sum] += 1
        else:
            sum_count[cumulative_sum] = 1

    return output