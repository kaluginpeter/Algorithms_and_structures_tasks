# D. Tung Tung Sahur
# time limit per test2 seconds
# memory limit per test256 megabytes
# You have two drums in front of you: a left drum and a right drum. A hit on the left can be recorded as "L", and a hit on the right as "R".
#
# The strange forces that rule this world are fickle: sometimes, a blow sounds once, and sometimes it sounds twice. Therefore, a hit on the left drum could have sounded as either "L" or "LL", and a hit on the right drum could have sounded as either "R" or "RR".
#
# The sequence of hits made is recorded in the string p
# , and the sounds heard are in the string s
# . Given p
#  and s
# , determine whether it is true that the string s
#  could have been the result of the hits from the string p
# .
#
# For example, if p=
# "LR", then the result of the hits could be any of the strings "LR", "LRR", "LLR", and "LLRR", but the strings "LLLR" or "LRL" cannot.
#
# Input
# The first line contains an integer t
#  (1≤t≤104
# ) – the number of independent test cases.
#
# The first line of each test case contains the string p
#  (1≤|p|≤2⋅105
# ) consisting only of the characters "R" and "L", where |p|
#  denotes the length of the string p
# .
#
# The second line of each test case contains the string s
#  (1≤|p|≤|s|≤2⋅105
# ) consisting only of the characters "R" and "L".
#
# It is guaranteed that the sum of |s|
#  does not exceed 2⋅105
#  across all test cases.
#
# Output
# For each set of input data, output "YES" if s
#  can be the heard sound, and "NO" otherwise. You may output in any case.
#
# Example
# InputCopy
# 5
# R
# RR
# LRLR
# LRLR
# LR
# LLLR
# LLLLLRL
# LLLLRRLL
# LLRLRLRRL
# LLLRLRRLLRRRL
# OutputCopy
# YES
# YES
# NO
# NO
# YES
# Solution
# C++ O(min(N,M)) O(1) TwoPointers
#include <iostream>
#include <string>


void solution() {
    std::string p, s;
    std::cin >> p >> s;
    int leftP = 0, leftS = 0;
    while (leftP < p.size() && leftS < s.size()) {
        int rightP = leftP;
        while (rightP < p.size() && p[leftP] == p[rightP]) ++rightP;
        int extra = 2 * (rightP - leftP);
        int rightS = leftS;
        while (rightS < s.size() && s[leftS] == s[rightS]) ++rightS;
        if ((p[leftP] != s[leftS]) || (rightS - leftS < rightP - leftP) || (rightS - leftS > 2 * (rightP - leftP))) {
            std::cout << "NO\n";
            return;
        }
        leftP = rightP;
        leftS = rightS;
    }
    std::cout << (leftS == s.size() && leftP == p.size()? "YES" : "NO") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(min(N, M)) O(1) TwoPointers
import sys


def solution() -> None:
    p: str = sys.stdin.readline().rstrip()
    s: str = sys.stdin.readline().rstrip()
    left_p: int = 0
    left_s: int = 0
    while left_p < len(p) and left_s < len(s):
        right_p: int = left_p
        while right_p < len(p) and p[left_p] == p[right_p]: right_p += 1
        extra: int = 2 * (right_p - left_p)
        right_s: int = left_s
        while right_s < len(s) and s[left_s] == s[right_s]: right_s += 1
        if (p[left_p] != s[left_s]) or (right_s - left_s < right_p - left_p) or (right_s - left_s > extra):
            sys.stdout.write('NO\n')
            return
        left_p = right_p
        left_s = right_s
    sys.stdout.write('{}\n'.format(['NO', 'YES'][left_s == len(s) and left_p == len(p)]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()