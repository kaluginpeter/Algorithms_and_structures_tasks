# B. Above the Clouds
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given a string s
#  of length n
# , consisting of lowercase letters of the Latin alphabet. Determine whether there exist three non-empty strings a
# , b
# , and c
#  such that:
#
# a+b+c=s
# , meaning the concatenation∗
#  of strings a
# , b
# , and c
#  equals s
# .
# The string b
#  is a substring†
#  of the string a+c
# , which is the concatenation of strings a
#  and c
# .
# ∗
# Concatenation of strings a
#  and b
#  is defined as the string a+b=a1a2…apb1b2…bq
# , where p
#  and q
#  are the lengths of strings a
#  and b
# , respectively. For example, the concatenation of the strings "code" and "forces" is "codeforces".
#
# †
# A string a
#  is a substring of a string b
#  if a
#  can be obtained from b
#  by the deletion of several (possibly, zero or all) characters from the beginning and several (possibly, zero or all) characters from the end.
#
# Input
# Each test consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (3≤n≤105
# ) — the length of the string s
# .
#
# The second line of each test case contains the string s
#  of length n
# , consisting of lowercase letters of the Latin alphabet.
#
# It is guaranteed that the sum of n
#  across all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "Yes" if there exist three non-empty strings a
# , b
# , and c
#  that satisfy the conditions, and "No" otherwise.
#
# You may output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive answers.
#
# Example
# InputCopy
# 12
# 3
# aaa
# 3
# aba
# 3
# aab
# 4
# abca
# 4
# abba
# 4
# aabb
# 5
# abaca
# 5
# abcda
# 5
# abcba
# 6
# abcbbf
# 6
# abcdaa
# 3
# abb
# OutputCopy
# Yes
# No
# Yes
# No
# Yes
# Yes
# Yes
# No
# Yes
# Yes
# Yes
# Yes
# Note
# In the first test case, there exist unique non-empty strings a
# , b
# , and c
#  such that a+b+c=s
# . These are the strings a=
#  "a", b=
#  "a", and c=
#  "a". The concatenation of strings a
#  and c
#  equals a+c=
#  "aa". The string b
#  is a substring of this string.
#
# In the sixth test case, one can choose a=
#  "a", b=
#  "ab", and c=
#  "b". The concatenation of strings a
#  and c
#  equals a+c=
#  "ab". The string b
#  is a substring of this string.
#
# In the seventh test case, one can choose a=
#  "ab", b=
#  "a", and c=
#  "ca". The concatenation of strings a
#  and c
#  equals a+c=
#  "abca". The string b
#  is a substring of this string.
# Solution
# C++ O(N) O(1) Greedy HashMap
#include <iostream>
#include <string>
#include <vector>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::string sequence;
        std::cin >> sequence;
        std::vector<int> hashmap(26, 0);
        bool isValid = false;
        for (int j = 0; j < n; ++j) {
            if (hashmap[sequence[j] - 'a'] && j + 1 < n) {
                isValid = true;
                break;
            }
            ++hashmap[sequence[j] - 'a'];
        }
        hashmap = std::vector<int>(26, 0);
        for (int j = n - 1; j >= 0; --j) {
            if (hashmap[sequence[j] - 'a'] && j) {
                isValid = true;
                break;
            }
            ++hashmap[sequence[j] - 'a'];
        }
        std::cout << (isValid ? "YES" : "NO") << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy HashMap
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        sequence: str = sys.stdin.readline().rstrip()
        is_valid: bool = False
        hashmap: list[int] = [0] * 26
        for j in range(n):
            if hashmap[ord(sequence[j]) - 97] and j + 1 < n:
                is_valid = True
                break
            hashmap[ord(sequence[j]) - 97] += 1
        hashmap = [0] * 26
        for j in range(n - 1, -1, -1):
            if hashmap[ord(sequence[j]) - 97] and j:
                is_valid = True
                break
            hashmap[ord(sequence[j]) - 97] += 1
        sys.stdout.write('{}\n'.format(['NO', 'YES'][is_valid]))


if __name__ == '__main__':
    solution()