v
# Python O(NlogN) O(N) Sorting Greedy
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        output: list[int] = sorted(nums)
        groups: list[list[int]] = []
        hashmap: dict[int, int] = dict()
        for num in output:
            if not groups:
                groups.append(deque([num]))
            elif num - groups[-1][-1] <= limit:
                groups[-1].append(num)
            else:
                groups.append(deque([num]))
            hashmap[num] = len(groups) - 1
        for idx in range(len(nums)):
            output[idx] = groups[hashmap[nums[idx]]].popleft()
        return output

# C++ O(NlogN) O(N) Greedy
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        std::vector<int> output = nums;
        std::sort(output.begin(), output.end());
        std::vector<std::queue<int>> groups;
        std::unordered_map<int, int> hashmap;
        for (int& num : output) {
            if (groups.empty()) {
                std::queue<int> newGroup;
                newGroup.push(num);
                groups.push_back(newGroup);
            } else if (num - groups[groups.size() - 1].back() <= limit) {
                groups[groups.size() - 1].push(num);
            } else {
                std::queue<int> newGroup;
                newGroup.push(num);
                groups.push_back(newGroup);
            }
            hashmap[num] = groups.size() - 1;
        }
        for (int idx = 0; idx < nums.size(); ++idx) {
            output[idx] = groups[hashmap[nums[idx]]].front();
            groups[hashmap[nums[idx]]].pop();
        }
        return output;
    }
};

# C++ O(NlogN) O(N) HashMap SlidingWindow Sorting
class Solution {
public:
    vector<int> lexicographicallySmallestArray(vector<int>& nums, int limit) {
        size_t n = nums.size();
        std::unordered_map<int, std::vector<size_t>> seen;
        for (size_t i = 0; i < n; ++i) {
            seen[nums[i]].push_back(i);
        }
        std::sort(nums.begin(), nums.end());
        std::vector<int> output(n, 0);
        size_t left = 0;
        std::vector<size_t> sequence;
        for (size_t right = 0; right < n; ++right) {
            if (right && (nums[right - 1] == nums[right])) continue;
            if (nums[right] - nums[(right ? right - 1 : right)] > limit) {
                std::sort(sequence.begin(), sequence.end());
                for (size_t& i : sequence) output[i] = nums[left++];
                sequence.clear();
            }
            for (size_t& ptr : seen[nums[right]]) {
                sequence.push_back(ptr);
            }
        }
        std::sort(sequence.begin(), sequence.end());
        for (size_t& i : sequence) output[i] = nums[left++];
        sequence.clear();
        return output;
    }
};