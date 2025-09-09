# You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).
#
# The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.
#
# There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road goes in one direction from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.
#
# Return the minimum cost required to go from (startX, startY) to (targetX, targetY).
#
#
#
# Example 1:
#
# Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
#
# Output: 5
#
# Explanation:
#
# (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
# (1,2) to (3,3). Use specialRoads[0] with the cost 2.
# (3,3) to (3,4) with a cost of |3 - 3| + |4 - 3| = 1.
# (3,4) to (4,5). Use specialRoads[1] with the cost 1.
# So the total cost is 1 + 2 + 1 + 1 = 5.
#
# Example 2:
#
# Input: start = [3,2], target = [5,7], specialRoads = [[5,7,3,2,1],[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
#
# Output: 7
#
# Explanation:
#
# It is optimal not to use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.
#
# Note that the specialRoads[0] is directed from (5,7) to (3,2).
#
# Example 3:
#
# Input: start = [1,1], target = [10,4], specialRoads = [[4,2,1,1,3],[1,2,7,4,4],[10,3,6,1,2],[6,1,1,2,3]]
#
# Output: 8
#
# Explanation:
#
# (1,1) to (1,2) with a cost of |1 - 1| + |2 - 1| = 1.
# (1,2) to (7,4). Use specialRoads[1] with the cost 4.
# (7,4) to (10,4) with a cost of |10 - 7| + |4 - 4| = 3.
#
#
# Constraints:
#
# start.length == target.length == 2
# 1 <= startX <= targetX <= 105
# 1 <= startY <= targetY <= 105
# 1 <= specialRoads.length <= 200
# specialRoads[i].length == 5
# startX <= x1i, x2i <= targetX
# startY <= y1i, y2i <= targetY
# 1 <= costi <= 105
# Solution
# Python O(N^2logN) O(N^2) PriorityQueue
class Solution:
    def get_distance(self, x1: int, y1: int, x2: int, y2: int) -> int:
        return abs(x2 - x1) + abs(y2 - y1)

    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        output: int = self.get_distance(start[0], start[1], target[0], target[1])
        seen: dict[tuple[int, int], int] = dict()
        seen[(start[0], start[1])] = 0
        min_heap: list[tuple[int, int, int]] = []
        for path in specialRoads:
            dist: int = self.get_distance(start[0], start[1], path[0], path[1]) + path[4]
            seen[(path[2], path[3])] = min(seen.get((path[2], path[3]), float('inf')), dist)
            heapq.heappush(min_heap, (dist, path[2], path[3]))
        while min_heap:
            cost, x, y = heapq.heappop(min_heap)
            output = min(output, cost + self.get_distance(x, y, target[0], target[1]))
            for sx, sy, ex, ey, c in specialRoads:
                dist: int = cost + self.get_distance(x, y, sx, sy) + c
                if (ex, ey) not in seen or seen[(ex, ey)] > dist:
                    seen[(ex, ey)] = dist
                    heapq.heappush(min_heap, (dist, ex, ey))
        return output

# C++ O(N^2logN) O(N^2) PriorityQueue Graph
using tiii = std::tuple<int, int, int>;
struct pair_hash {
    size_t operator()(const pair<int, int>& p) const {
        return hash<long long>()(((long long)p.first << 32) ^ p.second);
    }
};
class Solution {
public:
    int getDistance(const int &x1, const int &y1, const int &x2, const int &y2) {
        return std::abs(x2 - x1) + std::abs(y2 - y1);
    }

    int minimumCost(vector<int>& start, vector<int>& target, vector<vector<int>>& specialRoads) {
        size_t n = specialRoads.size();
        int output = getDistance(start[0], start[1], target[0], target[1]);
        std::priority_queue<tiii, std::vector<tiii>, std::greater<tiii>> minHeap;
        std::unordered_map<std::pair<int, int>, int, pair_hash> seen;
        seen[std::pair<int, int>(start[0], start[1])] = 0;
        for (size_t i = 0; i < n; ++i) {
            int dist = getDistance(start[0], start[1], specialRoads[i][0], specialRoads[i][1]) + specialRoads[i][4];
            std::pair<int, int> ceil = {specialRoads[i][2], specialRoads[i][3]};
            if (!seen.count(ceil) || seen[ceil] > dist) {
                seen[ceil] = dist;
                minHeap.push(std::make_tuple(dist, specialRoads[i][2], specialRoads[i][3]));
            }
        }
        while (!minHeap.empty()) {
            tiii cur = minHeap.top();
            minHeap.pop();
            output = std::min(output, std::get<0>(cur) + getDistance(std::get<1>(cur), std::get<2>(cur), target[0], target[1]));
            for (const auto &p : specialRoads) {
                int dist = std::get<0>(cur) + getDistance(std::get<1>(cur), std::get<2>(cur), p[0], p[1]) + p[4];
                std::pair<int, int> nextMove = {p[2], p[3]};
                if (!seen.count(nextMove) || seen[nextMove] > dist) {
                    seen[nextMove] = dist;
                    minHeap.push(std::make_tuple(dist, p[2], p[3]));
                }
            }
        }
        return output;
    }
};