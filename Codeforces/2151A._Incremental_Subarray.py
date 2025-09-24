# A. Incremental Subarray
# time limit per test1 second
# memory limit per test256 megabytes
# Schtiffles - Marbl
# ⠀
# James is learning numbers, and he is having fun writing them on a huge blackboard, from left to right.
#
# At the beginning, James writes the number 1
# .
# Right after, James writes 1
#  again, and then 2
# .
# Then James writes 1
# , 2
# , 3
# .
# …
# In the end, James writes 1
# , 2
# , 3
# , …
# , n
# .
# For example, for n=5
# , the numbers written by James make the array b=[1,1,2,1,2,3,1,2,3,4,1,2,3,4,5]
# .
#
# James has a list of favorite numbers a1,a2,…,am
# , and he wants to calculate how many subarrays of the array b
#  are equal to a1,a2,…,am
# . ∗
#
# James is already sure that a1,a2,…,am
#  is a subarray of b
# , so the answer is at least 1
# .
#
# ∗
# The subarrays of an array [v1,v2,…,vk]
#  are generated as follows: for each l,r
#  such that 1≤l≤r≤k
# , the array [vl,vl+1,…,vr]
#  is a subarray. So there are k(k+1)/2
#  subarrays in total, and some of them may be equal.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and m
#  (1≤n≤105
# , 1≤m≤200
# ) — the maximum number written by James, and the length of the array a1,a2,…,am
# .
#
# The second line of each test case contains m
#  integers a1,a2,…,am
#  (1≤ai≤105
# ) — James' favorite numbers.
#
# It is guaranteed that for the given input, the answer is always at least 1
# .
#
# Note that there are no constraints on the sum of n
#  and m
#  over all test cases.
#
# Output
# For each test case, output a single line containing an integer: the number of subarrays of the array b
#  which are equal to a1,a2,…,am
# .
#
# Example
# InputCopy
# 5
# 4 1
# 1
# 5 3
# 1 2 3
# 6 6
# 3 1 2 3 4 1
# 100000 1
# 100000
# 4 2
# 1 1
# OutputCopy
# 4
# 3
# 1
# 1
# 1
# Note
# In the first test case, the blackboard contains the numbers
#
# b=[1,1,2,1,2,3,1,2,3,4]
#
# and James has only one favorite number: the number 1
# . There are 4
#  subarrays of b
#  equal to [1]
#  (highlighted in red):
#
# [1,1,2,1,2,3,1,2,3,4]
# ;
# [1,1,2,1,2,3,1,2,3,4]
# ;
# [1,1,2,1,2,3,1,2,3,4]
# ;
# [1,1,2,1,2,3,1,2,3,4]
# .
# In the second test case, the blackboard contains the numbers
#
# b=[1,1,2,1,2,3,1,2,3,4,1,2,3,4,5]
#
# and James's list of favorite numbers is [1,2,3]
# . There are 3
#  subarrays of b
#  equal to [1,2,3]
#  (highlighted in red):
#
# [1,1,2,1,2,3,1,2,3,4,1,2,3,4,5]
# ;
# [1,1,2,1,2,3,1,2,3,4,1,2,3,4,5]
# ;
# [1,1,2,1,2,3,1,2,3,4,1,2,3,4,5]
# .
# In the third test case, the blackboard contains the numbers
#
# b=[1,1,2,1,2,3,1,2,3,4,1,2,3,4,5,1,2,3,4,5,6]
#
# and James's list of favorite numbers is [3,1,2,3,4,1]
# . There is only 1
#  subarray of b
#  equal to [3,1,2,3,4,1]
#  (highlighted in red):
#
# [1,1,2,1,2,3,1,2,3,4,1,2,3,4,5,1,2,3,4,5,6]
# .
# Solution
# C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>


void solution() {
    size_t n, m;
    std::cin >> n >> m;
    std::vector<int> nums(m, 0);
    for (size_t i = 0; i < m; ++i) std::cin >> nums[i];
    bool isValid = true;
    for (size_t i = 1; i < m; ++i) {
        if ((nums[i] - 1) != nums[i - 1]) {
            isValid = false;
            break;
        }
    }
    std::cout << (isValid ? n - nums[m - 1] + 1 : 1) << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) Greedy
import sys


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    is_valid: bool = True
    for i in range(1, m):
        if nums[i] - 1 != nums[i - 1]:
            is_valid = False
            break
    sys.stdout.write('{}\n'.format([1, n - nums[m - 1] + 1][is_valid]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()