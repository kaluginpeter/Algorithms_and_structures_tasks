# A. The number of positions
# time limit per test0.5 second
# memory limit per test256 megabytes
# Petr stands in line of n people, but he doesn't know exactly which position he occupies. He can say that there are no less than a people standing in front of him and no more than b people standing behind him. Find the number of different positions Petr can occupy.
#
# Input
# The only line contains three integers n, a and b (0 ≤ a, b < n ≤ 100).
#
# Output
# Print the single number — the number of the sought positions.
#
# Examples
# InputCopy
# 3 1 1
# OutputCopy
# 2
# InputCopy
# 5 2 3
# OutputCopy
# 3
# Note
# The possible positions in the first sample are: 2 and 3 (if we number the positions starting with 1).
#
# In the second sample they are 3, 4 and 5.
# Solution
# C++ O(1) O(1) Math
#include <bits/stdc++.h>


void solution() {
    int n, a, b;
    std::cin >> n >> a >> b;
    std::cout << std::min(n - a, b + 1) << "\n";
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    n, a, b = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(str(min(n - a, b + 1)) + '\n')


if __name__ == '__main__':
    solution()
