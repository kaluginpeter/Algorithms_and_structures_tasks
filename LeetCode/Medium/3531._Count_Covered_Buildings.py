# You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
#
# A building is covered if there is at least one building in all four directions: left, right, above, and below.
#
# Return the number of covered buildings.
#
#
#
# Example 1:
#
#
#
# Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
#
# Output: 1
#
# Explanation:
#
# Only building [2,2] is covered as it has at least one building:
# above ([1,2])
# below ([3,2])
# left ([2,1])
# right ([2,3])
# Thus, the count of covered buildings is 1.
# Example 2:
#
#
#
# Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
#
# Output: 0
#
# Explanation:
#
# No building has at least one building in all four directions.
# Example 3:
#
#
#
# Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
#
# Output: 1
#
# Explanation:
#
# Only building [3,3] is covered as it has at least one building:
# above ([1,3])
# below ([5,3])
# left ([3,2])
# right ([3,5])
# Thus, the count of covered buildings is 1.
#
#
# Constraints:
#
# 2 <= n <= 105
# 1 <= buildings.length <= 105
# buildings[i] = [x, y]
# 1 <= x, y <= n
# All coordinates of buildings are unique.
# Solution
# Python O(NlogN + NlogM) O(N) HashMap BinarySearch Sorting
class Solution:
    def binary_search(self, nums: list[int], target: int) -> int:
        left: int = 0
        right: int = len(nums) - 1
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1
        return -1

    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        buildings.sort()
        x_axis: dict[int, int] = dict()
        y_axis: dict[int, int] = dict()
        for i in range(len(buildings)):
            b: list[int] = buildings[i]
            if b[0] not in x_axis:
                x_axis[b[0]] = []
            x_axis[b[0]].append(b[1])
            if b[1] not in y_axis:
                y_axis[b[1]] = []
            y_axis[b[1]].append(b[0])
        output: int = 0
        for i in range(len(buildings)):
            b: list[int] = buildings[i]
            if (
                    self.binary_search(x_axis[b[0]], b[1]) not in {0, len(x_axis[b[0]]) - 1}
                    and self.binary_search(y_axis[b[1]], b[0]) not in {0, len(y_axis[b[1]]) - 1}
            ):
                output += 1

        return output

# C++ O(NlogN + NlogM) O(N) BinarySearch Sorting HashMap
class Solution {
public:
    int binarySearch(int &target, vector<int> &nums) {
        int left = 0, right = nums.size() - 1;
        while (left <= right) {
            int middle = left + ((right - left) >> 1);
            if (nums[middle] == target) return middle;
            else if (nums[middle] > target) right = middle - 1;
            else left = middle + 1;
        }
        return -1;
    }

    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        std::sort(buildings.begin(), buildings.end());
        unordered_map<int, vector<int>> xAxis, yAxis;
        for (vector<int> &building : buildings) {
            xAxis[building[0]].push_back(building[1]);
            yAxis[building[1]].push_back(building[0]);
        }
        int output = 0;
        for (vector<int> &building : buildings) {
            int xBound = binarySearch(building[1], xAxis[building[0]]);
            if (!xBound || xBound == xAxis[building[0]].size() - 1) continue;
            int yBound = binarySearch(building[0], yAxis[building[1]]);
            if (!yBound || yBound == yAxis[building[1]].size() - 1) continue;
            ++output;
        }
        return output;
    }
};


# Python O(N) O(M) Math
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        y_axis: dict[int, tuple[int, int]] = dict()
        x_axis: dict[int, tuple[int, int]] = dict()
        for x, y in buildings:
            if x not in x_axis: x_axis[x] = (y, y)
            elif y < x_axis[x][0]: x_axis[x] = (y, x_axis[x][1])
            elif y > x_axis[x][1]: x_axis[x] = (x_axis[x][0], y)
            if y not in y_axis: y_axis[y] = (x, x)
            elif x < y_axis[y][0]: y_axis[y] = (x, y_axis[y][1])
            elif x > y_axis[y][1]: y_axis[y] = (y_axis[y][0], x)
        output: int = 0
        for x, y in buildings:
            if (y_axis[y][0] < x < y_axis[y][1]) and (x_axis[x][0] < y < x_axis[x][1]): output += 1
        return output

# C++ O(N) O(M) Math
class Solution {
public:
    int countCoveredBuildings(int n, vector<vector<int>>& buildings) {
        std::unordered_map<int, std::pair<int, int>> yAxis, xAxis;
        for (std::vector<int>& build : buildings) {
            if (!xAxis.count(build[0])) xAxis[build[0]] = {build[1], build[1]};
            else if (build[1] <= xAxis[build[0]].first) xAxis[build[0]].first = build[1];
            else if (build[1] > xAxis[build[0]].second) xAxis[build[0]].second = build[1];
            if (!yAxis.count(build[1])) yAxis[build[1]] = {build[0], build[0]};
            else if (build[0] <= yAxis[build[1]].first) yAxis[build[1]].first = build[0];
            else if (build[0] > yAxis[build[1]].second) yAxis[build[1]].second = build[0];
        }
        int output = 0;
        for (std::vector<int>& build : buildings) {
            bool horizontal = (build[1] > xAxis[build[0]].first) && (build[1] < xAxis[build[0]].second);
            bool vertical = (build[0] > yAxis[build[1]].first) && (build[0] < yAxis[build[1]].second);
            if (horizontal && vertical) ++output;
        }
        return output;
    }
};