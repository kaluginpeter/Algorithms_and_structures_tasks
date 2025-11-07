# You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.
#
# Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.
#
# Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
# The power of a city is the total number of power stations it is being provided power from.
#
# The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.
#
# Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.
#
# Note that you can build the k power stations in multiple cities.
#
#
#
# Example 1:
#
# Input: stations = [1,2,4,5,0], r = 1, k = 2
# Output: 5
# Explanation:
# One of the optimal ways is to install both the power stations at city 1.
# So stations will become [1,4,4,5,0].
# - City 0 is provided by 1 + 4 = 5 power stations.
# - City 1 is provided by 1 + 4 + 4 = 9 power stations.
# - City 2 is provided by 4 + 4 + 5 = 13 power stations.
# - City 3 is provided by 5 + 4 = 9 power stations.
# - City 4 is provided by 5 + 0 = 5 power stations.
# So the minimum power of a city is 5.
# Since it is not possible to obtain a larger power, we return 5.
# Example 2:
#
# Input: stations = [4,4,4,4], r = 0, k = 3
# Output: 4
# Explanation:
# It can be proved that we cannot make the minimum power of a city greater than 4.
#
#
# Constraints:
#
# n == stations.length
# 1 <= n <= 105
# 0 <= stations[i] <= 105
# 0 <= r <= n - 1
# 0 <= k <= 109
# Solution
# Python O(N + NlogM) O(N) BinarySearch Greedy
class Solution:
    def check(self, bound: int, windows: list[int], r: int, k: int) -> bool:
        used: int = 0
        addition: int = 0
        seen: list[tuple[int, int]] = deque()
        for i in range(len(windows)):
            while seen and seen[0][0] < i:
                addition -= seen.popleft()[1]
            needed: int = bound - (windows[i] + addition)
            if needed <= 0: continue
            if used + needed > k: return False
            addition += needed
            used += needed
            seen.append((i + r + r, needed))
        return True

    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        windows: list[int] = []
        window: int = 0
        left: int = 0
        right: int = 0
        bound: int = float('inf')
        for i in range(len(stations)):
            while left + r < i:
                window -= stations[left]
                left += 1
            while i + r >= right and right < len(stations):
                window += stations[right]
                right += 1
            windows.append(window)
            bound = min(bound, window)
        left = 0
        right = bound + k
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.check(middle, windows, r, k): left = middle + 1
            else: right = middle - 1
        return right

# C++ O(N + NlogM) O(N) BinarySearch Greedy
class Solution {
public:
    bool check(long long& bound, std::vector<long long>& windows, int& r, int& k) {
        long long used = 0;
        std::deque<std::pair<int, int>> extra;
        long long addition = 0;
        for (size_t i = 0; i < windows.size(); ++i) {
            while (!extra.empty() && extra.front().first < i) {
                addition -= extra.front().second;
                extra.pop_front();
            }
            long long needed = bound - (windows[i] + addition);
            if (needed <= 0) continue;
            if (used + needed > k) return false;
            used += needed;
            extra.push_back({i + r + r, needed});
            addition += needed;
        }
        return true;
    }
    long long maxPower(vector<int>& stations, int r, int k) {
        std::vector<long long> windows;
        long long window = 0;
        size_t L = 0, R = 0;
        for (size_t i = 0; i < stations.size(); ++i) {
            while (L + r < i) {
                window -= stations[L];
                ++L;
            }
            while (i + r >= R && R < stations.size()) {
                window += stations[R];
                ++R;
            }
            windows.push_back(window);
        }
        long long left = 0LL, right = 1e11;
        while (left <= right) {
            long long middle = left + ((right - left) >> 1);
            if (check(middle, windows, r, k)) left = middle + 1;
            else right = middle - 1;
        }
        return right;
    }
};