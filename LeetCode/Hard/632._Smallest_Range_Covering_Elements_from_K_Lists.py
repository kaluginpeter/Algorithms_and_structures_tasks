# You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.
#
# We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.
#
#
#
# Example 1:
#
# Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
# Output: [20,24]
# Explanation:
# List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
# List 2: [0, 9, 12, 20], 20 is in range [20,24].
# List 3: [5, 18, 22, 30], 22 is in range [20,24].
# Example 2:
#
# Input: nums = [[1,2,3],[1,2,3],[1,2,3]]
# Output: [1,1]
#
#
# Constraints:
#
# nums.length == k
# 1 <= k <= 3500
# 1 <= nums[i].length <= 50
# -105 <= nums[i][j] <= 105
# nums[i] is sorted in non-decreasing order.
# Solution
# Python O(NlogN) O(N) Heap
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap: list[tuple[int, int, int, int]] = []
        current_max = float('-inf')
        ans: list[int, int] = [float('-inf'), float('inf')]
        for list_idx in range(len(nums)):
            heapq.heappush(heap, (nums[list_idx][0], list_idx, 0))
            current_max = max(current_max, nums[list_idx][0])
        while heap:
            current_min, list_index, element_index = heapq.heappop(heap)
            if current_max - current_min < ans[1] - ans[0]:
                ans = [current_min, current_max]
            if element_index + 1 >= len(nums[list_index]):
                break
            heapq.heappush(heap, (nums[list_index][element_index + 1], list_index, element_index + 1))
            current_max = max(current_max, nums[list_index][element_index + 1])
        return ans

# C++ O(NlogN) O(N) Heap
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        std::priority_queue<
        std::tuple<int, int, int>,
        std::vector<std::tuple<int, int, int>>,
        std::greater<std::tuple<int, int, int>>
        > heap;
        int current_max = -100000;
        for (int list_index = 0; list_index < nums.size(); ++list_index) {
            heap.push(std::make_tuple(nums[list_index][0], list_index, 0));
            current_max = std::max(current_max, nums[list_index][0]);
        }
        std::vector<int> answer = {-100000, 100000};
        while (heap.size()) {
            int current_min, list_index, element_index;
            std::tie(current_min, list_index, element_index) = heap.top();
            heap.pop();
            if (current_max - current_min < answer[1] - answer[0]) {
                answer[0] = current_min;
                answer[1] = current_max;
            }
            if (element_index + 1 >= nums[list_index].size()) {
                break;
            }
            heap.push(std::make_tuple(nums[list_index][element_index + 1], list_index, element_index + 1));
            current_max = std::max(current_max, nums[list_index][element_index + 1]);
        }
        return answer;
    }
};

# Python O(NlogN) O(N) Two Pointers
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        all_nums: list[tuple[int, int]] = []
        for list_index in range(len(nums)):
            for num in nums[list_index]:
                all_nums.append((num, list_index))
        all_nums.sort()
        ans: list[int, int] = [float('-inf'), float('inf')]
        left: int = 0
        hashmap: dict[int, int] = dict()
        for right in range(len(all_nums)):
            hashmap[all_nums[right][1]] = hashmap.get(all_nums[right][1], 0) + 1
            while len(hashmap) == len(nums):
                if all_nums[right][0] - all_nums[left][0] < ans[1] - ans[0]:
                    ans = [all_nums[left][0], all_nums[right][0]]
                hashmap[all_nums[left][1]] -= 1
                if hashmap[all_nums[left][1]] == 0:
                    del hashmap[all_nums[left][1]]
                left += 1
        return ans

# C++ O(NlogN) O(N) Two Pointers
class Solution {
public:
    vector<int> smallestRange(vector<vector<int>>& nums) {
        std::vector<std::tuple<int, int>> all_nums;
        for (int list_index = 0; list_index < nums.size(); ++list_index) {
            for (int num : nums[list_index]) {
                all_nums.push_back(std::make_tuple(num, list_index));
            }
        }
        std::sort(all_nums.begin(), all_nums.end());
        std::unordered_map<int, int> hashmap;
        std::vector<int> answer = {-100000, 100000};
        int left = 0;
        for (int right = 0; right < all_nums.size(); ++right) {
            ++hashmap[std::get<1>(all_nums[right])];
            while (hashmap.size() == nums.size()) {
                int current_start = std::get<0>(all_nums[left]);
                int current_end = std::get<0>(all_nums[right]);
                if (current_end - current_start < answer[1] - answer[0]) {
                    answer[0] = current_start;
                    answer[1] = current_end;
                }
                --hashmap[std::get<1>(all_nums[left])];
                if (!hashmap[std::get<1>(all_nums[left])]) {
                    hashmap.erase(std::get<1>(all_nums[left]));
                }
                ++left;
            }
        }
        return answer;
    }
};