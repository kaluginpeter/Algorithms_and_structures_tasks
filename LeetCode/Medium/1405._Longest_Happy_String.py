# A string s is called happy if it satisfies the following conditions:
#
# s only contains the letters 'a', 'b', and 'c'.
# s does not contain any of "aaa", "bbb", or "ccc" as a substring.
# s contains at most a occurrences of the letter 'a'.
# s contains at most b occurrences of the letter 'b'.
# s contains at most c occurrences of the letter 'c'.
# Given three integers a, b, and c, return the longest possible happy string. If there are multiple longest happy strings, return any of them. If there is no such string, return the empty string "".
#
# A substring is a contiguous sequence of characters within a string.
#
#
#
# Example 1:
#
# Input: a = 1, b = 1, c = 7
# Output: "ccaccbcc"
# Explanation: "ccbccacc" would also be a correct answer.
# Example 2:
#
# Input: a = 7, b = 1, c = 0
# Output: "aabaa"
# Explanation: It is the only correct answer in this case.
#
#
# Constraints:
#
# 0 <= a, b, c <= 100
# a + b + c > 0
# Solution
# Python Heap Greedy
# General idea
# at each iteration choose letter with longest possible moves and second letter for separation.
# Use almost 2 letters from first letter, until we don't have enough letters and separate by 1 from second letter. Priority queue by maximum heap can help us to choose optimal first and second letters.
#
# In python we use negative numbers tricky to make max heap from builtin min heap.
#
# Complexity
# Time complexity: O(a + b + c)
#
# Space complexity: O(a + b + c)
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        output: list[str] = []
        heap: list[list[int, str]] = [[-a, 'a'], [-b, 'b'], [-c, 'c']]
        heapq.heapify(heap)
        while heap:
            first_move_least_steps, first_move_letter = heapq.heappop(heap)
            first_move_least_steps *= -1
            second_move_least_steps, second_move_letter = 0, ''
            if heap:
                second_move_least_steps, second_move_letter = heapq.heappop(heap)
            if len(output) > 1 and first_move_letter == output[-2] == output[-1]:
                break
            current_step: int = min(first_move_least_steps, 2) - (output[-1] == first_move_letter if output else 0)
            if first_move_least_steps:
                current_step = max(current_step, 1)
            output.extend([first_move_letter] * current_step)
            first_move_least_steps -= current_step
            if first_move_least_steps > 0:
                heapq.heappush(heap, [-first_move_least_steps, first_move_letter])
            second_move_least_steps *= -1
            next_second_step: int = min(second_move_least_steps, 1)
            output.extend([second_move_letter] * next_second_step)
            second_move_least_steps -= next_second_step
            if second_move_least_steps > 0:
                heapq.heappush(heap, [-second_move_least_steps, second_move_letter])

        return ''.join(output)

# C++ Heap Greedy
# General idea
# at each iteration choose letter with longest possible moves and second letter for separation.
# Use almost 2 letters from first letter, until we don't have enough letters and separate by 1 from second letter. Priority queue by maximum heap can help us to choose optimal first and second letters.
#
# In python we use negative numbers tricky to make max heap from builtin min heap.
#
# Complexity
# Time complexity: O(a + b + c)
#
# Space complexity: O(a + b + c)
class Solution {
public:
    string longestDiverseString(int a, int b, int c) {
        std::string output;
        std::priority_queue<std::pair<int, char>> heap;
        heap.push({a, 'a'});
        heap.push({b, 'b'});
        heap.push({c, 'c'});
        while (heap.size()) {
            int first_move_least_steps = heap.top().first;
            char first_move_letter = heap.top().second;
            heap.pop();
            int second_move_least_steps = 0;
            char second_move_letter;
            if (heap.size()) {
                second_move_least_steps = heap.top().first;
                second_move_letter = heap.top().second;
                heap.pop();
            }
            if (output.size() > 1 && output[output.size() - 2] == first_move_letter && output[output.size() - 1] == first_move_letter) {
                break;
            }
            int next_move = std::min(first_move_least_steps, 2) - (output.size() && output[output.size() - 1] == first_move_letter ? 1 : 0);
            if (first_move_least_steps) {
                next_move = std::max(next_move, 1);
            }
            for (int rep = 0; rep < next_move; ++rep) {
                output += first_move_letter;
            }
            first_move_least_steps -= next_move;
            if (first_move_least_steps > 0) {
                heap.push({first_move_least_steps, first_move_letter});
            }
            int next_second_move = std::min(second_move_least_steps, 1);
            for (int rep = 0; rep < next_second_move; ++rep) {
                output += second_move_letter;
            }
            second_move_least_steps -= next_second_move;
            if (second_move_least_steps > 0) {
                heap.push({second_move_least_steps, second_move_letter});
            }
        }
        return output;
    }
};