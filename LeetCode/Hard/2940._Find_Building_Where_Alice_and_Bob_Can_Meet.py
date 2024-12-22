# You are given a 0-indexed array heights of positive integers, where heights[i] represents the height of the ith building.
#
# If a person is in building i, they can move to any other building j if and only if i < j and heights[i] < heights[j].
#
# You are also given another array queries where queries[i] = [ai, bi]. On the ith query, Alice is in building ai while Bob is in building bi.
#
# Return an array ans where ans[i] is the index of the leftmost building where Alice and Bob can meet on the ith query. If Alice and Bob cannot move to a common building on query i, set ans[i] to -1.
#
#
#
# Example 1:
#
# Input: heights = [6,4,8,5,2,7], queries = [[0,1],[0,3],[2,4],[3,4],[2,2]]
# Output: [2,5,-1,5,2]
# Explanation: In the first query, Alice and Bob can move to building 2 since heights[0] < heights[2] and heights[1] < heights[2].
# In the second query, Alice and Bob can move to building 5 since heights[0] < heights[5] and heights[3] < heights[5].
# In the third query, Alice cannot meet Bob since Alice cannot move to any other building.
# In the fourth query, Alice and Bob can move to building 5 since heights[3] < heights[5] and heights[4] < heights[5].
# In the fifth query, Alice and Bob are already in the same building.
# For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
# For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
# Example 2:
#
# Input: heights = [5,3,8,2,6,1,4,6], queries = [[0,7],[3,5],[5,2],[3,0],[1,6]]
# Output: [7,6,-1,4,6]
# Explanation: In the first query, Alice can directly move to Bob's building since heights[0] < heights[7].
# In the second query, Alice and Bob can move to building 6 since heights[3] < heights[6] and heights[5] < heights[6].
# In the third query, Alice cannot meet Bob since Bob cannot move to any other building.
# In the fourth query, Alice and Bob can move to building 4 since heights[3] < heights[4] and heights[0] < heights[4].
# In the fifth query, Alice can directly move to Bob's building since heights[1] < heights[6].
# For ans[i] != -1, It can be shown that ans[i] is the leftmost building where Alice and Bob can meet.
# For ans[i] == -1, It can be shown that there is no building where Alice and Bob can meet.
#
#
#
# Constraints:
#
# 1 <= heights.length <= 5 * 104
# 1 <= heights[i] <= 109
# 1 <= queries.length <= 5 * 104
# queries[i] = [ai, bi]
# 0 <= ai, bi <= heights.length - 1
# Solution
# Python O(MlogM + NlogM) O(M), where M is the length of queries and N is length of heights. Priority Queue
class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        n: int = len(queries)
        output: list[int] = [-1] * n
        bucket: dict[int, list[tuple[int, int]]] = dict()
        for idx in range(n):
            a, b = queries[idx]
            if a > b:
                a, b = b, a
            if a == b or heights[a] < heights[b]:
                output[idx] = b
                continue
            elif b not in bucket:
                bucket[b] = list()
            bucket[b].append((max(heights[a], heights[b]), idx))

        min_heap: list[tuple[int, int]] = []
        for idx in range(len(heights)):
            for pair in bucket.get(idx, []):
                heapq.heappush(min_heap, pair)
            while min_heap and heights[idx] > min_heap[0][0]:
                output[heapq.heappop(min_heap)[1]] = idx
        return output

# C++ O(MlogM + NlogM) O(M), where M is the length of queries and N is length of heights. Priority Queue
class Solution {
public:
    vector<int> leftmostBuildingQueries(vector<int>& heights, vector<vector<int>>& queries) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> bucket;
        std::vector<int> output(queries.size(), -1);
        for (int idx = 0; idx < queries.size(); ++idx) {
            int a = queries[idx][0], b = queries[idx][1];
            if (a > b) {
                int c = b;
                b = a;
                a = c;
            }
            if (a == b || heights[a] < heights[b]) {
                output[idx] = b;
            } else {
                bucket[b].push_back(
                    {std::max(heights[a], heights[b]), idx}
                );
            }
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        for (int idx = 0; idx < heights.size(); ++idx) {
            for (std::pair<int, int>& p : bucket[idx]) {
                minHeap.push(p);
            }
            while (minHeap.size() && heights[idx] > minHeap.top().first) {
                output[minHeap.top().second] = idx;
                minHeap.pop();
            }
        }
        return output;
    }
};