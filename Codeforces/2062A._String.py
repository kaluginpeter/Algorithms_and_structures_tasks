# A. String
# time limit per test1 second
# memory limit per test512 megabytes
# You are given a string s
#  of length n
#  consisting of 0
#  and/or 1
# . In one operation, you can select a non-empty subsequence t
#  from s
#  such that any two adjacent characters in t
#  are different. Then, you flip each character of t
#  (0
#  becomes 1
#  and 1
#  becomes 0
# ). For example, if s=0––0101––––
#  and t=s1s3s4s5=0101
# , after the operation, s
#  becomes 1––0010––––
# .
#
# Calculate the minimum number of operations required to change all characters in s
#  to 0
# .
#
# Recall that for a string s=s1s2…sn
# , any string t=si1si2…sik
#  (k≥1
# ) where 1≤i1<i2<…<ik≤n
#  is a subsequence of s
# .
#
# Input
# The first line of input contains a single integer t
#  (1≤t≤104
# ) — the number of input test cases.
#
# The only line of each test case contains the string s
#  (1≤|s|≤50
# ), where |s|
#  represents the length of s
# .
#
# Output
# For each test case, output the minimum number of operations required to change all characters in s
#  to 0
# .
#
# Example
# InputCopy
# 5
# 1
# 000
# 1001
# 10101
# 01100101011101
# OutputCopy
# 1
# 0
# 2
# 3
# 8
# Note
# In the first test case, you can flip s1
# . Then s
#  becomes 0
# , so the answer is 1
# .
#
# In the fourth test case, you can perform the following three operations in order:
#
# Flip s1s2s3s4s5
# . Then s
#  becomes 01010––––––
# .
# Flip s2s3s4
# . Then s
#  becomes 0010––––0
# .
# Flip s3
# . Then s
#  becomes 000––00
# .
# It can be shown that you can not change all characters in s
#  to 0
#  in less than three operations, so the answer is 3
# .
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <string>

void solution() {
    std::string sequence;
    std::cin >> sequence;
    int ones = 0;
    for (int i = 0; i < sequence.size(); ++i) {
        if (sequence[i] == '1') ++ones;
    }
    std::cout << ones << std::endl;

}

int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    sequence: str = sys.stdin.readline().rstrip()
    sys.stdout.write('{}\n'.format(sequence.count('1')))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()