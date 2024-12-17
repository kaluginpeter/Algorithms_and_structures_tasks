# You are given an integer array arr. You can choose a set of integers and remove all the occurrences of these integers in the array.
#
# Return the minimum size of the set so that at least half of the integers of the array are removed.
#
#
#
# Example 1:
#
# Input: arr = [3,3,3,3,5,5,5,2,2,7]
# Output: 2
# Explanation: Choosing {3,7} will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).
# Possible sets of size 2 are {3,5},{3,2},{5,2}.
# Choosing set {2,7} is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old array.
# Example 2:
#
# Input: arr = [7,7,7,7,7,7]
# Output: 1
# Explanation: The only possible set you can choose is {7}. This will make the new array empty.
#
#
# Constraints:
#
# 2 <= arr.length <= 105
# arr.length is even.
# 1 <= arr[i] <= 105
# Solution
# Python O(NlogN) O(N) Priority Queue
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        n: int = 0
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
            n += 1
        min_heap: list[tuple[int, int]] = []
        for num, freq in hashmap.items():
            heapq.heappush(min_heap, (-freq, num))
        removed: int = 0
        size: int = 0
        while removed < n / 2:
            removed += -heapq.heappop(min_heap)[0]
            size += 1
        return size

# C++ O(NlogN) O(N) Priority Queue
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        std::unordered_map<int, int> hashmap;
        int n = 0;
        for (int& num : arr) {
            ++hashmap[num];
            ++n;
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>> maxHeap;
        for (auto& pair : hashmap) {
            maxHeap.push({pair.second, pair.first});
        }
        int removed = 0;
        int size = 0;
        while (removed < n / 2) {
            ++size;
            removed += maxHeap.top().first;
            maxHeap.pop();
        }
        return size;
    }
};

# Python O(NlogN) O(N) Sorting Greedy
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        hashmap: dict[int, int] = dict()
        n: int = 0
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
            n += 1
        num_freq: list[tuple[int, int]] = sorted(hashmap.items(), key=lambda x: x[1])
        removed: int = 0
        size: int = 0
        while removed < n / 2:
            size += 1
            removed += num_freq.pop()[1]
        return size

# C++ O(NlogN) O(N) Sorting Greedy
class Solution {
public:
    int minSetSize(vector<int>& arr) {
        std::unordered_map<int, int> hashmap;
        int n = 0;
        for (int& num : arr) {
            ++hashmap[num];
            ++n;
        }
        std::vector<std::pair<int, int>> numFreq;
        for (auto& pair : hashmap) {
            numFreq.push_back({pair.second, pair.first});
        }
        std::sort(numFreq.begin(), numFreq.end());
        int removed = 0;
        int size = 0;
        while (removed < n / 2) {
            ++size;
            removed += numFreq[numFreq.size() - 1].first;
            numFreq.pop_back();
        }
        return size;
    }
};