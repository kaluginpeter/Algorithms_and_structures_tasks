# You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.
#
# To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.
#
# If k > 0, replace the ith number with the sum of the next k numbers.
# If k < 0, replace the ith number with the sum of the previous k numbers.
# If k == 0, replace the ith number with 0.
# As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].
#
# Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!
#
#
#
# Example 1:
#
# Input: code = [5,7,1,4], k = 3
# Output: [12,10,16,13]
# Explanation: Each number is replaced by the sum of the next 3 numbers. The decrypted code is [7+1+4, 1+4+5, 4+5+7, 5+7+1]. Notice that the numbers wrap around.
# Example 2:
#
# Input: code = [1,2,3,4], k = 0
# Output: [0,0,0,0]
# Explanation: When k is zero, the numbers are replaced by 0.
# Example 3:
#
# Input: code = [2,4,9,3], k = -2
# Output: [12,5,6,13]
# Explanation: The decrypted code is [3+9, 2+3, 4+2, 9+4]. Notice that the numbers wrap around again. If k is negative, the sum is of the previous numbers.
#
#
# Constraints:
#
# n == code.length
# 1 <= n <= 100
# 1 <= code[i] <= 100
# -(n - 1) <= k <= n - 1
# Solution
class Solution(object):
    def decrypt(self, code, k):
        if k == 0:
          return [0] * len(code)
        l, code = [], code * 2
        for i in range(len(code) // 2):
          if k > 0:
            l.append(sum(code[i + 1:i + k + 1]))
          else:
            x = i + len(code) // 2 - 1
            l.append(sum(code[x: x + k: -1]))
        return l


# Python O(N) O(N) Prefix Sum
class Solution:
    def get_remainder(self, idx: int, n: int, k: int, prefix: list[int], is_negative: bool) -> int:
        remainder: int = 0
        if is_negative:
            if idx - k >= 0:
                return prefix[idx - 1] - (prefix[idx - k - 1] if idx - k else 0)
            overhead_idx: int = k - idx
            return (prefix[idx - 1] if idx else 0) + (prefix[-1] - prefix[-overhead_idx - 1])
        else:
            if idx + k < n:
                return prefix[idx + k] - prefix[idx]
            overhead_idx: int = k - (n - idx)
            return (prefix[-1] - prefix[idx]) + prefix[overhead_idx]

    def decrypt(self, code: List[int], k: int) -> List[int]:
        n: int = len(code)
        output: list[int] = [0] * n
        if not k:
            return output
        prefix: list[int] = []
        for idx in range(n):
            if not idx:
                prefix.append(code[idx])
            else:
                prefix.append(code[idx] + prefix[-1])
        wholes: int = abs(k) // n * prefix[-1]
        is_negative: bool = k < 0
        k = abs(k) % n
        for idx in range(n):
            remainder: int = self.get_remainder(idx, n, k, prefix, is_negative)
            output[idx] = wholes + remainder
        return output

# C++ O(N) O(N) Prefix Sum
class Solution {
public:
    int getRemainder(int idx, int n, int k, std::vector<int>& prefix, bool isNegative) {
        int remainder = 0;
        if (isNegative) {
            if (idx - k >= 0) {
                return prefix[idx - 1] - (idx - k? prefix[idx - k - 1] : 0);
            }
            int overheadIdx = n - (k - idx);
            return (idx? prefix[idx - 1] : 0) + (prefix[n - 1] - prefix[overheadIdx - 1]);
        } else {
            if (idx + k < n) {
                return prefix[idx + k] - prefix[idx];
            }
            int overheadIdx = k - (n - idx);
            return (prefix[n - 1] - prefix[idx]) + prefix[overheadIdx];
        }
        return remainder;
    }
    vector<int> decrypt(vector<int>& code, int k) {
        int n = code.size();
        std::vector<int> output(n, 0);
        if (!k) {
            return output;
        }
        std::vector<int> prefix;
        for (int idx = 0; idx < n; ++idx) {
            if (!idx) {
                prefix.push_back(code[idx]);
            } else {
                prefix.push_back(code[idx] + prefix[prefix.size() - 1]);
            }
        }
        int wholes = std::abs(k) / n * prefix[n - 1];
        bool isNegative = k < 0;
        k = std::abs(k) % n;
        for (int idx = 0; idx < n; ++idx) {
            int remainder = getRemainder(idx, n, k, prefix, isNegative);
            output[idx] = wholes + remainder;
        }
        return output;
    }
};