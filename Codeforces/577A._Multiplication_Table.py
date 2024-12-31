# A. Multiplication Table
# time limit per test1 second
# memory limit per test256 megabytes
# Let's consider a table consisting of n rows and n columns. The cell located at the intersection of i-th row and j-th column contains number i × j. The rows and columns are numbered starting from 1.
#
# You are given a positive integer x. Your task is to count the number of cells in a table that contain number x.
#
# Input
# The single line contains numbers n and x (1 ≤ n ≤ 105, 1 ≤ x ≤ 109) — the size of the table and the number that we are looking for in the table.
#
# Output
# Print a single number: the number of times x occurs in the table.
#
# Examples
# InputCopy
# 10 5
# OutputCopy
# 2
# InputCopy
# 6 12
# OutputCopy
# 4
# InputCopy
# 5 13
# OutputCopy
# 0
# Note
# A table for the second sample test is given below. The occurrences of number 12 are marked bold.
# Solution
# C++ O(x) O(1) Number Theory
#include <iostream>


void solution() {
    int n, x;
    std::cin >> n >> x;
    int count = 0;
    int bound = std::min(x, n);
    for (int m = 1; m <= bound; ++m) {
        if (x % m == 0 && x / m <= bound) {
            ++count;
        }
    }
    std::cout << count << "\n";
}


int main() {
    solution();
}

# Python O(x) O(1) Number Theory
import sys


def solution() -> None:
    n, x = map(int, sys.stdin.readline().rstrip().split())
    bound: int = min(n, x)
    count: int = 0
    for m in range(1, bound + 1):
        if x % m == 0 and x // m <= bound:
            count += 1
    sys.stdout.write(f'{count}\n')


if __name__ == '__main__':
    solution()
