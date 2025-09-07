# Given an integer n, return any array containing n unique integers such that they add up to 0.
#
#
#
# Example 1:
#
# Input: n = 5
# Output: [-7,-1,1,3,4]
# Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
# Example 2:
#
# Input: n = 3
# Output: [-1,0,1]
# Example 3:
#
# Input: n = 1
# Output: [0]
#
#
# Constraints:
#
# 1 <= n <= 1000
#
# Solution
# Python O(N) O(N) Math
class Solution:
    def sumZero(self, n: int) -> List[int]:
        output: list[int] = []
        if n & 1: output.append(0)
        i: int = 1
        while len(output) < n:
            output.append(-i)
            output.append(i)
            i += 1
        return output

# C++ O(N) O(N) Math
class Solution {
public:
    vector<int> sumZero(int n) {
        std::vector<int> output;
        if (n & 1) output.push_back(0);
        int i = 1;
        while (output.size() < n) {
            output.push_back(-i);
            output.push_back(i);
            ++i;
        }
        return output;
    }
};