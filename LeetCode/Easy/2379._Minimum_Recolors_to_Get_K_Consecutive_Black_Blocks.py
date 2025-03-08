# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.
#
#
#
# Example 1:
#
# Input: blocks = "WBBWWBBWBW", k = 7
# Output: 3
# Explanation:
# One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
# so that blocks = "BBBBBBBWBW".
# It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
# Therefore, we return 3.
# Example 2:
#
# Input: blocks = "WBWBBBW", k = 2
# Output: 0
# Explanation:
# No changes need to be made, since 2 consecutive black blocks already exist.
# Therefore, we return 0.
#
#
# Constraints:
#
# n == blocks.length
# 1 <= n <= 100
# blocks[i] is either 'W' or 'B'.
# 1 <= k <= n
# Solution
# Python O(N) O(1) Sliding Window
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = black = 0
        left: int = 0
        for right in range(k):
            if blocks[right] == 'W': white += 1
            else: black += 1
        needed: int = white
        for right in range(k, len(blocks)):
            if blocks[right] == 'W': white += 1
            else: black += 1
            if blocks[left] == 'W': white -= 1
            else: black -= 1
            if white < needed: needed = white
            left += 1
        return needed

# C++ O(N) O(1) Sliding Window
class Solution {
public:
    int minimumRecolors(string blocks, int k) {
        int left = 0;
        int black = 0;
        int white = 0;
        for (int right = 0; right < k; ++right) {
            if (blocks[right] == 'W') ++white;
            else ++black;
        }
        int needed = white;
        for (int right = k; right < blocks.size(); ++right) {
            if (blocks[right] == 'W') ++white;
            else ++black;
            if (blocks[left] == 'W') --white;
            else --black;
            if (white < needed) needed = white;
            ++left;
        }
        return needed;
    }
};