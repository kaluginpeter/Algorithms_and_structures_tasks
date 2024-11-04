# C. Prepend and Append
# time limit per test1 second
# memory limit per test256 megabytes
# Timur initially had a binary string†
#  s
#  (possibly of length 0
# ). He performed the following operation several (possibly zero) times:
#
# Add 0
#  to one end of the string and 1
#  to the other end of the string. For example, starting from the string 1011
# , you can obtain either 010111
#  or 110110
# .
# You are given Timur's final string. What is the length of the shortest possible string he could have started with?
# †
#  A binary string is a string (possibly the empty string) whose characters are either 0
#  or 1
# .
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤100
# ) — the number of testcases.
#
# The first line of each test case contains an integer n
#  (1≤n≤2000
# ) — the length of Timur's final string.
#
# The second line of each test case contains a string s
#  of length n
#  consisting of characters 0
#  or 1
# , denoting the final string.
#
# Output
# For each test case, output a single nonnegative integer — the shortest possible length of Timur's original string. Note that Timur's original string could have been empty, in which case you should output 0
# .
#
# Example
# InputCopy
# 9
# 3
# 100
# 4
# 0111
# 5
# 10101
# 6
# 101010
# 7
# 1010110
# 1
# 1
# 2
# 10
# 2
# 11
# 10
# 1011011010
# OutputCopy
# 1
# 2
# 5
# 0
# 3
# 1
# 0
# 2
# 4
# Note
# In the first test case, the shortest possible string Timur started with is 0
# , and he performed the following operation: 0→100
# .
#
# In the second test case, the shortest possible string Timur started with is 11
# , and he performed the following operation: 11→0111
# .
#
# In the third test case, the shortest possible string Timur started with is 10101
# , and he didn't perform any operations.
#
# In the fourth test case, the shortest possible string Timur started with is the empty string (which we denote by ε
# ), and he performed the following operations: ε→10→0101→101010
# .
#
# In the fifth test case, the shortest possible string Timur started with is 101
# , and he performed the following operations: 101→01011→1010110
# .
# Solution
# Python O(N) O(1) Two Pointers
#include <iostream>
#include <string>

int main() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::string input = "";
        for (int j = 0; j < n; ++j) {
            char letter;
            std::cin >> letter;
            input += letter;
        }
        int left = 0;
        int right = n - 1;
        while (left < right && input[left] != input[right]) {
            ++left;
            --right;
        }
        std::cout << right - left + 1 << std::endl;
    }
}

# Python O(N) O(1) Two Pointers
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        s: str = sys.stdin.readline().rstrip()
        left: int = 0
        right: int = n - 1
        while left < right and s[left] != s[right]:
            left += 1
            right -= 1
        sys.stdout.write(str(right - left + 1) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
