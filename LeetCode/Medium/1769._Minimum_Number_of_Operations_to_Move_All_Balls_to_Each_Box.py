# You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.
#
# In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.
#
# Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.
#
# Each answer[i] is calculated considering the initial state of the boxes.
#
#
#
# Example 1:
#
# Input: boxes = "110"
# Output: [1,1,3]
# Explanation: The answer for each box is as follows:
# 1) First box: you will have to move one ball from the second box to the first box in one operation.
# 2) Second box: you will have to move one ball from the first box to the second box in one operation.
# 3) Third box: you will have to move one ball from the first box to the third box in two operations, and move one ball from the second box to the third box in one operation.
# Example 2:
#
# Input: boxes = "001011"
# Output: [11,8,5,4,3,4]
#
#
# Constraints:
#
# n == boxes.length
# 1 <= n <= 2000
# boxes[i] is either '0' or '1'.
# Solution Brute Force O(N**2) O(N)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n: int = len(boxes)
        ans: list[int] = [0] * n
        for i in range(n):
            for j in range(n):
                ans[i] += abs(i - j) if boxes[j] == '1' else 0
        return ans

# Solution Counting O(N) O(N)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n: int = len(boxes)
        ans: list[int] = [0] * n
        left_frq_ones, left_sm_ones = 0, 0
        for i in range(1, n):
            if boxes[i - 1] == '1':
                left_frq_ones += 1
            left_sm_ones += left_frq_ones
            ans[i] += left_sm_ones
        right_frq_ones, right_sm_ones = 0, 0
        for i in range(n - 2, -1, -1):
            if boxes[i + 1] == '1':
                right_frq_ones += 1
            right_sm_ones += right_frq_ones
            ans[i] += right_sm_ones
        return ans

# Solution
# Python O(N) O(N) Prefix Sum
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n: int = len(boxes)
        output: list[int] = [0] * n
        prev: int = 0
        ones: int = 0
        for i in range(n):
            output[i] += prev
            ones += boxes[i] == '1'
            prev += ones
        prev, ones = 0, 0
        for i in range(n - 1, -1, -1):
            output[i] += prev
            ones += boxes[i] == '1'
            prev += ones
        return output

# C++ O(N) O(N) Prefix Sum
class Solution {
public:
    vector<int> minOperations(string boxes) {
        int n = boxes.size();
        std::vector<int> output (n, 0);
        int prev = 0, ones = 0;
        for (int i = 0; i < n; ++i) {
            output[i] += prev;
            ones += (boxes[i] == '1'? 1 : 0);
            prev += ones;
        }
        prev = 0;
        ones = 0;
        for (int i = n - 1; i >= 0; --i) {
            output[i] += prev;
            ones += (boxes[i] == '1'? 1 : 0);
            prev = prev + ones;
        }
        return output;
    }
};