# A. Flipping Game
# time limit per test1 second
# memory limit per test256 megabytes
# Iahub got bored, so he invented a game to be played on paper.
#
# He writes n integers a1, a2, ..., an. Each of those integers can be either 0 or 1. He's allowed to do exactly one move: he chooses two indices i and j (1 ≤ i ≤ j ≤ n) and flips all values ak for which their positions are in range [i, j] (that is i ≤ k ≤ j). Flip the value of x means to apply operation x = 1 - x.
#
# The goal of the game is that after exactly one move to obtain the maximum number of ones. Write a program to solve the little game of Iahub.
#
# Input
# The first line of the input contains an integer n (1 ≤ n ≤ 100). In the second line of the input there are n integers: a1, a2, ..., an. It is guaranteed that each of those n values is either 0 or 1.
#
# Output
# Print an integer — the maximal number of 1s that can be obtained after exactly one move.
#
# Examples
# InputCopy
# 5
# 1 0 0 1 0
# OutputCopy
# 4
# InputCopy
# 4
# 1 0 0 1
# OutputCopy
# 4
# Note
# In the first case, flip the segment from 2 to 5 (i = 2, j = 5). That flip changes the sequence, it becomes: [1 1 1 0 1]. So, it contains four ones. There is no way to make the whole sequence equal to [1 1 1 1 1].
#
# In the second case, flipping only the second and the third element (i = 2, j = 3) will turn all numbers into 1.
# Solution
# C++ O(N**3) O(1)
#include <iostream>
#include <vector>


void solution(int& n, std::vector<int>& nums) {
    int initialCountOfOnes = 0;
    for (int value : nums) {
        if (value == 1) {
            initialCountOfOnes++;
        }
    }
    int maxOnes = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            int count0s = 0;
            int count1s = 0;
            for (int k = i; k <= j; k++) {
                if (nums[k] == 0) {
                    count0s++;
                } else {
                    count1s++;
                }
            }
            int newCountOfOnes = initialCountOfOnes + count0s - count1s;
            maxOnes = std::max(maxOnes, newCountOfOnes);
        }
    }
    if (initialCountOfOnes == n) {
        std::cout << n - 1 << "\n";
        return;
    }
    std::cout << maxOnes << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> nums;
    for (int i = 0; i < n; ++i) {\
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    solution(n, nums);
}

# Python O(N**3) O(1)
import sys


def solution(n: int, nums: list) -> None:
    initial_count_of_ones: int = sum(nums)
    max_ones: int = 0
    for i in range(n):
        for j in range(i, n):
            count_0s: int = sum(1 for k in range(i, j + 1) if nums[k] == 0)
            count_1s: int = sum(1 for k in range(i, j + 1) if nums[k] == 1)
            new_count_of_ones: int = initial_count_of_ones + count_0s - count_1s

            max_ones = max(max_ones, new_count_of_ones)
    if initial_count_of_ones == n:
        sys.stdout.write(str(n - 1) + '\n')
        return
    sys.stdout.write(str(max_ones) + '\n')

if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
    solution(n, nums)