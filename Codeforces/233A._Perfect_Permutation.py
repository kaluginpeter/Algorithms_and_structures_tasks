# A. Perfect Permutation
# time limit per test2 seconds
# memory limit per test256 megabytes
# A permutation is a sequence of integers p1, p2, ..., pn, consisting of n distinct positive integers, each of them doesn't exceed n. Let's denote the i-th element of permutation p as pi. We'll call number n the size of permutation p1, p2, ..., pn.
#
# Nickolas adores permutations. He likes some permutations more than the others. He calls such permutations perfect. A perfect permutation is such permutation p that for any i (1 ≤ i ≤ n) (n is the permutation size) the following equations hold ppi = i and pi ≠ i. Nickolas asks you to print any perfect permutation of size n for the given n.
#
# Input
# A single line contains a single integer n (1 ≤ n ≤ 100) — the permutation size.
#
# Output
# If a perfect permutation of size n doesn't exist, print a single integer -1. Otherwise print n distinct integers from 1 to n, p1, p2, ..., pn — permutation p, that is perfect. Separate printed numbers by whitespaces.
#
# Examples
# InputCopy
# 1
# OutputCopy
# -1
# InputCopy
# 2
# OutputCopy
# 2 1
# InputCopy
# 4
# OutputCopy
# 2 1 4 3
# Solution
# Python O(N) O(N) Math
import sys


def solution(n: int) -> str:
    if n % 2 != 0:
        return '-1'

    permutation = []
    for i in range(1, n + 1, 2):
        permutation.append(i + 1)  # p[i] is i + 1
        permutation.append(i)  # p[i + 1] is i

    return ' '.join(map(str, permutation))


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(n) + '\n')

# C++ O(N) O(1) Math
#include <iostream>
#include <string>

void solution(int& n) {
    if (n % 2 != 0) {
        std::cout << "-1\n";
        return;
    }
    std::string output = "";
    for (int i = 1; i <= n; i += 2) {
        if (i != 1) {
            std::cout << " ";
        }
        std::cout << std::to_string(i + 1) << " " << std::to_string(i);
    }
}

int main() {
    int n;
    std::cin >> n;
    solution(n);
}
