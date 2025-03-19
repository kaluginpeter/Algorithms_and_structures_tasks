# You are given a
# binary array
#  nums.
#
# You can do the following operation on the array any number of times (possibly zero):
#
# Choose any 3 consecutive elements from the array and flip all of them.
# Flipping an element means changing its value from 0 to 1, and from 1 to 0.
#
# Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.
#
#
#
# Example 1:
#
# Input: nums = [0,1,1,1,0,0]
#
# Output: 3
#
# Explanation:
# We can do the following operations:
#
# Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
# Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
# Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
# Example 2:
#
# Input: nums = [0,1,1,1]
#
# Output: -1
#
# Explanation:
# It is impossible to make all elements equal to 1.
#
#
#
# Constraints:
#
# 3 <= nums.length <= 105
# 0 <= nums[i] <= 1
# Solution Straight Forward O(N) O(1)
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        idx: int = 0
        count: int = 0
        while idx < len(nums) - 2:
            if nums[idx] == 0:
                count += 1
                nums[idx], nums[idx + 1], nums[idx + 2] = 1, int(not nums[idx + 1]), int(not nums[idx + 2])
            idx += 1
        return [-1, count][nums[-2] == nums[-1] == 1]


# Python O(N) O(N) Queue
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        q: list[int] = deque()
        output: int = 0
        steps: int = 0
        for i in range(len(nums)):
            if q and i - 3 >= q[0]:
                steps -= 1
                q.popleft()
            if not ((nums[i] + steps) % 2):
                if i + 3 > len(nums): return -1
                steps += 1
                output += 1
                q.append(i)
        return output

# C++ O(N) O(N) Queue
class Solution {
public:
    int minOperations(vector<int>& nums) {
        int steps = 0;
        int output = 0;
        queue<int> q;
        for (int i = 0; i < nums.size(); ++i) {
            if (!q.empty() && i - 3 >= q.front()) {
                q.pop();
                --steps;
            }
            if (!((nums[i] + steps) % 2)) {
                if (i + 3 > nums.size()) return -1;
                ++steps;
                ++output;
                q.push(i);
            }
        }
        return output;
    }
};