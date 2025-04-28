# A. Doremy's Paint 3
# time limit per test1 second
# memory limit per test256 megabytes
# An array b1,b2,…,bn
#  of positive integers is good if all the sums of two adjacent elements are equal to the same value. More formally, the array is good if there exists a k
#  such that b1+b2=b2+b3=…=bn−1+bn=k
# .
#
# Doremy has an array a
#  of length n
# . Now Doremy can permute its elements (change their order) however she wants. Determine if she can make the array good.
#
# Input
# The input consists of multiple test cases. The first line contains a single integer t
#  (1≤t≤100
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤100
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤105
# ).
#
# There are no constraints on the sum of n
#  over all test cases.
#
# Output
# For each test case, print "Yes" (without quotes), if it is possible to make the array good, and "No" (without quotes) otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 2
# 8 9
# 3
# 1 1 2
# 4
# 1 1 4 5
# 5
# 2 3 3 3 3
# 4
# 100000 100000 100000 100000
# OutputCopy
# Yes
# Yes
# No
# No
# Yes
# Note
# In the first test case, [8,9]
#  and [9,8]
#  are good.
#
# In the second test case, [1,2,1]
#  is good because a1+a2=a2+a3=3
# .
#
#
# Solution
# C++ O(N) O(N) HashMap
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;


void solution() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }
        unordered_map<int, int> cnt;
        for (int num : a) {
            cnt[num]++;
        }
        if (cnt.size() > 2) {
            cout << "No" << endl;
        } else if (cnt.size() == 1) {
            cout << "Yes" << endl;
        } else {
            auto it = cnt.begin();
            int a_count = it->second;
            ++it;
            int b_count = it->second;
            if (n % 2 == 0) {
                if (a_count == b_count) {
                    cout << "Yes" << endl;
                } else {
                    cout << "No" << endl;
                }
            } else {
                int high = (n + 1) / 2;
                int low = (n - 1) / 2;
                if ((a_count == high && b_count == low) || (a_count == low && b_count == high)) {
                    cout << "Yes" << endl;
                } else {
                    cout << "No" << endl;
                }
            }
        }
    }
}


int main() {
    solution();
}

# Python O(N) O(N) HashMap
from collections import Counter
import sys


def solution() -> None:
    t = int(sys.stdin.readline())
    for _ in range(t):
        n: int = int(sys.stdin.readline())
        a: list[int] = list(map(int, sys.stdin.readline().split()))
        cnt: dict[int, int] = Counter(a)
        if len(cnt) > 2: sys.stdout.write('NO\n')
        elif len(cnt) == 1: sys.stdout.write('YES\n')
        else:
            counts: list[int] = list(cnt.values())
            a_count, b_count = counts[0], counts[1]
            if n % 2 == 0:
                if a_count == b_count: sys.stdout.write('YES\n')
                else: sys.stdout.write('NO\n')
            else:
                high: int = (n + 1) // 2
                low: int = (n - 1) // 2
                if (a_count == high and b_count == low) or (a_count == low and b_count == high):
                    sys.stdout.write('YES\n')
                else: sys.stdout.write('NO\n')

if __name__ == '__main__':
    solution()
