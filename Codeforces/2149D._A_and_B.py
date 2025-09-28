# D. A and B
# time limit per test2 seconds
# memory limit per test256 megabytes
# Given a string s
#  of length n
# , consisting only of the characters 'a' and 'b'.
#
# In one operation, you can choose a position i
#  (1≤i≤n−1
# ) and swap the neighboring characters si
#  and si+1
# .
#
# You need to perform the minimum number of operations to ensure that all characters of one type (either a
#  or b
# ) are located strictly together, forming exactly one continuous block.
#
# Characters of the other type can be positioned either before or after this block, forming two (possibly empty) blocks.
#
# Examples of valid final forms:
#
# 'aaabbbaaa' — all 'b's are located together (one block), 'a's can be both before and after this block;
# 'bbbaaaaaabbb' — all 'a's together, 'b's are at the edges of the string;
# 'aaaaabbbb' or 'bbbbaaaaa' — both types of characters form one continuous block each.
# You need to find the minimum number of described operations required to achieve the specified state.
#
# Input
# Each test consists of several test cases.
#
# The first line contains one integer t
#  (1≤t≤104
# ) — the number of test cases. The description of test cases follows.
#
# The first line of each test case contains one integer n
#  (1≤n≤2⋅105
# ) — the length of the string s
# .
#
# The second line contains the string s
#  of length n
# , consisting only of the characters 'a' and 'b'.
#
# It is guaranteed that the sum of the values of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output one integer — the minimum number of operations required for all characters of one of the two types to form a single continuous block.
#
# Example
# InputCopy
# 5
# 4
# abab
# 6
# bababa
# 7
# abababa
# 2
# ab
# 1
# b
# OutputCopy
# 1
# 2
# 2
# 0
# 0
# Note
# In the first test case, the initial string is 'abab':
#
# by swapping the neighboring characters at positions 2
#  and 3
# , we get the string 'aabb';
# or by swapping the characters at positions 1
#  and 2
# , we get the string 'baab'.
# In both cases, exactly one operation is performed, after which all letters of one type form a single block, so the minimum number of operations is 1
# .
# In the fifth input test case, the string consists of a single character 'b'. The single character already forms a continuous block, no swaps are needed, so the minimum number of operations is 0
# .
# Solution
# C++ O(MlogM + N) O(M) Sorting Math
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>


long long min_swaps(std::string s, char target) {
    std::vector<int> pos;
    for (int i = 0; i < (int)s.size(); ++i) {
        if (s[i] == target) pos.push_back(i);
    }
    int m = pos.size();
    if (m <= 1) return 0;
    std::vector<long long> diffs(m);
    for (int i = 0; i < m; ++i) {
        diffs[i] = pos[i] - i;
    }
    std::nth_element(diffs.begin(), diffs.begin() + m/2, diffs.end());
    long long median = diffs[m/2];
    long long ans = 0;
    for (long long d : diffs) ans += std::llabs(d - median);
    return ans;
}



void solution() {
    size_t n;
    std::cin >> n;
    std::string s;
    std::cin >> s;
    std::cout << std::min(min_swaps(s, 'a'), min_swaps(s, 'b')) << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(MlogM + N) O(M) Greedy Math
import sys


def solution(s: str, target: str) -> int:
    pos: list[int] = [i for i, ch in enumerate(s) if ch == target]
    m: int = len(pos)
    if m <= 1: return 0
    shifted: list[int] = [pos[i] - i for i in range(m)]
    shifted.sort()
    median: int = shifted[m // 2]
    return sum(abs(x - median) for x in shifted)


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        a: str = sys.stdin.readline().rstrip()
        sys.stdout.write('{}\n'.format(min(solution(a, 'a'), solution(a, 'b'))))