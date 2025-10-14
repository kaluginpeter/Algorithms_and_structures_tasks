# A. Circle of Apple Trees
# time limit per test1 second
# memory limit per test256 megabytes
#
# There are n
#  apple trees arranged in a circle. Each tree bears exactly one apple, and the beauty of the apple on the i
# -th tree is given by bi
#  for all 1≤i≤n
# . You start in front of tree 1
# .
#
# At each tree, you may choose to either eat the apple or skip it. After making your choice, you move to the next tree: from tree i
# , you move to tree i+1
#  for 1≤i≤n−1
# , and from tree n
# , you move back to tree 1
# . This process continues indefinitely as you move through the trees in a cycle.
#
# However, you have a special condition: you may only eat an apple if its beauty is strictly greater than the beauty of the last apple you ate. For example, if b=[2,1,2,3]
#  and you eat the apple on tree 1
#  (beauty 2
# ), you cannot eat the apples on trees 2
#  and 3
#  because their beauties are not greater than 2
# . However, you may eat the apple on tree 4
#  since b4=3>2
# .
#
# Note that you are allowed to skip an apple when you first encounter it, and you can choose to eat it later on a subsequent cycle.
#
# Your task is to determine the maximum number of apples you can eat if you make optimal decisions on when to eat or skip each apple.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤500
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (1≤n≤100
# ) — the number of apple trees.
#
# The second line of each test case contains n
#  integers b1,b2,…,bn
#  (1≤bi≤n
# ) — the beauty of the apples on the trees.
#
# Note that there are no constraints on the sum of n
#  over all test cases.
#
# Output
# For each test case, output a single integer representing the maximum number of apples you can eat.
#
# Example
# InputCopy
# 3
# 4
# 2 2 2 2
# 5
# 1 4 5 1 2
# 6
# 5 4 2 1 2 3
# OutputCopy
# 1
# 4
# 5
# Note
# In the first test case, since all apples have the same beauty, no matter which apple you eat first, you cannot eat any others afterward. Hence, the maximum number of apples that you can eat is 1
# .
#
# In the second test case, you can eat four apples as follows:
#
# At tree 1
# , skip the apple.
# At tree 2
# , skip the apple.
# At tree 3
# , skip the apple.
# At tree 4
# , eat the apple (beauty 1
# ).
# At tree 5
# , eat the apple (beauty 2
# ).
# At tree 1
# , skip the apple. You are not allowed to eat the apple as its beauty (b1=1
# ) is not greater than the beauty of the last apple you ate (b5=2
# ).
# At tree 2
# , eat the apple (beauty 4
# ).
# At tree 3
# , eat the apple (beauty 5
# ).
# It can be proven that it is not possible to eat all five apples; hence, the maximum number of apples that you can eat is 4
# .
# Solution
# C++ O(NlogN) O(1) Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    int output = 1;
    for (size_t i = 1; i < n; ++i) {
        if (nums[i] > nums[i - 1]) ++output;
    }
    std::cout << output << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) O(1) Sorting
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    output: int = 1 + sum(nums[i] > nums[i - 1] for i in range(1, n))
    sys.stdout.write('{}\n'.format(output))

if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()