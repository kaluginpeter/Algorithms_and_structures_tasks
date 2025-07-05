# Given an array of integers arr, a lucky integer is an integer that has a frequency in the array equal to its value.
# Return the largest lucky integer in the array. If there is no lucky integer return -1.
#
# Example 1:
#
# Input: arr = [2,2,3,4]
# Output: 2
# Explanation: The only lucky number in the array is 2 because frequency[2] == 2.
# Example 2:
#
# Input: arr = [1,2,2,3,3,3]
# Output: 3
# Explanation: 1, 2 and 3 are all lucky numbers, return the largest of them.
# Example 3:
#
# Input: arr = [2,2,2,3,3]
# Output: -1
# Explanation: There are no lucky numbers in the array.
#
# Constraints:
# 1 <= arr.length <= 500
# 1 <= arr[i] <= 500
# Solution
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        l = [i for i in arr if arr.count(i) == i]
        return max(l) if l else -1


# Python O(N + D) O(D) HashMap Counting
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap: list[int] = [0] * 501
        for num in arr: hashmap[num] += 1
        for i in range(500, 0, -1):
            if hashmap[i] == i: return i
        return -1

# C++ O(N + D) O(D) HashMap Counting
class Solution {
public:
    int findLucky(vector<int>& arr) {
        std::array<int, 501> hashmap = {};
        for (int &num : arr) ++hashmap[num];
        for (int i = 500; i > 0; --i) {
            if (hashmap[i] == i) return i;
        }
        return -1;
    }
};