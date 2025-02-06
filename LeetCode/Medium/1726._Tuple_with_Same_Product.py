# Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.
#
#
#
# Example 1:
#
# Input: nums = [2,3,4,6]
# Output: 8
# Explanation: There are 8 valid tuples:
# (2,6,3,4) , (2,6,4,3) , (6,2,3,4) , (6,2,4,3)
# (3,4,2,6) , (4,3,2,6) , (3,4,6,2) , (4,3,6,2)
# Example 2:
#
# Input: nums = [1,2,4,5,10]
# Output: 16
# Explanation: There are 16 valid tuples:
# (1,10,2,5) , (1,10,5,2) , (10,1,2,5) , (10,1,5,2)
# (2,5,1,10) , (2,5,10,1) , (5,2,1,10) , (5,2,10,1)
# (2,10,4,5) , (2,10,5,4) , (10,2,4,5) , (10,2,5,4)
# (4,5,2,10) , (4,5,10,2) , (5,4,2,10) , (5,4,10,2)
#
#
# Constraints:
#
# 1 <= nums.length <= 1000
# 1 <= nums[i] <= 104
# All elements in nums are distinct.
# Solution
# Python O(N**2) O(N**2) HashMap
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap: dict[int, list[tuple[int, int]]] = dict()
        n: int = len(nums)
        for c in range(n):
            for d in range(n):
                if c == d: continue
                prod: int = nums[c] * nums[d]
                if prod not in hashmap: hashmap[prod] = []
                hashmap[prod].append([c, d])

        output: int = 0
        for a in range(n):
            for b in range(n):
                if a == b: continue
                prod: int = nums[a] * nums[b]
                for c, d in hashmap.get(prod, []):
                    if (a != c and a != d) and (b != c and b != d): output += 1
        return output

# C++ O(N**2) O(N**2) Hashmap
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> hashmap;
        int n = nums.size();
        for (int c = 0; c < n; ++c) {
            for (int d = 0; d < n; ++d) {
                if (c == d) continue;
                hashmap[nums[c] * nums[d]].push_back({c, d});
            }
        }
        int output = 0;
        for (int a = 0; a < n; ++a) {
            for (int b = 0; b < n; ++b) {
                if (a == b) continue;
                int prod = nums[a] * nums[b];
                for (std::pair<int, int>& p : hashmap[prod]) {
                    if ((a != p.first && a != p.second) && (b != p.first && b != p.second)) ++output;
                }
            }
        }
        return output;
    }
};

# Python O(N**2) O(N**2) Hashmap
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        n: int = len(nums)
        for c in range(n):
            for d in range(c + 1, n):
                prod: int = nums[c] * nums[d]
                hashmap[prod] = hashmap.get(prod, 0) + 1

        output: int = 0
        for _, freq in hashmap.items():
            if freq > 1: output += (freq - 1) * freq * 4
        return output

# C++ O(N**2) O(N**2) Hashmap
class Solution {
public:
    int tupleSameProduct(vector<int>& nums) {
        std::unordered_map<int, int> hashmap;
        int n = nums.size();
        for (int c = 0; c < n; ++c) {
            for (int d = c + 1; d < n; ++d) {
                ++hashmap[nums[c] * nums[d]];
            }
        }
        int output = 0;
        for (auto& p : hashmap) {
            if (p.second > 1) output += (p.second - 1) * p.second * 4;
        }
        return output;
    }
};