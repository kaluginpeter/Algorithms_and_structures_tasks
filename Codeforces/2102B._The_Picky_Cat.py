# B. The Picky Cat
# time limit per test1 second
# memory limit per test256 megabytes
#
# You are given an array of integers a1,a2,…,an
# . You are allowed to do the following operation any number of times (possibly zero):
#
# Choose an index i
#  (1≤i≤n
# ). Multiply ai
#  by −1
#  (i.e., update ai:=−ai
# ).
# Your task is to determine whether it is possible to make the element at index 1
#  become the median of the array after doing the above operation any number of times. Note that operations can be applied to index 1
#  as well, meaning the median can be either the original value of a1
#  or its negation.
#
# The median of an array b1,b2,…,bm
#  is defined as the ⌈m2⌉
# -th∗
#  smallest element of array b
# . For example, the median of the array [3,1,2]
#  is 2
# , while the median of the array [10,1,8,3]
#  is 3
# .
#
# It is guaranteed that the absolute value of the elements of a
#  are distinct. Formally, there are no pairs of indices 1≤i<j≤n
#  where |ai|=|aj|
# .
#
# ∗
# ⌈x⌉
#  is the ceiling function which returns the least integer greater than or equal to x
# .
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ) — the length of the array a
# .
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (|ai|≤106
# , |ai|≠|aj|
# ) — the elements of the array a
# .
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 105
# .
#
# Output
# For each testcase, output "YES" if it is possible to make the element at index 1
#  become the median of the array, and "NO" otherwise.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 7
# 3
# 2 3 1
# 5
# 1 2 3 4 5
# 4
# 4 2 0 -5
# 4
# -5 0 4 3
# 4
# -10 8 3 2
# 1
# 1
# 10
# 9 1000 -999 -13 456 -223 23 24 10 0
# OutputCopy
# YES
# YES
# YES
# NO
# NO
# YES
# YES
# Note
# In the first test case, a1=2
#  is already the median of the array a=[2,3,1]
# , so no operation is required.
#
# In the second test case, we can do two operations: one on index 2
# , and one on index 5
# . The array becomes [1,−2,3,4,−5]
# , which has a median of 1
# .
#
# In the third test case, if you do an operation on index 1
# , the array will become [−4,2,0,−5]
# , which has a median of −4
# .
#
# In the fourth test case, it can be proven that no sequence of operations can make the median of the array become 5
#  or −5
# .
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>
#include <cmath>

bool simulate(std::vector<int> &nums) {
    int less = 0, extraLess = 0;
    for (int i = 1; i < nums.size(); ++i) {
        if (std::abs(nums[i]) < nums[0]) ++less;
        else if (-std::abs(nums[i]) < nums[0]) ++extraLess;
    }
    int target = nums.size() / 2;
    if (nums.size() & 1) ++target;
    --target;
    return (less + extraLess) >= target && less <= target;
}


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    if (n <= 2) {
        std::cout << "YES\n";
        return;
    }
    bool first = simulate(nums);
    nums[0] *= -1;
    bool second = simulate(nums);
    std::cout << (first || second ? "YES" : "NO") << std::endl;

}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def simulate(nums: list[int]) -> bool:
    less: int = 0
    extra: int = 0
    for i in range(1, len(nums)):
        if abs(nums[i]) < nums[0]: less += 1
        elif -abs(nums[i]) < nums[0]: extra += 1
    target: int = len(nums) // 2
    if len(nums) & 1: target += 1
    target -= 1
    return less <= target and less + extra >= target


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    first: bool = simulate(nums)
    nums[0] *= -1
    second: bool = simulate(nums)
    sys.stdout.write('{}\n'.format('YES' if (first or second) else 'NO'))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()