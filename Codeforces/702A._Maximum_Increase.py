# A. Maximum Increase
# time limit per test1 second
# memory limit per test256 megabytes
# You are given array consisting of n integers. Your task is to find the maximum length of an increasing subarray of the given array.
#
# A subarray is the sequence of consecutive elements of the array. Subarray is called increasing if each element of this subarray strictly greater than previous.
#
# Input
# The first line contains single positive integer n (1 ≤ n ≤ 105) — the number of integers.
#
# The second line contains n positive integers a1, a2, ..., an (1 ≤ ai ≤ 109).
#
# Output
# Print the maximum length of an increasing subarray of the given array.
#
# Examples
# InputCopy
# 5
# 1 7 2 11 15
# OutputCopy
# 3
# InputCopy
# 6
# 100 100 100 100 100 100
# OutputCopy
# 1
# InputCopy
# 3
# 1 2 3
# OutputCopy
# 3
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>

int main() {
    int maxSeq = 0;
    int curSeq = 0;
    int prevNum = 0;
    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        if (num <= prevNum) {
            curSeq = 1;
        } else {
            ++curSeq;
        }
        maxSeq = std::max(maxSeq, curSeq);
        prevNum = num;
    }
    std::cout << maxSeq << std::endl;
}

# Python O(N) O(1) Greedy
import sys


def solution(n: int) -> str:
    max_seq: int = 0
    cur_seq: int = 0
    prev_num: int = 0
    nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
    for idx in range(n):
        if nums[idx] <= prev_num:
            cur_seq = 1
        else:
            cur_seq += 1
        prev_num = nums[idx]
        max_seq = max(max_seq, cur_seq)
    return str(max_seq)

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n))
