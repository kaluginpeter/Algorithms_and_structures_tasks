# B. Two Arrays And Swaps
# time limit per test1 second
# memory limit per test256 megabytes
# You are given two arrays a
#  and b
#  both consisting of n
#  positive (greater than zero) integers. You are also given an integer k
# .
#
# In one move, you can choose two indices i
#  and j
#  (1≤i,j≤n
# ) and swap ai
#  and bj
#  (i.e. ai
#  becomes bj
#  and vice versa). Note that i
#  and j
#  can be equal or different (in particular, swap a2
#  with b2
#  or swap a3
#  and b9
#  both are acceptable moves).
#
# Your task is to find the maximum possible sum you can obtain in the array a
#  if you can do no more than (i.e. at most) k
#  such moves (swaps).
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤200
# ) — the number of test cases. Then t
#  test cases follow.
#
# The first line of the test case contains two integers n
#  and k
#  (1≤n≤30;0≤k≤n
# ) — the number of elements in a
#  and b
#  and the maximum number of moves you can do. The second line of the test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤30
# ), where ai
#  is the i
# -th element of a
# . The third line of the test case contains n
#  integers b1,b2,…,bn
#  (1≤bi≤30
# ), where bi
#  is the i
# -th element of b
# .
#
# Output
# For each test case, print the answer — the maximum possible sum you can obtain in the array a
#  if you can do no more than (i.e. at most) k
#  swaps.
#
# Example
# inputCopy
# 5
# 2 1
# 1 2
# 3 4
# 5 5
# 5 5 6 6 5
# 1 2 5 4 3
# 5 3
# 1 2 3 4 5
# 10 9 10 10 9
# 4 0
# 2 2 4 3
# 2 4 2 3
# 4 4
# 1 2 2 1
# 4 4 5 4
# outputCopy
# 6
# 27
# 39
# 11
# 17
# Note
# In the first test case of the example, you can swap a1=1
#  and b2=4
# , so a=[4,2]
#  and b=[3,1]
# .
#
# In the second test case of the example, you don't need to swap anything.
#
# In the third test case of the example, you can swap a1=1
#  and b1=10
# , a3=3
#  and b3=10
#  and a2=2
#  and b4=10
# , so a=[10,10,10,4,5]
#  and b=[1,9,3,2,9]
# .
#
# In the fourth test case of the example, you cannot swap anything.
#
# In the fifth test case of the example, you can swap arrays a
#  and b
# , so a=[4,4,5,4]
#  and b=[1,2,2,1]
# .
# Solution
# Python O(NlogN) O(1) Two Pointers Sorting
import sys
from typing import List


def solution(t: int) -> None:
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        a: List[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        b: List[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        a.sort()
        b.sort()
        left: int = 0
        right: int = n - 1
        for _ in range(k):
            if a[left] >= b[right]: break
            a[left] = b[right]
            left += 1
            right -= 1
        sys.stdout.write(str(sum(a)) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

# C++ O(NlogN) O(1) Two Pointers Sorting
#include <iostream>
#include <vector>
#include <numeric>
#include <algorithm>

int main() {
    size_t t;
    std::cin >> t;
    for (size_t rep = 0; rep < t; ++rep) {
        size_t n;
        int k;
        std::cin >> n >> k;
        std::vector<int> a_nums;
        for (size_t j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            a_nums.push_back(num);
        }
        std::vector<int> b_nums;
        for (size_t j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            b_nums.push_back(num);
        }
        std::sort(a_nums.begin(), a_nums.end());
        std::sort(b_nums.begin(), b_nums.end());
        size_t left = 0;
        size_t right = n - 1;
        for (int move = 0; move < k; ++move) {
            if (a_nums[left] >= b_nums[right]) {
                break;
            }
            a_nums[left] = b_nums[right];
            left += 1;
            right -= 1;
        }
        std::cout << std::accumulate(a_nums.begin(), a_nums.end(), 0) << std::endl;
    }
}