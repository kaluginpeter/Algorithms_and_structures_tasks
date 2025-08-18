# C. Make it Equal
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given two multisets S
#  and T
#  of size n
#  and a positive integer k
# , you may perform the following operations any number (including zero) of times on S
# :
#
# Select an element x
#  in S
# , and remove one occurrence of x
#  in S
# . Then, either insert x+k
#  into S
# , or insert |x−k|
#  into S
# .
# Determine if it is possible to make S
#  equal to T
# . Two multisets S
#  and T
#  are equal if every element appears the same number of times in S
#  and T
# .
#
# Input
# Each test contains multiple test cases. The first line contains an integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line contains two integers n
#  and k
#  (1≤n≤2⋅105
# , 1≤k≤109
# ) — the size of S
#  and the constant, respectively.
#
# The second line contains n
#  integers S1,S2,…,Sn
#  (0≤Si≤109
# ) — the elements in S
# .
#
# The third line contains n
#  integers T1,T2,…,Tn
#  (0≤Ti≤109
# ) — the elements in T
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output "YES" if it is possible to make S
#  equal to T
# , and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 5
# 1 3
# 1
# 2
# 1 8
# 4
# 12
# 3 5
# 6 2 9
# 8 4 11
# 2 7
# 2 8
# 2 9
# 3 2
# 0 1 0
# 1 0 1
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# Note
# In the first test case, we can remove one occurrence of 1
#  from S
#  and insert |1−k|=|1−3|=2
#  into S
# , making S
#  equal to T
# .
#
# In the second test case, we can remove one occurrence of 4
#  from S
#  and insert 4+k=4+8=12
#  into S
# , making S
#  equal to T
# .
#
# In the last test case, we can show that it is impossible to make S
#  equal to T
# .
# Solution
# C++ O(NlogN + MlogM) O(N + M) Map Math // Need to use map to avoid tle on hash collision tests
#include <iostream>
#include <map>
#include <vector>
#include <cmath>


void solution() {
    int n, k;
    std::cin >> n >> k;
    std::map<int, int> have, needed;
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        ++have[x];
    }
    for (int i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (!have.count(x)) ++needed[x % k];
        else {
            --have[x];
            if (!have[x]) have.erase(x);
        }
    }
    for (const auto &p : have) {
        int first = p.first % k, second = std::abs(p.first % k - k);
        int times = p.second;
        if (needed.count(first)) {
            int steps = std::min(times, needed[first]);
            times -= steps;
            needed[first] -= steps;
            if (!needed[first]) needed.erase(first);
        }
        if (needed.count(second)) {
            int steps = std::min(times, needed[second]);
            times -= steps;
            needed[second] -= steps;
            if (!needed[second]) needed.erase(second);
        }
        if (times) {
            std::cout << "NO\n";
            return;
        }
    }
    std::cout << (needed.empty() ? "YES" : "NO") << std::endl;
}


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N + M) O(N + M) Map Math // amortized O(1)* get TLE
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    have: dict[int, int] = dict()
    needed: dict[int, int] = dict()
    for _ in range(n):
        x: int = next(nums)
        have[x] = have.get(x, 0) + 1
    nums = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(n):
        x: int = next(nums)
        if x in have:
            have[x] -= 1
            if not have[x]: del have[x]
        else: needed[x % k] = needed.get(x % k, 0) + 1
    for num, freq in have.items():
        if num % k in needed:
            steps: int = min(freq, needed[num % k])
            freq -= steps
            needed[num % k] -= steps
            if not needed[num % k]: del needed[num % k]
        if abs(num % k - k) in needed:
            steps: int = min(freq, needed[abs(num % k - k)])
            freq -= steps
            needed[abs(num % k - k)] -= steps
            if not needed[abs(num % k - k)]: del needed[abs(num % k - k)]
        if freq:
            sys.stdout.write('NO\n')
            return
    sys.stdout.write('{}\n'.format(['YES', 'NO'][len(needed)]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()