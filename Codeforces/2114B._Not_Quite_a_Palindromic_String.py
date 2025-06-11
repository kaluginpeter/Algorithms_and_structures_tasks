# B. Not Quite a Palindromic String
# time limit per test2 seconds
# memory limit per test256 megabytes
# Vlad found a binary string∗
#  s
#  of even length n
# . He considers a pair of indices (i,n−i+1
# ), where 1≤i<n−i+1
# , to be good if si=sn−i+1
#  holds true.
#
# For example, in the string '010001' there is only 1
#  good pair, since s1≠s6
# , s2≠s5
# , and s3=s4
# . In the string '0101' there are no good pairs.
#
# Vlad loves palindromes, but not too much, so he wants to rearrange some characters of the string so that there are exactly k
#  good pairs of indices.
#
# Determine whether it is possible to rearrange the characters in the given string so that there are exactly k
#  good pairs of indices (i,n−i+1
# ).
#
# ∗
# A string s
#  is called binary if it consists only of the characters '0' and '1'
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains two integers n
#  and k
#  (2≤n≤2⋅105
# , 0≤k≤n2
# , n
#  is even) — the length of the string and the required number of good pairs.
#
# The second line of each test case contains a binary string s
#  of length n
# .
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if there is a way to rearrange the characters of the string so that there are exactly k
#  good pairs, otherwise output "NO".
#
# You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 6
# 6 2
# 000000
# 2 1
# 01
# 4 1
# 1011
# 10 2
# 1101011001
# 10 1
# 1101011001
# 2 1
# 11
# OutputCopy
# NO
# NO
# YES
# NO
# YES
# YES
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>
#include <cmath>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, k;
        std::scanf("%d %d", &n, &k);
        std::string sequence;
        std::cin >> sequence;
        int ones = 0, zeros = 0;
        for (char &letter : sequence) {
            if (letter == '1') ++ones;
            else ++zeros;
        }
        if (zeros / 2 + ones / 2 < k) {
            std::cout << "NO\n";
            continue;
        }
        for (int j = 0; j < k; ++j) {
            if (ones > zeros) ones -= 2;
            else zeros -= 2;
        }
        std::cout << (ones - zeros == 0? "YES" : "NO") << "\n";
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
        n, k = map(int, sys.stdin.readline().rstrip().split())
        sequence: str = sys.stdin.readline().rstrip()
        zeros: int = 0
        ones: int = 0
        for letter in sequence:
            if letter == '1': ones += 1
            else: zeros += 1
        if ones // 2 + zeros // 2 < k:
            sys.stdout.write('NO\n')
            continue
        for i in range(k):
            if ones > zeros: ones -= 2
            else: zeros -= 2
        sys.stdout.write('{}\n'.format(['NO', 'YES'][zeros - ones == 0]))

if __name__ == '__main__':
    solution()