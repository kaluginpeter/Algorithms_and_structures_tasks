# B. Merging the Sets
# time limit per test1 second
# memory limit per test256 megabytes
# You are given n
#  sets S1,S2,…,Sn
# , where each element in the sets is an integer between 1
#  and m
# .
#
# You want to choose some of the sets (possibly none or all), such that every integer between 1
#  and m
#  is included in at least one of the chosen sets.
#
# You have to determine whether there exist at least three ways to choose the sets.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and m
#  (2≤n≤5⋅104
# , 1≤m≤105
# ) — the number of sets and the upper bound of the integers in the sets.
#
# Then n
#  lines follow, the i
# -th line first containing an integer li
#  (1≤li≤m
# ) — the size of set Si
# .
#
# Then li
#  integers Si,1,Si,2,…,Si,li
#  follow in the same line (1≤Si,1<Si,2<⋯<Si,li≤m
# ) — the elements of set Si
# .
#
# Let L=∑i=1nli
# . It is guaranteed that:
#
# The sum of n
#  over all test cases does not exceed 5⋅104
# ;
# The sum of m
#  over all test cases does not exceed 105
# ;
# The sum of L
#  over all test cases does not exceed 2⋅105
# .
# Output
# For each test case, print "YES" if there exist at least three ways to choose the sets. Otherwise, print "NO".
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 6
# 3 2
# 2 1 2
# 1 1
# 1 2
# 4 10
# 3 1 2 3
# 2 4 5
# 1 6
# 4 7 8 9 10
# 2 5
# 4 1 2 3 4
# 4 1 2 3 4
# 5 5
# 5 1 2 3 4 5
# 5 1 2 3 4 5
# 5 1 2 3 4 5
# 5 1 2 3 4 5
# 5 1 2 3 4 5
# 5 10
# 4 1 2 3 4
# 5 1 2 5 6 7
# 5 2 6 7 8 9
# 4 6 7 8 9
# 2 9 10
# 5 5
# 1 1
# 1 2
# 1 3
# 2 4 5
# 1 5
# OutputCopy
# YES
# NO
# NO
# YES
# YES
# NO
# Note
# In the first test case, there are 5≥3
#  possible ways to choose the sets:
#
# S1
#  — both 1
#  and 2
#  are included in S1
# ;
# S1
#  and S2
#  — 1
#  is included in S1
#  and S2
# , and 2
#  is included in S1
# ;
# S1
#  and S3
#  — 1
#  is included in S1
# , and 2
#  is included in S1
#  and S3
# ;
# S2
#  and S3
#  — 1
#  is included in S2
# , and 2
#  is included in S3
# ;
# S1
# , S2
# , and S3
#  — 1
#  is included in S1
#  and S2
# , and 2
#  is included in S1
#  and S3
# .
# Note that it is invalid to choose S2
#  only because 2
#  is not included in S2
# .
#
# In the second test case, the only way is to choose all the sets.
#
# In the third test case, 5
#  does not appear in any of the sets, so there is no way to choose the sets.
#
# In the fourth test case, choosing any non-empty collection of the sets is valid, so the number of ways is 25−1=31≥3
# .
# Solution
# C++ O(NL) O(N + M) HashMap
#include <iostream>
#include <vector>
#include <unordered_set>


void solution() {
    size_t n, m;
    std::cin >> n >> m;
    std::vector<int> hashmap(m + 1, 0);
    std::vector<std::vector<int>> inTake(n, std::vector<int>());
    for (size_t i = 0; i < n; ++i) {
        int k;
        std::cin >> k;
        inTake[i].resize(k);
        for (size_t j = 0; j < k; ++j) {
            std::cin >> inTake[i][j];
            ++hashmap[inTake[i][j]];
        }
    }
    for (size_t i = 1; i <= m; ++i) {
        if (!hashmap[i]) {
            std::cout << "NO\n";
            return;
        }
    }
    int uniq = 0;
    for (size_t i = 0; i < n; ++i) {
        bool isValid = true;
        for (int& num : inTake[i]) {
            if (hashmap[num] == 1) {
                isValid = false;
                break;
            }
        }
        if (isValid) {
            ++uniq;
            if (uniq == 2) break;
        }
    }
    std::cout << (uniq > 1 ? "YES" : "NO") << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NL) O(N + M) HashMap
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    hashmap: list[int] = [0] * (m + 1)
    in_take: list[list[int]] = [[] for _ in range(n)]
    for i in range(n):
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        k: int = next(nums)
        for _ in range(k):
            x: int = next(nums)
            in_take[i].append(x)
            hashmap[x] += 1
    if not min(hashmap[1:]):
        sys.stdout.write('NO\n')
        return
    uniq: int = 0
    for i in range(n):
        if all(hashmap[num] > 1 for num in in_take[i]): uniq += 1
        if uniq == 2: break
    sys.stdout.write('{}\n'.format(['NO', 'YES'][uniq == 2]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()