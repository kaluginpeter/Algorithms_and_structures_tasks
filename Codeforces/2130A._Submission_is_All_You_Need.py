# A. Submission is All You Need
# time limit per test1 second
# memory limit per test256 megabytes
# For a multiset T
#  consisting of non-negative integers, we define:
#
# sum(T)
#  is the sum of all elements in T
# . For example, if T={0,1,1,3}
# , then sum(T)=0+1+1+3=5
# .
#
# mex(T)
#  is the smallest non-negative integer not in T
# . For example, if T={0,1,1,3}
# , then mex(T)=2
#  because 2
#  is the smallest non-negative integer not present in T
# .
# You are given a multiset S
#  of size n
#  consisting of non-negative integers. At first, your score is 0
# . You can perform the following operations any number of times in any order (possibly zero):
# Select a subset S′⊆S
#  (i.e., S′
#  contains some of the elements currently in S
# ), add sum(S′)
#  to your score, and then remove S′
#  from S
# .
# Select a subset S′⊆S
# , add mex(S′)
#  to your score, and then remove S′
#  from S
# .
# Find the maximum possible score that can be obtained.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤103
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤50
# ).
#
# The second line of each test case contains n
#  integers S1,S2,…,Sn
#  (0≤Si≤50
# ).
#
# Output
# For each test case, print a single integer — the maximum possible score that can be obtained.
#
# Example
# InputCopy
# 2
# 3
# 0 1 1
# 3
# 1 2 3
# OutputCopy
# 3
# 6
# Note
# In the first test case, a possible optimal strategy is as follows:
#
# Select S′={0,1}
# , add mex(S′)=mex({0,1})=2
#  to your score, and then remove S′
#  from S
# . Currently, your score is 2
#  and S={1}
# .
# Select S′={1}
# , add sum(S′)=sum({1})=1
#  to your score, and then remove S′
#  from S
# . Currently, your score is 3
#  and S=∅
# .
# After that, you cannot do any further operations. It can be proven that 3
#  is the maximum possible score that can be obtained.
# Solution
# C++ O(N) O(D) HashMap
#include <iostream>
#include <vector>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> hashmap(51, 0);
    int output = 0;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        output += x;
        ++hashmap[x];
    }
    output += hashmap[0];
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy Math
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write('{}\n'.format(sum(nums) + nums.count(0)))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()