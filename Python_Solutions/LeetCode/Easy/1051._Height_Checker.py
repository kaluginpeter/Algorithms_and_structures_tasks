# A school is trying to take an annual photo of all the students. The students are asked to stand in a single file line in non-decreasing order by height. Let this ordering be represented by the integer array expected where expected[i] is the expected height of the ith student in line.
#
# You are given an integer array heights representing the current order that the students are standing in. Each heights[i] is the height of the ith student in line (0-indexed).
#
# Return the number of indices where heights[i] != expected[i].
#
#
#
# Example 1:
#
# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
# heights:  [1,1,4,2,1,3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# Example 2:
#
# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights:  [5,1,2,3,4]
# expected: [1,2,3,4,5]
# All indices do not match.
# Example 3:
#
# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights:  [1,2,3,4,5]
# expected: [1,2,3,4,5]
# All indices match.
#
#
# Constraints:
#
# 1 <= heights.length <= 100
# 1 <= heights[i] <= 100
# Solution Sorting One line O(NlogN) O(N)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(i != j for i, j in zip(heights, sorted(heights)))
# Solution Counting O(N) O(N)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        arr: list[int] = [0] * 101
        ans: int = 0
        idx: int = 0
        for i in heights:
            arr[i] += 1
        for i in heights:
            while not arr[idx]:
                idx += 1
            if idx != i:
                ans += 1
            arr[idx] -= 1
        return ans

# Solution Counting sorting O(N) O(N)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        correct_height: list[int] = []
        total_students: list[int] = [0 for _ in range(max(heights) + 1)]
        for student in heights:
            total_students[student] += 1
        for student in range(len(total_students)):
            if total_students[student] > 0:
                correct_height += [student] * total_students[student]
        return sum(correct_height[idx] != heights[idx] for idx in range(len(heights)))