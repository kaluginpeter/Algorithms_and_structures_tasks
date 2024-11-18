# B. Ilya and Queries
# time limit per test2 seconds
# memory limit per test256 megabytes
# Ilya the Lion wants to help all his friends with passing exams. They need to solve the following problem to pass the IT exam.
#
# You've got string s = s1s2... sn (n is the length of the string), consisting only of characters "." and "#" and m queries. Each query is described by a pair of integers li, ri (1 ≤ li < ri ≤ n). The answer to the query li, ri is the number of such integers i (li ≤ i < ri), that si = si + 1.
#
# Ilya the Lion wants to help his friends but is there anyone to help him? Help Ilya, solve the problem.
#
# Input
# The first line contains string s of length n (2 ≤ n ≤ 105). It is guaranteed that the given string only consists of characters "." and "#".
#
# The next line contains integer m (1 ≤ m ≤ 105) — the number of queries. Each of the next m lines contains the description of the corresponding query. The i-th line contains integers li, ri (1 ≤ li < ri ≤ n).
#
# Output
# Print m integers — the answers to the queries in the order in which they are given in the input.
#
# Examples
# InputCopy
# ......
# 4
# 3 4
# 2 3
# 1 6
# 2 6
# OutputCopy
# 1
# 1
# 5
# 4
# InputCopy
# #..###
# 5
# 1 3
# 5 6
# 1 5
# 3 6
# 3 4
# OutputCopy
# 1
# 1
# 2
# 2
# 0
# Solution
# C++ O(N) O(N) Prefix Sum
#include <iostream>
#include <string>
#include <vector>


int main() {
    std::string exams;
    std::cin >> exams;
    int n = exams.size();
    std::vector<int> prefix(n, 0);
    for (int index = 0; index < n - 1; ++index) {
        int score = (exams[index] == exams[index + 1]? 1 : 0);
        if (!index) {
            prefix[index] = score;
        } else {
            prefix[index] = score + prefix[index - 1];
        }
    }
    if (n > 1) {
        prefix[n - 1] = prefix[n - 2];
    }
    int m;
    std::cin >> m;
    for (int i = 0; i < m; ++i) {
        int left, right;
        std::cin >> left >> right;
        std::cout << (right - 1? prefix[right - 2] : 0) - (left - 1? prefix[left - 2] : 0) << "\n";
    }
}

# Python O(N) O(N) Prefix Sum
import sys


def solution(exams: str, m: int) -> None:
    n: int = len(exams)
    prefix: list = [0] * n
    for idx in range(n - 1):
        score: int = exams[idx] == exams[idx + 1]
        prefix[idx] = prefix[idx - 1] + score
    if n > 1:
        prefix[-1] = prefix[-2]
    for _ in range(m):
        left, right = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str((prefix[right - 2] if right - 1 else 0) - (prefix[left - 2] if left - 1 else 0)) + '\n')


if __name__ == '__main__':
    exams: str = sys.stdin.readline().rstrip()
    m: int = int(sys.stdin.readline().rstrip())
    solution(exams, m)
