# B. Villagers
# time limit per test1 second
# memory limit per test256 megabytes
#
# Steve lives in a village with n
#  other villagers. Unfortunately, due to disputes over the distribution of emeralds, none of those villagers are friends with any other villager. Furthermore, villager i
#  initially has a grumpiness of gi
# .
#
# Steve can perform the following operation any number of times:
#
# Select two villagers i
#  and j
#  and give them max(gi,gj)
#  emeralds to share. Both of their grumpinesses decrease by min(gi,gj)
# , and they become friends with each other if they weren't already.
# Steve wishes to make every villager friends with every other villager (possibly through some intermediate friendships); that is, from any villager, you can follow a path of friendships to reach any other villager. Since he does not want to inflate the village economy too much, calculate the minimum number of emeralds he must give away to accomplish this.
#
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t
#  (1≤t≤104
# ). The description of the test cases follows.
#
# The first line of each test case contains a single integer n
#  (2≤n≤2⋅105
# ) — the number of villagers.
#
# The second line of each test case contains n
#  integers g1,g2,…,gn
#  (1≤gi≤109
# ) — the initial grumpiness of each villager.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer — the minimum number of emeralds Steve must give away to make everyone friends.
#
# Example
# InputCopy
# 4
# 2
# 1 2
# 4
# 2 1 5 2
# 5
# 1000000000 1000000000 1000000000 1000000000 1000000000
# 6
# 3 1 4 1 5 9
# OutputCopy
# 2
# 7
# 3000000000
# 14
# Note
# In the first test case, the only valid operation is i=1
# , j=2
# . Steve gives them max(1,2)=2
#  emeralds, and they become friends.
#
# In the second test case, one optimal sequence of operations is as follows:
#
# Steve chooses i=1
# , j=3
# . He gives the villagers max(2,5)=5
#  emeralds, and their grumpiness decreases by min(2,5)=2
# . Now everyone's grumpiness is [0,1,3,2]
# ;
# Steve chooses i=2
# , j=4
# . He gives the villagers max(1,2)=2
#  emeralds, and their grumpiness decreases by min(1,2)=1
# . Now everyone's grumpiness is [0,0,3,1]
# ;
# Steve chooses i=1
# , j=2
# . He gives the villagers max(0,0)=0
#  emeralds, and their grumpiness decreases by min(0,0)=0
# . Now everyone's grumpiness is [0,0,3,1]
# .
# After this, the pairs of villagers (1,3)
# , (2,4)
#  and (1,2)
#  are directly friends, and every other pair of villagers is connected by a chain of mutual friendships. It can be shown that Steve cannot spend fewer than 7
#  emeralds to accomplish this.
# Solution
# C++ O(NlogN) O(1) Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    long long output = 0;
    for (int i = n - 1; i >= 0; i -= 2) output += nums[i];
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) O(1) Greedy
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    output: int = sum(nums[i] for i in range(n - 1, -1, -2))
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()