# A. Common Multiple
# time limit per test1 second
# memory limit per test256 megabytes
#
# You are given an array of integers a1,a2,…,an
# . An array x1,x2,…,xm
#  is beautiful if there exists an array y1,y2,…,ym
#  such that the elements of y
#  are distinct (in other words, yi≠yj
#  for all 1≤i<j≤m
# ), and the product of xi
#  and yi
#  is the same for all 1≤i≤m
#  (in other words, xi⋅yi=xj⋅yj
#  for all 1≤i<j≤m
# ).
#
# Your task is to determine the maximum size of a subsequence∗
#  of array a
#  that is beautiful.
#
# ∗
# A sequence b
#  is a subsequence of a sequence a
#  if b
#  can be obtained from a
#  by the deletion of several (possibly, zero or all) element from arbitrary positions.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤n
# ) — the elements of array a
# .
#
# Note that there are no constraints on the sum of n
#  over all test cases.
#
# Output
# For each test case, output the maximum size of a subsequence of array a
#  that is beautiful.
#
# Example
# InputCopy
# 3
# 3
# 1 2 3
# 5
# 3 1 4 1 5
# 1
# 1
# OutputCopy
# 3
# 4
# 1
# Note
# In the first test case, the entire array a=[1,2,3]
#  is already beautiful. A possible array y
#  is [6,3,2]
# , which is valid since the elements of y
#  are distinct, and 1⋅6=2⋅3=3⋅2
# .
#
# In the second test case, the subsequence [3,1,4,5]
#  is beautiful. A possible array y
#  is [20,60,15,12]
# . It can be proven that the entire array a=[3,1,4,1,5]
#  is not beautiful, so the maximum size of a subsequence of array a
#  that is beautiful is 4
# .
# Solution
# C++ O(N) O(D) HashSet
#include <iostream>
#include <set>
using namespace std;

void solution() {
    int t;
    cin >> t;
    for (int j = 0; j < t; ++j) {
        int n;
        cin >> n;
        set<int> s;
        for (int i = 0; i < n; i++) {
            int a;
            cin >> a;
            s.insert(a);
        }
        cout << s.size() << '\n';
    }
}

int main() {
    solution();
}

# Python O(N) O(D) HashSet
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: set[int] = set(map(int, sys.stdin.readline().rstrip().split()))
        sys.stdout.write('{}\n'.format(len(nums)))


if __name__ == '__main__':
    solution()