# A. Coins
# time limit per test2 seconds
# memory limit per test256 megabytes
# In Berland, there are two types of coins, having denominations of 2
#  and k
#  burles.
#
# Your task is to determine whether it is possible to represent n
#  burles in coins, i. e. whether there exist non-negative integers x
#  and y
#  such that 2⋅x+k⋅y=n
# .
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The only line of each test case contains two integers n
#  and k
#  (1≤k≤n≤1018
# ; k≠2
# ).
#
# Output
# For each test case, print YES if it is possible to represent n
#  burles in coins; otherwise, print NO. You may print each letter in any case (YES, yes, Yes will all be recognized as positive answer, NO, no and nO will all be recognized as negative answer).
#
# Example
# InputCopy
# 4
# 5 3
# 6 1
# 7 4
# 8 8
# OutputCopy
# YES
# YES
# NO
# YES
# Note
# In the first test case, you can take one coin with denomination 2
#  and one coin with denomination k=3
# .
#
# In the second test case, you can take three coins with denomination 2
# . Alternatively, you can take six coins with denomination k=1
# .
#
# In the third test case, there is no way to represent 7
#  burles.
#
# In the fourth test case, you can take one coin with denomination k=8
# .
# Solution
# C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        long long n, k;
        std::scanf("%lld %lld", &n, &k);
        if (k & 1) {
            std::cout << (k == 1 || n >= 0? "YES" : "NO") << "\n";
        } else {
            std::cout << (n % 2 == 0? "YES" : "NO") << "\n";
        }
    }
}


int main() {
    solution();
}

# Python O(1) O(1) Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        if k & 1:
            sys.stdout.write('{}\n'.format(['NO', 'YES'][k & 1 or n >= 0]))
        else:
            sys.stdout.write('{}\n'.format(['NO', 'YES'][n % 2 == 0]))


if __name__ == '__main__':
    solution()