# Given an array arr of integers, check if there exist two indices i and j such that :
# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
#
# Example 1:
#
# Input: arr = [10,2,5,3]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:
#
# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.
#
# Constraints:
# 2 <= arr.length <= 500
# -103 <= arr[i] <= 103
# Solution
# Python O(N) O(N) HashMap
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hashmap: dict[int, int] = dict()
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        for num in hashmap:
            if num * 2 in hashmap:
                if num == 0 and hashmap[0] == 1:
                    continue
                return True
        return False

# C++ O(N) O(N) HashMap
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        std::unordered_map<int, int> hashmap;
        for (int num : arr) {
            ++hashmap[num];
        }
        for (int num : arr) {
            if (hashmap[num * 2]) {
                if (num == 0 && hashmap[num] == 1) {
                    continue;
                }
                return true;
            }
        }
        return false;
    }
};