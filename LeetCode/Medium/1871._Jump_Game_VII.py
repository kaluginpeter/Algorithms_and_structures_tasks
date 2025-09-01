# You are given a 0-indexed binary string s and two integers minJump and maxJump. In the beginning, you are standing at index 0, which is equal to '0'. You can move from index i to index j if the following conditions are fulfilled:
#
# i + minJump <= j <= min(i + maxJump, s.length - 1), and
# s[j] == '0'.
# Return true if you can reach index s.length - 1 in s, or false otherwise.
#
#
#
# Example 1:
#
# Input: s = "011010", minJump = 2, maxJump = 3
# Output: true
# Explanation:
# In the first step, move from index 0 to index 3.
# In the second step, move from index 3 to index 5.
# Example 2:
#
# Input: s = "01101110", minJump = 2, maxJump = 3
# Output: false
#
#
# Constraints:
#
# 2 <= s.length <= 105
# s[i] is either '0' or '1'.
# s[0] == '0'
# 1 <= minJump <= maxJump < s.length
# Solution
# Python O(N) O(N) Deque DynamicProgramming
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n: int = len(s)
        data: list[int] = deque([0])
        for i in range(1, n):
            if s[i] == '1': continue
            while data and data[0] + maxJump < i: data.popleft()
            if not data: return False
            if data[0] + minJump <= i:
                if i == n - 1: return True
                data.append(i)
        return False

# C++ O(N) O(N) Deque DynamicProgramming
class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        size_t n = s.size();
        std::deque<size_t> data = {0};
        for (size_t i = 1; i < n; ++i) {
            if (s[i] == '1') continue;
            while (!data.empty() && (data.front() + maxJump < i)) data.pop_front();
            if (data.empty()) return false;
            else if (data.front() + minJump <= i) {
                data.push_back(i);
                if (i == n - 1) return true;
            }
        }
        return false;
    }
};