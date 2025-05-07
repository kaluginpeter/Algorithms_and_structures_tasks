# C. Unique Number
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given a positive number x
# . Find the smallest positive integer number that has the sum of digits equal to x
#  and all digits are distinct (unique).
#
# Input
# The first line contains a single positive integer t
#  (1≤t≤50
# ) — the number of test cases in the test. Then t
#  test cases follow.
#
# Each test case consists of a single integer number x
#  (1≤x≤50
# ).
#
# Output
# Output t
#  answers to the test cases:
#
# if a positive integer number with the sum of digits equal to x
#  and all digits are different exists, print the smallest such number;
# otherwise print -1.
# Example
# InputCopy
# 4
# 1
# 5
# 15
# 50
# OutputCopy
# 1
# 5
# 69
# -1
# Solution
# C++ O(logN) O(logN) Math Greedy
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        int output = -1;
        if (n > 45) {
            std::printf("-1\n");
            continue;
        }
        std::vector<bool> hashmap(10, false);
        std::vector<int> digits;
        while (n > 0) {
            for (int digit = 9; digit > 0; --digit) {
                if (!hashmap[digit] && digit <= n) {
                    digits.push_back(digit);
                    hashmap[digit] = true;
                    n -= digit;
                    break;
                }
            }
        }
        for (int j = digits.size() - 1; j >= 0; --j) {
            std::printf("%d", digits[j]);
        }
        std::printf("\n");
    }
}


int main() {
    solution();
}

# Python O(logN) O(logN) Math Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        if n > 45:
            sys.stdout.write('-1\n')
            continue
        digits: list[int] = []
        used: list[bool] = [False] * 10
        while n:
            for digit in range(9, 0, -1):
                if not used[digit] and digit <= n:
                    used[digit] = True
                    n -= digit
                    digits.append(digit)
                    break
        sys.stdout.write('{}\n'.format(''.join(str(digit) for digit in reversed(digits))))


if __name__ == '__main__':
    solution()