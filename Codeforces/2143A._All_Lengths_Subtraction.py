# A. All Lengths Subtraction
# time limit per test1 second
# memory limit per test256 megabytes
#
# You are given a permutation∗
#  p
#  of length n
# .
#
# You must perform exactly one operation for each integer k
#  from 1 up to n
#  in that order:
#
# Choose a subarray†
#  of p
#  of length exactly k
# , and subtract 1 from every element in that subarray.
# After completing all n
#  operations, your goal is to have all elements of the array equal to zero.
#
# Determine whether it is possible to achieve this.
#
# ∗
# A permutation of length n
#  is an array consisting of n
#  distinct integers from 1
#  to n
#  in arbitrary order. For example, [2,3,1,5,4]
#  is a permutation, but [1,2,2]
#  is not a permutation (2
#  appears twice in the array), and [1,3,4]
#  is also not a permutation (n=3
#  but there is 4
#  in the array).
#
# †
# An array a
#  is a subarray of an array b
#  if a
#  can be obtained from b
#  by the deletion of several (possibly, zero or all) elements from the beginning and several (possibly, zero or all) elements from the end.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤100
# ). The description of the test cases follows.
#
# The first line contains the value n
#  (1≤n≤100
# ) — the length of the permutation.
#
# The second line contains p1,p2,…pn
#  (1≤pi≤n
# ) — the permutation itself.
#
# Output
# For each test case, output YES if it is possible to make all elements of the array p
#  equal to 0
#  after performing all the operations; otherwise, output NO.
#
# You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.
#
# Example
# InputCopy
# 4
# 4
# 1 3 4 2
# 5
# 1 5 2 4 3
# 5
# 2 4 5 3 1
# 3
# 3 1 2
# OutputCopy
# YES
# NO
# YES
# NO
# Note
# For the first test case, we can proceed as follows:
#
# k=1
# : Choose the subarray [3,3]
# . The array [1,3,4,2]
#  becomes [1,3,3,2]
# .
# k=2
# : Choose the subarray [2,3]
# . The array [1,3,3,2]
#  becomes [1,2,2,2]
# .
# k=3
# : Choose the subarray [2,4]
# . The array [1,2,2,2]
#  becomes [1,1,1,1]
# .
# k=4
# : Choose the subarray [1,4]
# . The array [1,1,1,1]
#  becomes [0,0,0,0]
# .
# Thus, we have successfully reduced the entire array to zeros, so the answer is YES.
#
# For the second test case, it can be shown that it is impossible to reduce all elements to zero.
#
# For the third test case, the process is as follows:
#
# [2,4,5,3,1]→[2,4,4,3,1]→[2,3,3,3,1]→[2,2,2,2,1]→[1,1,1,1,1]→[0,0,0,0,0].
#
# The bolded values indicate the subarrays from which we subtract at each step.
#
# For the fourth test case, it can also be proven that it is impossible to make all values zero.
# Solution
# C++ O(N) O(1) TwoPointers
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    size_t left = 0, right = 0, start = 0;
    for (size_t i = 0; i < n; ++i) {
        if (nums[i] == n) {
            start = i;
            left = i;
            right = i;
            break;
        }
    }
    int cur = n;
    while (cur) {
        if (nums[left] == cur) (left ? --left : 0);
        else if (nums[right] == cur) (right < n ? ++right : 0);
        else break;

        if (cur == n) {
            if (left == start && left) --left;
            else if (right < n - 1) ++right;
        }
        --cur;
    }
    std::cout << (!cur ? "YES" : "NO") << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(N) O(1) TwoPointers
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    start: int = nums.index(max(nums))
    left: int = start
    right: int = start
    cur: int = n
    while cur:
        if nums[left] == cur:
            if left: left -= 1
        elif nums[right] == cur:
            if right < n - 1: right += 1
        else: break
        if cur == n:
            if left == start and left: left -= 1
            elif right < n - 1: right += 1
        cur -= 1
    sys.stdout.write('{}\n'.format(['NO', 'YES'][not cur]))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()