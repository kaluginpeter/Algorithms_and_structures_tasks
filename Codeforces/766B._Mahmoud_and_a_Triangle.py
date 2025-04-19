# B. Mahmoud and a Triangle
# time limit per test2 seconds
# memory limit per test256 megabytes
# Mahmoud has n line segments, the i-th of them has length ai. Ehab challenged him to use exactly 3 line segments to form a non-degenerate triangle. Mahmoud doesn't accept challenges unless he is sure he can win, so he asked you to tell him if he should accept the challenge. Given the lengths of the line segments, check if he can choose exactly 3 of them to form a non-degenerate triangle.
#
# Mahmoud should use exactly 3 line segments, he can't concatenate two line segments or change any length. A non-degenerate triangle is a triangle with positive area.
#
# Input
# The first line contains single integer n (3 ≤ n ≤ 105) — the number of line segments Mahmoud has.
#
# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 109) — the lengths of line segments Mahmoud has.
#
# Output
# In the only line print "YES" if he can choose exactly three line segments and form a non-degenerate triangle with them, and "NO" otherwise.
#
# Examples
# InputCopy
# 5
# 1 5 3 2 4
# OutputCopy
# YES
# InputCopy
# 3
# 4 1 2
# OutputCopy
# NO
# Note
# For the first example, he can use line segments with lengths 2, 4 and 5 to form a non-degenerate triangle.
# Solution
# C++ O(NlogN) O(1) Greedy Geometry
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n;
    std::scanf("%d", &n);
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::scanf("%d", &nums[i]);
    std::sort(nums.begin(), nums.end());
    bool isValid = false;
    for (int i = 0; i < n - 2; ++i) {
        if (static_cast<long long>(nums[i]) + nums[i + 1] > nums[i + 2]) {
            isValid = true;
            break;
        }
    }
    std::cout << (isValid? "YES" : "NO") << '\n';
}


int main() {
    solution();
}

# Python O(NlogN) O(1) Sorting Geometry
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    is_valid: bool = False
    for i in range(n - 2):
        if nums[i] + nums[i + 1] > nums[i + 2]:
            is_valid = True
            break
    sys.stdout.write('{}\n'.format(['NO', 'YES'][is_valid]))


if __name__ == '__main__':
    solution()