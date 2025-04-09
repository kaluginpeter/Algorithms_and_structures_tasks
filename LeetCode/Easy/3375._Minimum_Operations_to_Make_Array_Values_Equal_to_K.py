# You are given an integer array nums and an integer k.
#
# An integer h is called valid if all values in the array that are strictly greater than h are identical.
#
# For example, if nums = [10, 8, 10, 8], a valid integer is h = 9 because all nums[i] > 9 are equal to 10, but 5 is not a valid integer.
#
# You are allowed to perform the following operation on nums:
#
# Select an integer h that is valid for the current values in nums.
# For each index i where nums[i] > h, set nums[i] to h.
# Return the minimum number of operations required to make every element in nums equal to k. If it is impossible to make all elements equal to k, return -1.
#
#
#
# Example 1:
#
# Input: nums = [5,2,5,4,5], k = 2
#
# Output: 2
#
# Explanation:
#
# The operations can be performed in order using valid integers 4 and then 2.
#
# Example 2:
#
# Input: nums = [2,1,2], k = 2
#
# Output: -1
#
# Explanation:
#
# It is impossible to make all the values equal to 2.
#
# Example 3:
#
# Input: nums = [9,7,5,3], k = 1
#
# Output: 4
#
# Explanation:
#
# The operations can be performed using valid integers in the order 7, 5, 3, and 1.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 100
# 1 <= nums[i] <= 100
# 1 <= k <= 100
# Solution
# Python O(N) O(N) HashSet
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return len({num for num in nums if num > k}) if min(nums) >= k else -1

# C++ O(N) O(N) HashSet
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        std::unordered_set<int> hashset;
        int minValue = 101;
        for (int& num : nums) {
            if (num > k) {
                hashset.insert(num);
            }
            minValue = std::min(minValue, num);
        }
        return (minValue >= k? hashset.size() : -1);
    }
};

# Python O(NlogN) O(1) Sorting
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        if nums[0] < k: return -1
        prev: int = len(nums) - 1
        operations: int = int(nums[0] != k)
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] != nums[prev]:
                operations += 1
                prev = i
        return operations

# C++ O(NlogN) O(1) Sorting
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int prev = nums.size() - 1, operations = 0;
        if (nums[0] < k) return -1;
        for (int i = nums.size() - 2; i >= 0; --i) {
            if (nums[i] != nums[prev]) {
                ++operations;
                prev = i;
            }
        }
        if (nums[0] != k) ++operations;
        return operations;
    }
};

# Python O(N) O(D) HashMap
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        hashmap: dict[int, int] = dict()
        for num in nums:
            if num < k: return -1
            if num > k: hashmap[num] = hashmap.get(num, 0) + 1
        return len(hashmap)

# C++ O(N) O(D) HashMap
class Solution {
public:
    int minOperations(vector<int>& nums, int k) {
        unordered_map<int, int> hashmap;
        for (int& num : nums) {
            if (num < k) return -1;
            if (num > k) ++hashmap[num];
        }
        return hashmap.size();
    }
};