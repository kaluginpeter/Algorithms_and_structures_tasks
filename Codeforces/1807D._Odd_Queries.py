# D. Odd Queries
# time limit per test2 seconds
# memory limit per test256 megabytes
# You have an array a1,a2,…,an
# . Answer q
#  queries of the following form:
#
# If we change all elements in the range al,al+1,…,ar
#  of the array to k
# , will the sum of the entire array be odd?
# Note that queries are independent and do not affect future queries.
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case consists of 2
#  integers n
#  and q
#  (1≤n≤2⋅105
# ; 1≤q≤2⋅105
# ) — the length of the array and the number of queries.
#
# The second line of each test case consists of n
#  integers ai
#  (1≤ai≤109
# ) — the array a
# .
#
# The next q
#  lines of each test case consists of 3
#  integers l,r,k
#  (1≤l≤r≤n
# ; 1≤k≤109
# ) — the queries.
#
# It is guaranteed that the sum of n
#  over all test cases doesn't exceed 2⋅105
# , and the sum of q
#  doesn't exceed 2⋅105
# .
#
# Output
# For each query, output "YES" if the sum of the entire array becomes odd, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 2
# 5 5
# 2 2 1 3 2
# 2 3 3
# 2 3 4
# 1 5 5
# 1 4 9
# 2 4 3
# 10 5
# 1 1 1 1 1 1 1 1 1 1
# 3 8 13
# 2 5 10
# 3 8 10
# 1 10 2
# 1 9 100
# OutputCopy
# YES
# YES
# YES
# NO
# YES
# NO
# NO
# NO
# NO
# YES
# Note
# For the first test case:
#
# If the elements in the range (2,3)
#  would get set to 3
#  the array would become {2,3,3,3,2}
# , the sum would be 2+3+3+3+2=13
#  which is odd, so the answer is "YES".
# If the elements in the range (2,3)
#  would get set to 4
#  the array would become {2,4,4,3,2}
# , the sum would be 2+4+4+3+2=15
#  which is odd, so the answer is "YES".
# If the elements in the range (1,5)
#  would get set to 5
#  the array would become {5,5,5,5,5}
# , the sum would be 5+5+5+5+5=25
#  which is odd, so the answer is "YES".
# If the elements in the range (1,4)
#  would get set to 9
#  the array would become {9,9,9,9,2}
# , the sum would be 9+9+9+9+2=38
#  which is even, so the answer is "NO".
# If the elements in the range (2,4)
#  would get set to 3
#  the array would become {2,3,3,3,2}
# , the sum would be 2+3+3+3+2=13
#  which is odd, so the answer is "YES".
# Solution
# C++ O(N + Q) O(N) PrefixSum
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, q;
        std::scanf("%d %d", &n, &q);
        std::vector<long long> prefixSum = {0};
        for (int j = 0; j < n; ++j) {
            long long num;
            std::cin >> num;
            prefixSum.push_back(prefixSum.back() + num);
        }
        for (int j = 0; j < q; ++j) {
            int left, right, k;
            std::scanf("%d %d %d", &left, &right, &k);
            long long extra = (right - left + 1) * k;
            long long subtract = prefixSum[right] - prefixSum[left - 1];
            std::cout << ((prefixSum[n] - subtract + extra) % 2 != 0? "YES" : "NO") << "\n";
        }
    }
}


int main() {
    solution();
}

# Python O(N + Q) O(N) PrefixSum
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, q = map(int, sys.stdin.readline().rstrip().split())
        nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
        prefix_sum: list[int] = [0]
        for _ in range(n):
            prefix_sum.append(prefix_sum[-1] + next(nums))
        for _ in range(q):
            left, right, k = map(int, sys.stdin.readline().rstrip().split())
            extra: int = (right - left + 1) * k
            subtract: int = prefix_sum[right] - prefix_sum[left - 1]
            sys.stdout.write(['NO', 'YES'][(prefix_sum[n] - subtract + extra) & 1] + '\n')


if __name__ == '__main__':
    solution()