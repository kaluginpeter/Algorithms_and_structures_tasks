# A. Alternating Sum of Numbers
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given a sequence of integers. Output the alternating sum of this sequence. In other words, output a1−a2+a3−a4+a5−…
# . That is, the signs of plus and minus alternate, starting with a plus.
#
# Input
# The first line of the test contains one integer t
#  (1≤t≤1000
# ) — the number of test cases. Then follow t
#  test cases.
#
# The first line of each test case contains one integer n
#  (1≤n≤50
# ) — the length of the sequence. The second line of the test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤100
# ).
#
# Output
# Output t
#  lines. For each test case, output the required alternating sum of the numbers.
#
# Example
# InputCopy
# 4
# 4
# 1 2 3 17
# 1
# 100
# 2
# 100 100
# 5
# 3 1 4 1 5
# OutputCopy
# -15
# 100
# 0
# 10
# Solution
# C++ O(N) O(1) Simulation
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    int output = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (i & 1) output -= x;
        else output += x;
    }
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Simulation
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    output: int = 0
    for i in range(n):
        x: int = next(nums)
        if i & 1: output -= x
        else: output += x
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()