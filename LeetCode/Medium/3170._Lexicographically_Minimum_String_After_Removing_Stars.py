# You are given a string s. It may contain any number of '*' characters. Your task is to remove all '*' characters.
#
# While there is a '*', do the following operation:
#
# Delete the leftmost '*' and the smallest non-'*' character to its left. If there are several smallest characters, you can delete any of them.
# Return the
# lexicographically smallest
#  resulting string after removing all '*' characters.
#
#
#
# Example 1:
#
# Input: s = "aaba*"
#
# Output: "aab"
#
# Explanation:
#
# We should delete one of the 'a' characters with '*'. If we choose s[3], s becomes the lexicographically smallest.
#
# Example 2:
#
# Input: s = "abc"
#
# Output: "abc"
#
# Explanation:
#
# There is no '*' in the string.
#
#
#
# Constraints:
#
# 1 <= s.length <= 105
# s consists only of lowercase English letters and '*'.
# The input is generated such that it is possible to delete all '*' characters.
# Solution Heap O(NlogN) O(N)
import heapq
class Solution:
    def clearStars(self, s: str) -> str:
        heap = list()
        for i in range(len(s)):
            if s[i] == '*':
                 heapq.heappop(heap)
            else:
                heapq.heappush(heap, (s[i], -i))
        heap.sort(key=lambda x: -x[1])
        return ''.join(i[0] for i in heap)


# Python O(DN + NlogN) O(D + N) HashMap Stack PriorityQueue
class Solution:
    def clearStars(self, s: str) -> str:
        n: int = len(s)
        hashmap: list[list[int]] = [[] for _ in range(26)]
        for i in range(n):
            if s[i] != '*': hashmap[ord(s[i]) - 97].append(i)
            else:
                for j in range(26):
                    if hashmap[j]:
                        hashmap[j].pop()
                        break
        min_heap: list[int] = []
        for i in range(26):
            while hashmap[i]: heapq.heappush(min_heap, hashmap[i].pop())
        output: list[str] = []
        while min_heap:
            output.append(s[heapq.heappop(min_heap)])
        return ''.join(output)

# C++ O(DN + NlogN) O(D + N) HashMap Stack PriorityQueue
class Solution {
public:
    string clearStars(string s) {
        vector<vector<int>> hashmap(26, vector<int>());
        int n = s.size();
        for (int i = 0; i < n; ++i) {
            if (s[i] != '*') hashmap[s[i] - 'a'].push_back(i);
            else {
                for (int j = 0; j < 26; ++j) {
                    if (!hashmap[j].empty()) {
                        hashmap[j].pop_back();
                        break;
                    }
                }
            }
        }
        priority_queue<int> minHeap;
        for (int i = 0; i < 26; ++i) {
            while (!hashmap[i].empty()) {
                minHeap.push(-hashmap[i].back());
                hashmap[i].pop_back();
            }
        }
        string output = "";
        while (!minHeap.empty()) {
            output.push_back(s[-minHeap.top()]);
            minHeap.pop();
        }
        return output;
    }
};