# B. Sequence Game
# time limit per test2 seconds
# memory limit per test256 megabytes
# Tema and Vika are playing the following game.
#
# First, Vika comes up with a sequence of positive integers a
#  of length m
#  and writes it down on a piece of paper. Then she takes a new piece of paper and writes down the sequence b
#  according to the following rule:
#
# First, she writes down a1
# .
# Then, she writes down only those ai
#  (2≤i≤m
# ) such that ai−1≤ai
# . Let the length of this sequence be denoted as n
# .
# For example, from the sequence a=[4,3,2,6,3,3]
# , Vika will obtain the sequence b=[4,6,3]
# .
#
# She then gives the piece of paper with the sequence b
#  to Tema. He, in turn, tries to guess the sequence a
# .
#
# Tema considers winning in such a game highly unlikely, but still wants to find at least one sequence a
#  that could have been originally chosen by Vika. Help him and output any such sequence.
#
# Note that the length of the sequence you output should not exceed the input sequence length by more than two times.
#
# Input
# Each test consists of multiple test cases. The first line of input data contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. This is followed by a description of the test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤2⋅105
# ) — the length of the sequence b
# .
#
# The second line of each test case contains n
#  integers b1,b2,b3,…,bn
#  (1≤bi≤109
# ) — the elements of the sequence.
#
# The sum of the values of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output two lines. In the first line, output a single integer m
#  — the length of the sequence (n≤m≤2⋅n
# ). In the second line, output m
#  integers a1,a2,a3,…,am
#  (1≤ai≤109
# ) — the assumed sequence that Vika could have written on the first piece of paper.
#
# If there are multiple suitable sequences, you can output any of them.
#
# Example
# InputCopy
# 6
# 3
# 4 6 3
# 3
# 1 2 3
# 5
# 1 7 9 5 7
# 1
# 144
# 2
# 1 1
# 5
# 1 2 2 1 1
# OutputCopy
# 6
# 4 3 2 6 3 3
# 3
# 1 2 3
# 6
# 1 7 9 3 5 7
# 1
# 144
# 2
# 1 1
# 6
# 1 2 2 1 1 1
# Note
# The first sample is explained in the problem statement.
#
# In the second sample, Vika could have chosen the original sequence.
# Solution
# C++ O(N) O(N) Simulation Greedy
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> nums;
        int count = 0;
        for (int j = 0; j < n; ++j) {
            int num;
            std::scanf("%d", &num);
            if (nums.empty() || nums.back() <= num) nums.push_back(num);
            else {
                nums.push_back(num);
                nums.push_back(num);
            }
        }
        std::printf("%d\n", nums.size());
        for (int j = 0; j < nums.size(); ++j) std::printf("%d ", nums[j]);
        if (!nums.empty()) std::printf("\n");
    }
}


int main() {
    solution();
}

# Python O(N) O(N) Simulation Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        sequence: list[int] = []
        for i in range(n):
            num: int = next(nums)
            if not sequence or sequence[-1] <= num: sequence.append(num)
            else: sequence.append(num); sequence.append(num)
        sys.stdout.write('{}\n{}\n'.format(len(sequence), ' '.join(str(num) for num in sequence)))


if __name__ == '__main__':
    solution()