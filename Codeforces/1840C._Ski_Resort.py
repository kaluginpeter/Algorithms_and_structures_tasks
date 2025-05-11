# C. Ski Resort
# time limit per test1 second
# memory limit per test256 megabytes
# Dima Vatrushin is a math teacher at school. He was sent on vacation for n
#  days for his good work. Dima has long dreamed of going to a ski resort, so he wants to allocate several consecutive days and go skiing. Since the vacation requires careful preparation, he will only go for at least k
#  days.
#
# You are given an array a
#  containing the weather forecast at the resort. That is, on the i
# -th day, the temperature will be ai
#  degrees.
#
# Dima was born in Siberia, so he can go on vacation only if the temperature does not rise above q
#  degrees throughout the vacation.
#
# Unfortunately, Dima was so absorbed in abstract algebra that he forgot how to count. He asks you to help him and count the number of ways to choose vacation dates at the resort.
#
# Input
# The first line of the input contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# Then follow the descriptions of the test cases.
#
# The first line of each test case contains three integers n
# , k
# , q
#  (1≤n≤2⋅105
# , 1≤k≤n
# , −109≤q≤109
# ) — the length of the array a
# , the minimum number of days at the resort, and the maximum comfortable temperature for Dima.
#
# The second line of each test case contains n
#  integers a1,a2,a3,…,an
#  (−109≤ai≤109
# ) — the temperature at the ski resort.
#
# The sum of all n
#  values over all test cases does not exceed 2⋅105
# .
#
# Output
# Output t
#  integers, each of which is the answer to the corresponding test case — the number of ways for Dima to choose vacation dates at the resort.
#
# Example
# InputCopy
# 7
# 3 1 15
# -5 0 -10
# 5 3 -33
# 8 12 9 0 5
# 4 3 12
# 12 12 10 15
# 4 1 -5
# 0 -1 2 5
# 5 5 0
# 3 -1 4 -5 -3
# 1 1 5
# 5
# 6 1 3
# 0 3 -2 5 -4 -4
# OutputCopy
# 6
# 0
# 1
# 0
# 0
# 1
# 9
# Note
# In the first test case of the example, Dima can go on any day, so the suitable dates for him are [1], [2], [3], [1, 2], [2, 3], [1, 2, 3].
#
# In the second and fourth test cases of the example, Dima cannot go on any day due to the high temperature, so there are no suitable dates.
#
# In the third test case of the example, Dima can only go on the dates [1, 2, 3].
# Solution
# C++ O(N) O(1) Math Combinatorics TwoPointers
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, k, q;
        std::scanf("%d %d %d", &n, &k, &q);
        std::vector<int> days(n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &days[j]);
        int left = 0;
        long long output = 0;
        for (int right = 0; right < n; ++right) {
            if (days[right] > q) {
                left = right + 1;
            }
            output += std::max(0, right - left + 1 - k + 1);
        }
        std::printf("%lld\n", output);
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Math Combinatorics TwoPointers
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k, q = map(int, sys.stdin.readline().rstrip().split())
        days: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        output: int = 0
        left: int = 0
        for right in range(n):
            if days[right] > q: left = right + 1
            output += max(0, right - left + 1 - k + 1)
        sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()