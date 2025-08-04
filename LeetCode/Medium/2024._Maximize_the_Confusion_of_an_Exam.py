# A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
#
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:
#
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.
#
#
#
# Example 1:
#
# Input: answerKey = "TTFF", k = 2
# Output: 4
# Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
# There are four consecutive 'T's.
# Example 2:
#
# Input: answerKey = "TFFT", k = 1
# Output: 3
# Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
# Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
# In both cases, there are three consecutive 'F's.
# Example 3:
#
# Input: answerKey = "TTFTTFTT", k = 1
# Output: 5
# Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
# Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT".
# In both cases, there are five consecutive 'T's.
#
#
# Constraints:
#
# n == answerKey.length
# 1 <= n <= 5 * 104
# answerKey[i] is either 'T' or 'F'
# 1 <= k <= n
# Solution
# Python O(N) O(1) Sliding Window
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        output: int = 0
        # solve for T
        left: int = 0
        skipped: int = 0
        for right in range(len(answerKey)):
            if answerKey[right] != 'T': skipped += 1
            while skipped > k:
                if answerKey[left] != 'T': skipped -= 1
                left += 1
            output = max(output, right - left + 1)
        # sove for F
        left = 0
        skipped = 0
        for right in range(len(answerKey)):
            if answerKey[right] != 'F': skipped += 1
            while skipped > k:
                if answerKey[left] != 'F': skipped -= 1
                left += 1
            output = max(output, right - left + 1)
        return output

# C++ O(N) O(1) SlidingWindow
class Solution {
public:
    int maxConsecutiveAnswers(string answerKey, int k) {
        int output = 0;
        // solve for T
        int left = 0, misMatched = 0;
        for (int right = 0; right < answerKey.size(); ++right) {
            if (answerKey[right] != 'T') ++misMatched;
            while (misMatched > k) {
                if (answerKey[left] != 'T') --misMatched;
                ++left;
            }
            output = std::max(output, right - left + 1);
        }
        // solve for F
        left = 0;
        misMatched = 0;
        for (int right = 0; right < answerKey.size(); ++right) {
            if (answerKey[right] != 'F') ++misMatched;
            while (misMatched > k) {
                if (answerKey[left] != 'F') --misMatched;
                ++left;
            }
            output = std::max(output, right - left + 1);
        }
        return output;
    }
};