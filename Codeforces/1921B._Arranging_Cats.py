# B. Arranging Cats
# time limit per test2 seconds
# memory limit per test512 megabytes
# In order to test the hypothesis about the cats, the scientists must arrange the cats in the boxes in a specific way. Of course, they would like to test the hypothesis and publish a sensational article as quickly as possible, because they are too engrossed in the next hypothesis about the phone's battery charge.
#
# Scientists have n
#  boxes in which cats may or may not sit. Let the current state of the boxes be denoted by the sequence b1,…,bn
# : bi=1
#  if there is a cat in box number i
# , and bi=0
#  otherwise.
#
# Fortunately, the unlimited production of cats has already been established, so in one day, the scientists can perform one of the following operations:
#
# Take a new cat and place it in a box (for some i
#  such that bi=0
# , assign bi=1
# ).
# Remove a cat from a box and send it into retirement (for some i
#  such that bi=1
# , assign bi=0
# ).
# Move a cat from one box to another (for some i,j
#  such that bi=1,bj=0
# , assign bi=0,bj=1
# ).
# It has also been found that some boxes were immediately filled with cats. Therefore, the scientists know the initial position of the cats in the boxes s1,…,sn
#  and the desired position f1,…,fn
# .
#
# Due to the large amount of paperwork, the scientists do not have time to solve this problem. Help them for the sake of science and indicate the minimum number of days required to test the hypothesis.
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. This is followed by descriptions of the test cases.
#
# Each test case consists of three lines.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ) — the number of boxes.
#
# The second line of each test case contains a string s
#  of n
#  characters, where the i
# -th character is '1' if there is a cat in the i
# -th box and '0' otherwise.
#
# The third line of each test case contains a string f
#  of n
#  characters, where the i
# -th character is '1' if there should be a cat in the i
# -th box and '0' otherwise.
#
# It is guaranteed that in a test the sum of n
#  over all test cases does not exceed 105
# .
#
# Output
# For each test case, output a single integer on a separate line — the minimum number of operations required to obtain the desired position from the initial position. It can be shown that a solution always exists.
#
# Example
# InputCopy
# 6
# 5
# 10010
# 00001
# 1
# 1
# 1
# 3
# 000
# 111
# 4
# 0101
# 1010
# 3
# 100
# 101
# 8
# 10011001
# 11111110
# OutputCopy
# 2
# 0
# 3
# 2
# 1
# 4
# Note
# In the first test case, you can first move the cat from the first box to the fifth, and then remove the cat from the fourth box.
#
# In the second test case, there is nothing to do — the only cat is already sitting in the correct box.
#
# In the third test case of input data, it takes three days to place a cat in each box.
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>
#include <cmath>


void solution() {
    int t;
    std::scanf("%d\n", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d\n", &n);
        std::string start, end;
        std::cin >> start >> end;
        int extra = 0, needed = 0;
        for (int j = 0; j < n; ++j) {
            if (start[j] != end[j]) {
                if (start[j] == '0') ++extra;
                else ++needed;
            }
        }
        int rem = std::abs(extra - needed);
        std::printf("%d\n", rem + std::min(extra, needed));
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        start: str = sys.stdin.readline().rstrip()
        end: str = sys.stdin.readline().rstrip()
        extra: int = 0
        needed: int = 0
        for i in range(n):
            if start[i] != end[i]:
                if start[i] == '0': extra += 1
                else: needed += 1
        rem: int = abs(extra - needed)
        sys.stdout.write('{}\n'.format(rem + min(extra, needed)))


if __name__ == '__main__':
    solution()