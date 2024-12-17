# You are given a string s and an integer repeatLimit. Construct a new string repeatLimitedString using the characters of s such that no letter appears more than repeatLimit times in a row. You do not have to use all characters from s.
#
# Return the lexicographically largest repeatLimitedString possible.
#
# A string a is lexicographically larger than a string b if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b. If the first min(a.length, b.length) characters do not differ, then the longer string is the lexicographically larger one.
#
#
#
# Example 1:
#
# Input: s = "cczazcc", repeatLimit = 3
# Output: "zzcccac"
# Explanation: We use all of the characters from s to construct the repeatLimitedString "zzcccac".
# The letter 'a' appears at most 1 time in a row.
# The letter 'c' appears at most 3 times in a row.
# The letter 'z' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we return "zzcccac".
# Note that the string "zzcccca" is lexicographically larger but the letter 'c' appears more than 3 times in a row, so it is not a valid repeatLimitedString.
# Example 2:
#
# Input: s = "aababab", repeatLimit = 2
# Output: "bbabaa"
# Explanation: We use only some of the characters from s to construct the repeatLimitedString "bbabaa".
# The letter 'a' appears at most 2 times in a row.
# The letter 'b' appears at most 2 times in a row.
# Hence, no letter appears more than repeatLimit times in a row and the string is a valid repeatLimitedString.
# The string is the lexicographically largest repeatLimitedString possible so we return "bbabaa".
# Note that the string "bbabaaa" is lexicographically larger but the letter 'a' appears more than 2 times in a row, so it is not a valid repeatLimitedString.
#
#
# Constraints:
#
# 1 <= repeatLimit <= s.length <= 105
# s consists of lowercase English letters.
# Solution
# Python O(NlogK) O(K) Priority Queue Sorting
class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        output: list[str] = []
        chunks: list[int] = [0] * 26
        for ch in s:
            chunks[ord(ch) - 97] += 1
        min_heap: list[tuple[int, int]] = []
        for idx in range(26):
            if chunks[idx]:
                heapq.heappush(min_heap, (-idx, chunks[idx]))
        prev_amount: int = 0
        while min_heap:
            idx, count = heapq.heappop(min_heap)
            if output and -idx != ord(output[-1]) - 97:
                prev_amount = 0
            if count >= repeatLimit - prev_amount:
                output.extend(chr(-idx + 97) for _ in range(repeatLimit - prev_amount))
                if not min_heap:
                    break
                else:
                    separator_idx, separator_count = heapq.heappop(min_heap)
                    output.append(chr(-separator_idx + 97))
                    if separator_count - 1 > 0:
                        heapq.heappush(min_heap, (separator_idx, separator_count - 1))
                count -= repeatLimit - prev_amount
                if count > 0:
                    heapq.heappush(min_heap, (idx, count))
                prev_amount = 1
            else:
                prev_amount = count
                output.extend(chr(-idx + 97) for _ in range(count))
        return ''.join(output)

# C++ O(NlogK) O(K) Priority Queue Sorting
class Solution {
public:
    string repeatLimitedString(string s, int repeatLimit) {
        std::vector<int> chunks(26, 0);
        for (char& ch : s) {
            ++chunks[ch - 'a'];
        }
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>> maxHeap;
        for (int idx = 0; idx < 26; ++idx) {
            if (chunks[idx]) {
                maxHeap.push({idx, chunks[idx]});
            }
        }
        std::string output = "";
        int prevAmount = 0;
        while (maxHeap.size()) {
            int idx = maxHeap.top().first;
            int count = maxHeap.top().second;
            maxHeap.pop();
            if (output.size() && idx != (output[output.size() - 1] - 'a')) {
                prevAmount = 0;
            }
            if (count >= repeatLimit - prevAmount) {
                int amount = repeatLimit - prevAmount;
                for (int i = 0; i < amount; ++i) {
                    output.push_back(static_cast<char>(idx + 97));
                }
                count -= amount;
                if (maxHeap.empty()) {
                    break;
                } else {
                    int separatorIdx = maxHeap.top().first;
                    int separatorCount = maxHeap.top().second;
                    maxHeap.pop();
                    prevAmount = 1;
                    output.push_back(static_cast<char>(separatorIdx + 97));
                    if (separatorCount - 1 > 0) {
                        maxHeap.push({separatorIdx, separatorCount - 1});
                    }
                }
                if (count > 0) {
                    maxHeap.push({idx, count});
                }
            } else {
                prevAmount = 0;
                for (int i = 0; i < count; ++i) {
                    output.push_back(static_cast<char>(idx + 97));
                }
            }
        }
        return output;
    }
};