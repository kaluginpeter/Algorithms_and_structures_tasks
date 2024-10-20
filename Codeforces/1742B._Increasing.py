# B. Increasing
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an array a
#  of n
#  positive integers. Determine if, by rearranging the elements, you can make the array strictly increasing. In other words, determine if it is possible to rearrange the elements such that a1<a2<⋯<an
#  holds.
#
# Input
# The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the length of the array.
#
# The second line of each test case contains n
#  integers ai
#  (1≤ai≤109
# ) — the elements of the array.
#
# Output
# For each test case, output "YES" (without quotes) if the array satisfies the condition, and "NO" (without quotes) otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# inputCopy
# 3
# 4
# 1 1 1 1
# 5
# 8 7 1 3 4
# 1
# 5
# outputCopy
# NO
# YES
# YES
# Note
# In the first test case any rearrangement will keep the array [1,1,1,1]
# , which is not strictly increasing.
#
# In the second test case, you can make the array [1,3,4,7,8]
# .
# Solution
# C++ O(NlogN) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> nums;
        for (int j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            nums.push_back(num);
        }
        std::sort(nums.begin(), nums.end());
        bool isValid = true;
        for (size_t index = 0; index < nums.size() - 1; ++index) {
            if (nums[index] >= nums[index + 1]) {
                isValid = false;
                break;
            }
        }
        std::cout << (isValid ? "YES" : "NO") << std::endl;
    }
}

# Python O(NlogN) O(1) Sorting Greedy
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
        nums.sort()
        sys.stdout.write(['NO', 'YES'][all(nums[idx] < nums[idx + 1] for idx in range(n - 1))] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
