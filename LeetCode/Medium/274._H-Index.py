# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
#
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
#
#
#
# Example 1:
#
# Input: citations = [3,0,6,1,5]
# Output: 3
# Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
# Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
# Example 2:
#
# Input: citations = [1,3,1]
# Output: 1
#
#
# Constraints:
#
# n == citations.length
# 1 <= n <= 5000
# 0 <= citations[i] <= 1000
# Solution 1 O(N * N) == O(N**2)
class Solution(object):
    def hIndex(self, citations):
        h, count = 0, 0
        while True:
            for i in citations:
                if i >= h + 1:
                    count += 1
            if count >= h + 1:
                h += 1
                count = 0
            else:
                break
        return h
# Solution 2 O(N log N)
class Solution(object):
    def hIndex(self, citations):
        citations.sort()
        for i in range(1, len(citations) + 1):
            if citations[-i] < i:
                return i - 1
        return len(citations)
# Solution 3 O(N)
class Solution(object):
    def hIndex(self, citations):
        cop, n = [0] * (len(citations) + 1), len(citations)
        for num in citations:
            if num >= n:
                cop[n] += 1
            else:
                cop[num] += 1
        pos = 0
        for i in range(n + 1):
            for j in range(cop[i]):
                citations[pos] = i
                pos += 1
        for i in range(1, n+1):
            if citations[-i] < i:
                return i - 1
        return n