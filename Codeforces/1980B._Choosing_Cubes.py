# B. Choosing Cubes
# time limit per test1 second
# memory limit per test256 megabytes
# Dmitry has n
#  cubes, numbered from left to right from 1
#  to n
# . The cube with index f
#  is his favorite.
#
# Dmitry threw all the cubes on the table, and the i
# -th cube showed the value ai
#  (1≤ai≤100
# ). After that, he arranged the cubes in non-increasing order of their values, from largest to smallest. If two cubes show the same value, they can go in any order.
#
# After sorting, Dmitry removed the first k
#  cubes. Then he became interested in whether he removed his favorite cube (note that its position could have changed after sorting).
#
# For example, if n=5
# , f=2
# , a=[4,3,3,2,3]
#  (the favorite cube is highlighted in green), and k=2
# , the following could have happened:
#
# After sorting a=[4,3,3,3,2]
# , since the favorite cube ended up in the second position, it will be removed.
# After sorting a=[4,3,3,3,2]
# , since the favorite cube ended up in the third position, it will not be removed.
# Input
# The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases. Then follow the descriptions of the test cases.
#
# The first line of each test case description contains three integers n
# , f
# , and k
#  (1≤f,k≤n≤100
# ) — the number of cubes, the index of Dmitry's favorite cube, and the number of removed cubes, respectively.
#
# The second line of each test case description contains n
#  integers ai
#  (1≤ai≤100
# ) — the values shown on the cubes.
#
# Output
# For each test case, output one line — "YES" if the cube will be removed in all cases, "NO" if it will not be removed in any case, "MAYBE" if it may be either removed or left.
#
# You can output the answer in any case. For example, the strings "YES", "nO", "mAyBe" will be accepted as answers.
#
# Example
# InputCopy
# 12
# 5 2 2
# 4 3 3 2 3
# 5 5 3
# 4 2 1 3 5
# 5 5 2
# 5 2 4 1 3
# 5 5 5
# 1 2 5 4 3
# 5 5 4
# 3 1 2 4 5
# 5 5 5
# 4 3 2 1 5
# 6 5 3
# 1 2 3 1 2 3
# 10 1 1
# 1 1 1 1 1 1 1 1 1 1
# 1 1 1
# 42
# 5 2 3
# 2 2 1 1 2
# 2 1 1
# 2 1
# 5 3 1
# 3 3 2 3 2
# OutputCopy
# MAYBE
# YES
# NO
# YES
# YES
# YES
# MAYBE
# MAYBE
# YES
# YES
# YES
# NO
# Solution
# C++ O(N) O(1) Greedy Counting
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n, f, k;
        std::scanf("%d %d %d", &n, &f, &k);
        std::vector<int> nums (n, 0);
        for (int j = 0; j < n; ++j) {
            std::scanf("%d", &nums[j]);
        }
        int greaterThan = 0;
        int equal = 0;
        for (int j = 0; j < n; ++j) {
            if (j == f - 1) continue;
            else if (nums[j] > nums[f - 1]) ++greaterThan;
            else if (nums[j] == nums[f - 1]) ++equal;
        }
        if (greaterThan >= k) std::printf("NO\n");
        else if (greaterThan + equal >= k) std::printf("MAYBE\n");
        else std::printf("YES\n");
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy Counting
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, f, k = map(int, sys.stdin.readline().rstrip().split())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        greaterThan: int = sum(num > nums[f - 1] for num in nums)
        equal: int = sum(num == nums[f - 1] for num in nums) - 1
        if greaterThan >= k: sys.stdout.write('NO\n')
        elif greaterThan + equal >= k: sys.stdout.write('MAYBE\n')
        else: sys.stdout.write('YES\n')


if __name__ == '__main__':
    solution()