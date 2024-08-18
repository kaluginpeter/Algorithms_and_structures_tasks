# Given a sorted array of numbers, return the summary of its ranges.
#
# Examples
# summary_ranges([1, 2, 3, 4]) == ["1->4"]
# summary_ranges([1, 1, 1, 1, 1]) == ["1"]
# summary_ranges([0, 1, 2, 5, 6, 9]) == ["0->2", "5->6", "9"]
# summary_ranges([0, 1, 2, 3, 3, 3, 4, 5, 6, 7]) == ["0->7"]
# summary_ranges([0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10]) == ["0->7", "9->10"]
# summary_ranges([-2, 0, 1, 2, 3, 3, 3, 4, 4, 5, 6, 7, 7, 9, 9, 10, 12]) == ["-2", "0->7", "9->10", "12"]
# ARRAYSALGORITHMS
# Solution
def summary_ranges(nums):
    nums.append(float("inf"))
    i, l = nums[0], []
    for a, b in zip(nums, nums[1:]):
        if b - a > 1:
            l.append(str(i) if i == a else f"{i}->{a}")
            i = b
    return l