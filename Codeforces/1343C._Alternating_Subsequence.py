# C. Alternating Subsequence
# time limit per test1 second
# memory limit per test256 megabytes
# Recall that the sequence b
#  is a a subsequence of the sequence a
#  if b
#  can be derived from a
#  by removing zero or more elements without changing the order of the remaining elements. For example, if a=[1,2,1,3,1,2,1]
# , then possible subsequences are: [1,1,1,1]
# , [3]
#  and [1,2,1,3,1,2,1]
# , but not [3,2,3]
#  and [1,1,1,1,2]
# .
#
# You are given a sequence a
#  consisting of n
#  positive and negative elements (there is no zeros in the sequence).
#
# Your task is to choose maximum by size (length) alternating subsequence of the given sequence (i.e. the sign of each next element is the opposite from the sign of the current element, like positive-negative-positive and so on or negative-positive-negative and so on). Among all such subsequences, you have to choose one which has the maximum sum of elements.
#
# In other words, if the maximum length of alternating subsequence is k
#  then your task is to find the maximum sum of elements of some alternating subsequence of length k
# .
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤104
# ) — the number of test cases. Then t
#  test cases follow.
#
# The first line of the test case contains one integer n
#  (1≤n≤2⋅105
# ) — the number of elements in a
# . The second line of the test case contains n
#  integers a1,a2,…,an
#  (−109≤ai≤109,ai≠0
# ), where ai
#  is the i
# -th element of a
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
#  (∑n≤2⋅105
# ).
#
# Output
# For each test case, print the answer — the maximum sum of the maximum by size (length) alternating subsequence of a
# .
#
# Example
# InputCopy
# 4
# 5
# 1 2 3 -1 -2
# 4
# -1 -2 -1 -3
# 10
# -2 8 3 8 -4 -15 5 -2 -3 1
# 6
# 1 -1000000000 1 -1000000000 1 -1000000000
# OutputCopy
# 2
# -1
# 6
# -2999999997
# Note
# In the first test case of the example, one of the possible answers is [1,2,3–,−1–––,−2]
# .
#
# In the second test case of the example, one of the possible answers is [−1,−2,−1–––,−3]
# .
#
# In the third test case of the example, one of the possible answers is [−2–––,8,3,8–,−4–––,−15,5–,−2–––,−3,1–]
# .
#
# In the fourth test case of the example, one of the possible answers is [1–,−1000000000–––––––––––––,1–,−1000000000–––––––––––––,1–,−1000000000–––––––––––––]
# .
# Solution
# C++ O(N) O(1) Greedy SlidingWindow
#include <iostream>
#include <vector>
#include <cstdint>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> nums (n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &nums[j]);
        long long maxPositive = INT64_MIN;
        int positiveLength = 0;
        bool isPositive = true;
        int left = 0;
        int right = 0;
        while (right < n) {
            if (isPositive) {
                while (left < n && nums[left] < 0) ++left;
                if (left == n) break;
                right = std::max(right, left + 1);
                int curPositive = nums[left];
                while (right < n && nums[right] >= 0) {
                    curPositive = std::max(curPositive, nums[right]);
                    ++right;
                }
                if (maxPositive == INT64_MIN) maxPositive = 0;
                ++positiveLength;
                maxPositive += (long long)curPositive;
                left = right;
            } else {
                while (left < n && nums[left] >= 0) ++left;
                if (left == n) break;
                right = std::max(right, left + 1);
                int curNegative = nums[left];
                while (right < n && nums[right] < 0) {
                    curNegative = std::max(curNegative, nums[right]);
                    ++right;
                }
                ++positiveLength;
                maxPositive += (long long)curNegative;
                left = right;
            }
            isPositive = !isPositive;
        }

        long long maxNegative = INT64_MIN;
        int negativeLength = 0;
        isPositive = false;
        left = 0;
        right = 0;
        while (right < n) {
            if (isPositive) {
                while (left < n && nums[left] < 0) ++left;
                if (left == n) break;
                right = std::max(right, left + 1);
                int curPositive = nums[left];
                while (right < n && nums[right] >= 0) {
                    curPositive = std::max(curPositive, nums[right]);
                    ++right;
                }
                maxNegative += (long long)curPositive;
                ++negativeLength;
                left = right;
            } else {
                while (left < n && nums[left] >= 0) ++left;
                if (left == n) break;
                right = std::max(right, left + 1);
                int curNegative = nums[left];
                while (right < n && nums[right] < 0) {
                    curNegative = std::max(curNegative, nums[right]);
                    ++right;
                }
                if (maxNegative == INT64_MIN) maxNegative = 0;
                maxNegative += (long long) curNegative;
                ++negativeLength;
                left = right;
            }
            isPositive = !isPositive;
        }
        if (positiveLength > negativeLength) std::printf("%lld\n", maxPositive);
        else if (positiveLength < negativeLength) std::printf("%lld\n", maxNegative);
        else std::printf("%lld\n", std::max(maxPositive, maxNegative));
    }
}


int main() {
    solution();
}

# Python O(N) O(1) SlidingWindow Greedy
import sys


def get_pass(nums: list[int], is_positive: bool) -> tuple[int, int]:
    n: int = len(nums)
    length: int = 0
    cur_sum = float('-inf')
    left: int = 0
    right: int = 0
    while right < n:
        if is_positive:
            while left < n and nums[left] < 0: left += 1
            if left == n: break
            cur_number: int = nums[left]
            right = max(right, left + 1)
            while right < n and nums[right] >= 0:
                cur_number = max(cur_number, nums[right])
                right += 1
            if cur_sum == float('-inf'): cur_sum = 0
            cur_sum += cur_number
            left = right
            length += 1
        else:
            while left < n and nums[left] >= 0: left += 1
            if left == n: break
            cur_number: int = nums[left]
            right = max(right, left + 1)
            while right < n and nums[right] < 0:
                cur_number = max(cur_number, nums[right])
                right += 1
            if cur_sum == float('-inf'): cur_sum = 0
            cur_sum += cur_number
            left = right
            length += 1
        is_positive = not is_positive
    return (cur_sum, length)


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        max_positive, positive_length = get_pass(nums, True)
        max_negative, negative_length = get_pass(nums, False)
        if positive_length > negative_length:
            sys.stdout.write('{}\n'.format(max_positive))
        elif positive_length < negative_length:
            sys.stdout.write('{}\n'.format(max_negative))
        else: sys.stdout.write('{}\n'.format(max(max_negative, max_positive)))


if __name__ == '__main__':
    solution()