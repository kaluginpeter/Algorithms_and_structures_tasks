# You are given a 0-indexed array of n integers arr.
#
# The interval between two elements in arr is defined as the absolute difference between their indices. More formally, the interval between arr[i] and arr[j] is |i - j|.
#
# Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and each element in arr with the same value as arr[i].
#
# Note: |x| is the absolute value of x.
#
#
#
# Example 1:
#
# Input: arr = [2,1,3,1,2,3,3]
# Output: [4,2,7,2,4,4,5]
# Explanation:
# - Index 0: Another 2 is found at index 4. |0 - 4| = 4
# - Index 1: Another 1 is found at index 3. |1 - 3| = 2
# - Index 2: Two more 3s are found at indices 5 and 6. |2 - 5| + |2 - 6| = 7
# - Index 3: Another 1 is found at index 1. |3 - 1| = 2
# - Index 4: Another 2 is found at index 0. |4 - 0| = 4
# - Index 5: Two more 3s are found at indices 2 and 6. |5 - 2| + |5 - 6| = 4
# - Index 6: Two more 3s are found at indices 2 and 5. |6 - 2| + |6 - 5| = 5
# Example 2:
#
# Input: arr = [10,5,10,10]
# Output: [5,0,3,4]
# Explanation:
# - Index 0: Two more 10s are found at indices 2 and 3. |0 - 2| + |0 - 3| = 5
# - Index 1: There is only one 5 in the array, so its sum of intervals to identical elements is 0.
# - Index 2: Two more 10s are found at indices 0 and 3. |2 - 0| + |2 - 3| = 3
# - Index 3: Two more 10s are found at indices 0 and 2. |3 - 0| + |3 - 2| = 4
#
#
# Constraints:
#
# n == arr.length
# 1 <= n <= 105
# 1 <= arr[i] <= 105
#
#
# Note: This question is the same as 2615: Sum of Distances.
# Solution
# Python O(N) O(N) PrefixSum
class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        left: dict[int, list[int]] = dict()
        right: dist[int, list[int]] = dict()
        n: int = len(arr)
        for i in range(n - 1, -1, -1):
            if arr[i] not in right: right[arr[i]] = [0, 0]
            right[arr[i]][0] += i
            right[arr[i]][1] += 1
        output: list[int] = [0] * n
        for i in range(n):
            right[arr[i]][0] -= i
            right[arr[i]][1] -= 1
            if arr[i] not in left: left[arr[i]] = [0, 0]
            output[i] = (i * left[arr[i]][1] - left[arr[i]][0]) + (right[arr[i]][0] - i * right[arr[i]][1])
            left[arr[i]][0] += i
            left[arr[i]][1] += 1
        return output

# C++ O(N) O(N) PrefixSum
class Solution {
public:
    vector<long long> getDistances(vector<int>& arr) {
        std::unordered_map<int, std::pair<long long, int>> left, right;
        size_t n = arr.size();
        for (size_t i = n; i > 0; --i) {
            right[arr[i - 1]].first += i - 1;
            ++right[arr[i - 1]].second;
        }
        std::vector<long long> output(n, 0LL);
        for (size_t i = 0; i < n; ++i) {
            right[arr[i]].first -= i;
            --right[arr[i]].second;
            output[i] = (i * left[arr[i]].second - left[arr[i]].first) + (right[arr[i]].first - i * right[arr[i]].second);
            left[arr[i]].first += i;
            ++left[arr[i]].second;
        }
        return output;
    }
};