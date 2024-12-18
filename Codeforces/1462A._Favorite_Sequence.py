# A. Favorite Sequence
# time limit per test2 seconds
# memory limit per test256 megabytes
# Polycarp has a favorite sequence a[1…n]
#  consisting of n
#  integers. He wrote it out on the whiteboard as follows:
#
# he wrote the number a1
#  to the left side (at the beginning of the whiteboard);
# he wrote the number a2
#  to the right side (at the end of the whiteboard);
# then as far to the left as possible (but to the right from a1
# ), he wrote the number a3
# ;
# then as far to the right as possible (but to the left from a2
# ), he wrote the number a4
# ;
# Polycarp continued to act as well, until he wrote out the entire sequence on the whiteboard.
# The beginning of the result looks like this (of course, if n≥4
# ).
# For example, if n=7
#  and a=[3,1,4,1,5,9,2]
# , then Polycarp will write a sequence on the whiteboard [3,4,5,2,9,1,1]
# .
#
# You saw the sequence written on the whiteboard and now you want to restore Polycarp's favorite sequence.
#
# Input
# The first line contains a single positive integer t
#  (1≤t≤300
# ) — the number of test cases in the test. Then t
#  test cases follow.
#
# The first line of each test case contains an integer n
#  (1≤n≤300
# ) — the length of the sequence written on the whiteboard.
#
# The next line contains n
#  integers b1,b2,…,bn
#  (1≤bi≤109
# ) — the sequence written on the whiteboard.
#
# Output
# Output t
#  answers to the test cases. Each answer — is a sequence a
#  that Polycarp wrote out on the whiteboard.
#
# Example
# InputCopy
# 6
# 7
# 3 4 5 2 9 1 1
# 4
# 9 2 7 1
# 11
# 8 4 3 1 2 7 8 7 9 4 2
# 1
# 42
# 2
# 11 7
# 8
# 1 1 1 1 1 1 1 1
# OutputCopy
# 3 1 4 1 5 9 2
# 9 1 2 7
# 8 2 4 4 3 9 1 7 2 8 7
# 42
# 11 7
# 1 1 1 1 1 1 1 1
# Note
# In the first test case, the sequence a
#  matches the sequence from the statement. The whiteboard states after each step look like this:
#
# [3]⇒[3,1]⇒[3,4,1]⇒[3,4,1,1]⇒[3,4,5,1,1]⇒[3,4,5,9,1,1]⇒[3,4,5,2,9,1,1]
# .
# Solutuion
# C++ O(N) O(N) Simulation
#include <iostream>
#include <vector>


void solution(int& t) {
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> nums;
        for (int j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            nums.push_back(num);
        }
        std::vector<int> output(n, 0);
        int step = n;
        int curIndex = n;
        for (int j = 0; j < n; ++j) {
            if (j % 2 == 0) {
                curIndex -= step;
                output[j] = nums[curIndex];
            } else {
                curIndex += step;
                output[j] = nums[curIndex];
            }
            --step;
        }
        for (int idx = 0; idx < n; ++idx) {
            if (idx) {
                std::cout << " ";
            }
            std::cout << output[idx];
        }
        std::cout << "\n";
    }
}


int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(N) O(N) Simulation
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list = list(map(int, sys.stdin.readline().rstrip().split()))
        output: list = [0] * n
        cur_index: int = n
        step: int = n
        for idx in range(n):
            if idx & 1:
                cur_index += step
                output[idx] = nums[cur_index]
            else:
                cur_index -= step
                output[idx] = nums[cur_index]
            step -= 1
        for idx in range(n):
            if idx:
                sys.stdout.write(' ')
            sys.stdout.write(str(output[idx]))
        sys.stdout.write('\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
