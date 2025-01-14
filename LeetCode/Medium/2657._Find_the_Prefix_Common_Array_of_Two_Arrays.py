# You are given two 0-indexed integer permutations A and B of length n.
#
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
#
# Return the prefix common array of A and B.
#
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.
#
#
#
# Example 1:
#
# Input: A = [1,3,2,4], B = [3,1,2,4]
# Output: [0,2,3,4]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: 1 and 3 are common in A and B, so C[1] = 2.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
# At i = 3: 1, 2, 3, and 4 are common in A and B, so C[3] = 4.
# Example 2:
#
# Input: A = [2,3,1], B = [3,1,2]
# Output: [0,1,3]
# Explanation: At i = 0: no number is common, so C[0] = 0.
# At i = 1: only 3 is common in A and B, so C[1] = 1.
# At i = 2: 1, 2, and 3 are common in A and B, so C[2] = 3.
#
#
# Constraints:
#
# 1 <= A.length == B.length == n <= 50
# 1 <= A[i], B[i] <= n
# It is guaranteed that A and B are both a permutation of n integers.
# Solution O(N) O(N) Prefix Sum
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hsa: set = set()
        hsb: set = set()
        ans: list = []
        for i in range(len(A)):
            hsa.add(A[i])
            hsb.add(B[i])
            top: int = 0
            if A[i] != B[i]:
                if A[i] in hsb:
                    top += 1
                if B[i] in hsa:
                    top += 1
            else:
                top += 1
            if i > 0:
                top += ans[i-1]
            ans.append(top)
        return ans

# Python O(N) O(N) HashMap
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n: int = len(A)
        hashmap: list[int] = [0] * (n + 1)
        output: list[int] = [0] * n
        for i in range(n):
            hashmap[A[i]] += 1
            hashmap[B[i]] += 1
            if hashmap[A[i]] > 1: output[i] += 1
            if A[i] != B[i] and hashmap[B[i]] > 1: output[i] += 1
            if i: output[i] += output[i - 1]
        return output

# C++ O(N) O(N) HashMap
class Solution {
public:
    vector<int> findThePrefixCommonArray(vector<int>& A, vector<int>& B) {
        int n = A.size();
        std::vector<int> hashmap (n + 1, 0);
        std::vector<int> output (n, 0);
        for (int i = 0; i < n; ++i) {
            ++hashmap[A[i]];
            ++hashmap[B[i]];
            if (hashmap[A[i]] > 1) ++output[i];
            if (A[i] != B[i] && hashmap[B[i]] > 1) ++output[i];
            if (i) output[i] += output[i - 1];
        }
        return output;
    }
};