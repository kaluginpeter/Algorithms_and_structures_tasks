# B. Multiple Construction
# time limit per test1 second
# memory limit per test256 megabytes
# You are given an integer n
# . Your task is to construct an array of length 2⋅n
#  such that:
#
# Each integer from 1
#  to n
#  appears exactly twice in the array.
# For each integer x
#  (1≤x≤n
# ), the distance between the two occurrences of x
#  is a multiple of x
# . In other words, if px
#  and qx
#  are the indices of the two occurrences of x
# , |qx−px|
#  must be divisible by x
# .
# It can be shown that a solution always exists.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# Each of the next t
#  lines contains a single integer n
#  (1≤n≤2⋅105
# ).
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, print a line containing 2⋅n
#  integers — the array that satisfies the given conditions.
#
# If there are multiple valid answers, print any of them.
#
# Example
# InputCopy
# 3
# 2
# 3
# 1
# OutputCopy
# 1 2 1 2
# 1 3 1 2 3 2
# 1 1
# Note
# Visualizer link
#
# In the first test case:
#
# The number 1
#  appears at positions 1
#  and 3
# : the distance is 2
# , which is divisible by 1
# .
# The number 2
#  appears at positions 2
#  and 4
# : the distance is 2
# , which is divisible by 2
# .
# In the second test case:
#
# The number 1
#  appears at positions 1
#  and 3
# : the distance is 2
# , which is divisible by 1
# .
# The number 2
#  appears at positions 4
#  and 6
# : the distance is 2
# , which is divisible by 2
# .
# The number 3
#  appears at positions 2
#  and 5
# : the distance is 3
# , which is divisible by 3
# .
# In the third test case, the two occurrences of 1
#  are at positions 1
#  and 2
# , so the distance between them is 1
# , which is a multiple of 1
# .
# Solution
# C++ O(N) O(N) Greedy
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(2 * n + 1, 0);
    size_t ptr = 0;
    int target = (n & 1 ? n - 1 : n);
    while (target > 1) {
        nums[ptr] = target;
        nums[ptr + target] = target;
        ++ptr;
        target -= 2;
    }
    target = (n & 1 ? n : n - 1);
    while (target >= 1) {
        while (ptr < 2 * n && nums[ptr]) ++ptr;
        nums[ptr] = target;
        if (target == 1) {
            while (ptr < 2 * n && nums[ptr]) ++ptr;
            nums[ptr] = target;
        } else nums[ptr + target] = target;
        target -= 2;
    }
    for (size_t i = 0; i < 2 * n; ++i) std::cout << nums[i] << " ";
    std::cout << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(N) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    output: list[int] = [0] * (2 * n)
    target: int = n - (n & 1)
    ptr: int = 0
    while target:
        output[ptr] = target
        output[ptr + target] = target
        ptr += 1
        target -= 2
    target = n - int(n % 2 == 0)
    while target >= 1:
        while ptr < 2 * n and output[ptr]: ptr += 1
        output[ptr] = target
        if target == 1:
            while ptr < 2 * n and output[ptr]: ptr += 1
            output[ptr] = target
        else: output[ptr + target] = target
        target -= 2
    sys.stdout.write('{}\n'.format(' '.join(map(str, output))))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()