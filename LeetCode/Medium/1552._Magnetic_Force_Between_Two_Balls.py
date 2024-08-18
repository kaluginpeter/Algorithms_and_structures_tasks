# In the universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.
#
# Rick stated that magnetic force between two different balls at positions x and y is |x - y|.
#
# Given the integer array position and the integer m. Return the required force.
#
#
#
# Example 1:
#
#
# Input: position = [1,2,3,4,7], m = 3
# Output: 3
# Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs [3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.
# Example 2:
#
# Input: position = [5,4,3,2,1,1000000000], m = 2
# Output: 999999999
# Explanation: We can use baskets 1 and 1000000000.
#
#
# Constraints:
#
# n == position.length
# 2 <= n <= 105
# 1 <= position[i] <= 109
# All integers in position are distinct.
# 2 <= m <= position.length
# Solution Binary Search O(NlogN) O(1)
class Solution:
    def check(
        self, array: list[int], target: int,
        needed: int, upper_boundary: int
    ):
        slow, fast = upper_boundary - 1, upper_boundary - 2
        count_pairs: int = 0
        while fast >= 0:
            if array[slow] - array[fast] >= target:
                count_pairs += 1
                slow = fast
            if array[slow] <= target: break # other numbers will be smaller than target, so just break loop
            fast -= 1
            if count_pairs >= needed - 1: # case if already have needed count of pairs
                return True
        return count_pairs >= needed - 1

    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n: int = len(position)
        left, right = 1, position[-1] - position[0]
        while left <= right:
            middle: int = left + (right - left) // 2
            result: bool = self.check(position, middle, m, n)
            if result:
                left = middle + 1
            else:
                right = middle - 1
        return left - 1