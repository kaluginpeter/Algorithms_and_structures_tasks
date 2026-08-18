/*
You are given an integer array nums and an integer k.

An integer x is almost missing from nums if x appears in exactly one subarray of size k within nums.

Return the largest almost missing integer from nums. If no such integer exists, return -1.

A subarray is a contiguous sequence of elements within an array.


Example 1:

Input: nums = [3,9,2,1,7], k = 3

Output: 7

Explanation:

1 appears in 2 subarrays of size 3: [9, 2, 1] and [2, 1, 7].
2 appears in 3 subarrays of size 3: [3, 9, 2], [9, 2, 1], [2, 1, 7].
3 appears in 1 subarray of size 3: [3, 9, 2].
7 appears in 1 subarray of size 3: [2, 1, 7].
9 appears in 2 subarrays of size 3: [3, 9, 2], and [9, 2, 1].
We return 7 since it is the largest integer that appears in exactly one subarray of size k.

Example 2:

Input: nums = [3,9,7,2,1,7], k = 4

Output: 3

Explanation:

1 appears in 2 subarrays of size 4: [9, 7, 2, 1], [7, 2, 1, 7].
2 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
3 appears in 1 subarray of size 4: [3, 9, 7, 2].
7 appears in 3 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1], [7, 2, 1, 7].
9 appears in 2 subarrays of size 4: [3, 9, 7, 2], [9, 7, 2, 1].
We return 3 since it is the largest and only integer that appears in exactly one subarray of size k.

Example 3:

Input: nums = [0,0], k = 1

Output: -1

Explanation:

There is no integer that appears in only one subarray of size 1.



Constraints:

1 <= nums.length <= 50
0 <= nums[i] <= 50
1 <= k <= nums.length
*/
// Solution
// Python O(N) O(D) HashMap
from collections import Counter
class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        seen: dict[int, int] = Counter(nums)
        output: int = -1
        overall: int = -1
        for num, freq in seen.items():
            if freq == 1: output = max(output, num)
            overall = max(overall, num)
        if k == len(nums): return overall
        elif k == 1: return output
        x: int = nums[0] if seen[nums[0]] == 1 else -1
        y: int = nums[-1] if seen[nums[-1]] == 1 else -1
        return max(x, y)

// C++ O(N) O(D) HashMap
class Solution {
public:
    int largestInteger(vector<int>& nums, int k) {
        std::unordered_map<int, size_t> seen;
        for (int& num : nums) ++seen[num];
        int output = -1, overall = -1;
        for (auto& p : seen) {
            if (p.second == 1) output = std::max(output, p.first);
            overall = std::max(overall, p.first);
        }
        if (k == nums.size()) return overall;
        if (k == 1) return output;
        int x = nums[0], y = *--nums.end();
        if (seen[x] > 1) x = -1;
        if (seen[y] > 1) y = -1;
        return std::max(x, y);
    }
};

// Go O(N) O(D) HashMap
func largestInteger(nums []int, k int) int {
    seen := make(map[int]int)
    for _, num := range(nums) {
        seen[num]++
    }
    var output, overall int = -1, -1
    for num, freq := range(seen) {
        if freq == 1 {
            output = max(output, num)
        }
        overall = max(overall, num)
    }
    if k == len(nums) {
        return overall
    } else if k == 1 {
        return output
    }
    var x, y int = nums[0], nums[len(nums) - 1]
    if seen[x] > 1 {
        x = -1
    }
    if seen[y] > 1 {
        y = -1
    }
    return max(x, y)
}