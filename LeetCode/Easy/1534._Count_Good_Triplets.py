# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.
#
# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:
#
# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.
#
# Return the number of good triplets.
#
#
#
# Example 1:
#
# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# Example 2:
#
# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.
#
#
# Constraints:
#
# 3 <= arr.length <= 100
# 0 <= arr[i] <= 1000
# 0 <= a, b, c <= 1000
# Solution Brute Force Amortized O(N**3) O(1)
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        ans: int = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j + 1, len(arr)):
                    if abs(arr[j] - arr[k]) > b:
                        continue
                    elif abs(arr[i]  - arr[k]) <= c:
                        ans += 1
        return ans

# Python O(N^3) O(1) BruteForce
class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        good: int = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                for k in range(j + 1, len(arr)):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        good += 1
        return good

# C++ O(N^3) O(1) BruteForce
class Solution {
public:
    int countGoodTriplets(vector<int>& arr, int a, int b, int c) {
        int good = 0;
        for (int i = 0; i < arr.size(); ++i) {
            for (int j = i + 1; j < arr.size(); ++j) {
                for (int k = j + 1; k < arr.size(); ++k) {
                    if (abs(arr[i] - arr[j]) <= a && abs(arr[j] - arr[k]) <= b && abs(arr[i] - arr[k]) <= c) {
                        ++good;
                    }
                }
            }
        }
        return good;
    }
};