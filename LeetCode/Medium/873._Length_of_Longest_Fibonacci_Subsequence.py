# A sequence x1, x2, ..., xn is Fibonacci-like if:
#
# n >= 3
# xi + xi+1 == xi+2 for all i + 2 <= n
# Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.
#
# A subsequence is derived from another sequence arr by deleting any number of elements (including none) from arr, without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].
#
#
#
# Example 1:
#
# Input: arr = [1,2,3,4,5,6,7,8]
# Output: 5
# Explanation: The longest subsequence that is fibonacci-like: [1,2,3,5,8].
# Example 2:
#
# Input: arr = [1,3,7,11,12,14,18]
# Output: 3
# Explanation: The longest subsequence that is fibonacci-like: [1,11,12], [3,11,14] or [7,11,18].
#
#
# Constraints:
#
# 3 <= arr.length <= 1000
# 1 <= arr[i] < arr[i + 1] <= 109
# Solution
# Python O(N**2LogM) O(N) Greedy Number Theory
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n: int = len(arr)
        seen: set[int] = set()
        seen.add(arr[0])
        seen.add(arr[1])
        dp: list[int] = [0] * n
        for i in range(2, n):
            for j in range(i - 1, -1, -1):
                a: int = arr[i]
                b: int = arr[j]
                c: int = a - b
                path: int = 0
                while c in seen:
                    if c >= b: break
                    if a == arr[i]: path += 3
                    else: path += 1
                    a = b
                    b = c
                    c = a - b
                dp[i] = max(dp[i], path)
            seen.add(arr[i])
        return max(dp)

# C++ O(N**2logM) O(N) Greedy Number Theory
class Solution {
public:
    int lenLongestFibSubseq(vector<int>& arr) {
        int n = arr.size();
        std::vector<int> dp (n, 0);
        std::unordered_set<int> seen = {arr[0], arr[1]};
        for (int i = 2; i < n; ++i) {
            for (int j = i - 1; j >= 0; --j) {
                int a = arr[i];
                int b = arr[j];
                int c = a - b;
                int path = 0;
                while (seen.count(c)) {
                    if (c >= b) break;
                    if (a == arr[i]) path += 3;
                    else path += 1;
                    a = b;
                    b = c;
                    c = a - b;
                }
                dp[i] = std::max(dp[i], path);

            }
            seen.insert(arr[i]);
        }
        int answer = 0;
        for (int& num : dp) answer = std::max(answer, num);
        return answer;
    }
};