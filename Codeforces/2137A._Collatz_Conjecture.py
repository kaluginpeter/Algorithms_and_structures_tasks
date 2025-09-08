# A. Collatz Conjecture
# time limit per test1 second
# memory limit per test256 megabytes
# You are doing a research paper on the famous Collatz Conjecture. In your experiment, you start off with an integer x
# , and you do the following procedure k
#  times:
#
# If x
#  is even, divide x
#  by 2
# .
# Otherwise, set x
#  to 3⋅x+1
# .
# For example, starting off with 21
#  and doing the procedure 5
#  times, you get 21→64→32→16→8→4
# .
#
# After all k
#  iterations, you are left with the final value of x
# . Unfortunately, you forgot the initial value. Please output any possible initial value of x
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤400
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers k
#  and x
#  (1≤k,x≤20
# ).
#
# Output
# For each test case, print any possible initial value on a new line. It can be shown that the answer always exists.
#
# Example
# InputCopy
# 3
# 1 4
# 1 5
# 5 4
# OutputCopy
# 1
# 10
# 21
# Note
# In the first test case, since 1
#  is odd, performing the procedure k=1
#  times results in 1⋅3+1=4
# , so 1
#  is a valid output.
#
# In the second test case, since 10
#  is even, performing the procedure k=1
#  times results in 102=5
# , so 10
#  is a valid output.
#
# The third test case is explained in the statement.
# Solution
# C++ O(K) O(1) Greedy
#include <iostream>


void solution() {
    int n, k;
    std::cin >> k >> n;
    for (size_t i = 0; i < k; ++i) {
        if ((n - 1) % 3 == 0) {
            int cand = (n - 1) / 3;
            if (cand & 1) {
                n = cand;
                continue;
            }
        }
        n <<= 1;
    }
    std::cout << n << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(K) O(1) Greedy
import sys


def solution() -> None:
    k, n = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(k):
        if (n - 1) % 3 == 0 and (n - 1) // 3 & 1: n = (n - 1) // 3
        else: n <<= 1
    sys.stdout.write('{}\n'.format(n))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()