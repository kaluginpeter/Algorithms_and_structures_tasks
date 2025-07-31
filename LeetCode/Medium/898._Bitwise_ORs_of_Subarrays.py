# Given an integer array arr, return the number of distinct bitwise ORs of all the non-empty subarrays of arr.
#
# The bitwise OR of a subarray is the bitwise OR of each integer in the subarray. The bitwise OR of a subarray of one integer is that integer.
#
# A subarray is a contiguous non-empty sequence of elements within an array.
#
#
#
# Example 1:
#
# Input: arr = [0]
# Output: 1
# Explanation: There is only one possible result: 0.
# Example 2:
#
# Input: arr = [1,1,2]
# Output: 3
# Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
# These yield the results 1, 1, 2, 1, 3, 3.
# There are 3 unique values, so the answer is 3.
# Example 3:
#
# Input: arr = [1,2,4]
# Output: 6
# Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
#
#
# Constraints:
#
# 1 <= arr.length <= 5 * 104
# 0 <= arr[i] <= 109
# Solution
# Python O(NlogM) O(NlogM) BitManipulation
class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        subsets: set[int] = {0}
        output: set[int] = set()
        for num in arr:
            subsets = {or_ | num for or_ in subsets} | {num}
            output |= subsets
        return len(output)

# C++ O(NlogM) O(NlogM) BitManipulation
class Solution {
public:
    int subarrayBitwiseORs(vector<int>& arr) {
        std::unordered_set<int> seen = {0}, output;
        int n = arr.size();
        for (int i = 0; i < n; ++i) {
            std::unordered_set<int> newSubs;
            for (std::unordered_set<int>::const_iterator it = seen.cbegin(); it != seen.cend(); ++it) {
                newSubs.insert(*it | arr[i]);
            }
            newSubs.insert(arr[i]);
            seen = newSubs;
            for (auto &num : seen) output.insert(num);
        }
        return output.size();
    }
};