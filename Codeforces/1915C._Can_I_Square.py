# C. Can I Square?
# time limit per test1 second
# memory limit per test256 megabytes
# Calin has n
#  buckets, the i
# -th of which contains ai
#  wooden squares of side length 1
# .
#
# Can Calin build a square using all the given squares?
#
# Input
# The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤2⋅105
# ) — the number of buckets.
#
# The second line of each test case contains n
#  integers a1,…,an
#  (1≤ai≤109
# ) — the number of squares in each bucket.
#
# The sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if Calin can build a square using all of the given 1×1
#  squares, and "NO" otherwise.
#
# You can output the answer in any case (for example, the strings "yEs", "yes", "Yes" and "YES" will be recognized as a positive answer).
#
# Example
# InputCopy
# 5
# 1
# 9
# 2
# 14 2
# 7
# 1 2 3 4 5 6 7
# 6
# 1 3 5 7 9 11
# 4
# 2 2 2 2
# OutputCopy
# YES
# YES
# NO
# YES
# NO
# Note
# In the first test case, Calin can build a 3×3
#  square.
#
# In the second test case, Calin can build a 4×4
#  square.
#
# In the third test case, Calin cannot build a square using all the given squares.
# Solution
# C++ O(logN) O(1) Math
#include <iostream>
#include <cmath>


void solution(int t) {
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        long long sum = 0;
        for (int j = 0; j < n; ++j) {
            int square;
            std::cin >> square;
            sum += square;
        }
        long long corner = static_cast<long long>(std::sqrt(sum));
        std::cout << (corner * corner == sum? "YES" : "NO") << "\n";
    }
}

int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(logN) O(1) Math
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sm: int = sum(map(int, sys.stdin.readline().rstrip().split()))
        corner: int = int(sm**.5)
        sys.stdout.write(['NO', 'YES'][corner * corner == sm] + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)
