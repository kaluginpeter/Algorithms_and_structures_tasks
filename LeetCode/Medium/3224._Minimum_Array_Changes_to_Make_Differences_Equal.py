# You are given an integer array nums of size n where n is even, and an integer k.
#
# You can perform some changes on the array, where in one change you can replace any element in the array with any integer in the range from 0 to k.
#
# You need to perform some changes (possibly none) such that the final array satisfies the following condition:
#
# There exists an integer X such that abs(a[i] - a[n - i - 1]) = X for all (0 <= i < n).
# Return the minimum number of changes required to satisfy the above condition.
#
#
#
# Example 1:
#
# Input: nums = [1,0,1,2,4,3], k = 4
#
# Output: 2
#
# Explanation:
# We can perform the following changes:
#
# Replace nums[1] by 2. The resulting array is nums = [1,2,1,2,4,3].
# Replace nums[3] by 3. The resulting array is nums = [1,2,1,3,4,3].
# The integer X will be 2.
#
# Example 2:
#
# Input: nums = [0,1,2,3,3,6,5,4], k = 6
#
# Output: 2
#
# Explanation:
# We can perform the following operations:
#
# Replace nums[3] by 0. The resulting array is nums = [0,1,2,0,3,6,5,4].
# Replace nums[4] by 4. The resulting array is nums = [0,1,2,0,4,6,5,4].
# The integer X will be 4.
#
#
#
# Constraints:
#
# 2 <= n == nums.length <= 105
# n is even.
# 0 <= nums[i] <= k <= 105
# Solution HashTable Sorting Greedy O(NlogN) O(N)
from collections import defaultdict
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        n: int = len(nums)
        pairs: list[tuple[int, int]] = []
        freq: dict[int, int] = defaultdict(int)
        for i in range(n // 2):
            freq[abs(nums[i] - nums[n - i - 1])] += 1
            pairs.append((nums[i], nums[n - i - 1]))

        change_count: dict[int, int] = defaultdict(int)
        # Sorting freq by frequences and values in descending order
        freq = sorted(freq, key=lambda x: (freq[x], x), reverse=True)
        for X in freq[:100]: # Give first 100(or less if len(freq) < 100) possible X
            current_changes: int = 0 # Needed swaps
            for a, b in pairs:
                if abs(a - b) != X:
                    if 0 <= a - X <= k or 0 <= b + X <= k:
                        current_changes += 1 # Swap one number
                    elif 0 <= b - X <= k or 0 <= a + X <= k:
                        current_changes += 1 # Swap one number
                    else:
                        current_changes += 2 # Swap two number
            change_count[X] = current_changes # For current X store count fo swaps

        return min(change_count.values())