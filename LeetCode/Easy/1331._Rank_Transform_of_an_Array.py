# Given an array of integers arr, replace each element with its rank.
#
# The rank represents how large the element is. The rank has the following rules:
#
# Rank is an integer starting from 1.
# The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
# Rank should be as small as possible.
#
#
# Example 1:
#
# Input: arr = [40,10,20,30]
# Output: [4,1,2,3]
# Explanation: 40 is the largest element. 10 is the smallest. 20 is the second smallest. 30 is the third smallest.
# Example 2:
#
# Input: arr = [100,100,100]
# Output: [1,1,1]
# Explanation: Same elements share the same rank.
# Example 3:
#
# Input: arr = [37,12,28,9,100,56,80,5,12]
# Output: [5,3,4,2,8,6,7,1,3]
#
#
# Constraints:
#
# 0 <= arr.length <= 105
# -109 <= arr[i] <= 109
# Solution
# Python O(NlogN) O(N) HashMap
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap: dict[int, set[int]] = dict()
        for idx in range(len(arr)):
            if arr[idx] not in hashmap:
                hashmap[arr[idx]] = set()
            hashmap[arr[idx]].add(idx)
        arr.sort()
        output: list[int] = [0] * len(arr)
        rank: int = 1
        for idx in range(len(arr) - 1):
            if arr[idx] != arr[idx + 1]:
                output[hashmap[arr[idx]].pop()] = rank
                rank += 1
            else:
                output[hashmap[arr[idx]].pop()] = rank
        if hashmap:
            output[hashmap[arr[-1]].pop()] = rank
        return output

# C++ O(NlogN) O(N) HashMap
class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        if (!arr.size()) {
            return arr;
        }
        std::unordered_map<int, std::unordered_set<size_t>> hashmap;
        for (size_t index = 0; index < arr.size(); ++index) {
            hashmap[arr[index]].insert(index);
        }
        std::sort(arr.begin(), arr.end());
        std::vector<int> output(arr.size());
        int rank = 1;
        for (size_t index = 0; index < arr.size() - 1; ++index) {
            if (arr[index] != arr[index + 1]) {
                output[*(popFromSet(hashmap, arr[index]))] = rank;
                rank += 1;
            } else {
                output[*(popFromSet(hashmap, arr[index]))] = rank;
            }
        }
        output[*(popFromSet(hashmap, arr[arr.size() - 1]))] = rank;
        return output;
    }
private:
std::optional<size_t> popFromSet(std::unordered_map<int, std::unordered_set<size_t>>& hashmap, int key) {
    auto it = hashmap.find(key);
    if (it != hashmap.end() && !it->second.empty()) {
        auto set_it = it->second.begin();
        size_t value = *set_it;
        it->second.erase(set_it);
        if (it->second.empty()) {
            hashmap.erase(it);
        }
        return value;
    }
    return std::nullopt;
}
};