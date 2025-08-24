# C. Splitting Items
# time limit per test2 seconds
# memory limit per test256 megabytes
# Alice and Bob have n
#  items they'd like to split between them, so they decided to play a game. All items have a cost, and the i
# -th item costs ai
# . Players move in turns starting from Alice.
#
# In each turn, the player chooses one of the remaining items and takes it. The game goes on until no items are left.
#
# Let's say that A
#  is the total cost of items taken by Alice and B
#  is the total cost of Bob's items. The resulting score of the game then will be equal to A−B
# .
#
# Alice wants to maximize the score, while Bob wants to minimize it. Both Alice and Bob will play optimally.
#
# But the game will take place tomorrow, so today Bob can modify the costs a little. He can increase the costs ai
#  of several (possibly none or all) items by an integer value (possibly, by the same value or by different values for each item). However, the total increase must be less than or equal to k
# . Otherwise, Alice may suspect something. Note that Bob can't decrease costs, only increase.
#
# What is the minimum possible score Bob can achieve?
#
# Input
# The first line contains a single integer t
#  (1≤t≤5000
# ) — the number of test cases. Then t
#  cases follow.
#
# The first line of each test case contains two integers n
#  and k
#  (2≤n≤2⋅105
# ; 0≤k≤109
# ) — the number of items and the maximum total increase Bob can make.
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ) — the initial costs of the items.
#
# It's guaranteed that the sum of n
#  over all test cases doesn't exceed 2⋅105
# .
#
# Output
# For each test case, print a single integer — the minimum possible score A−B
#  after Bob increases the costs of several (possibly none or all) items.
#
# Example
# InputCopy
# 4
# 2 5
# 1 10
# 3 0
# 10 15 12
# 4 6
# 3 1 2 4
# 2 4
# 6 9
# OutputCopy
# 4
# 13
# 0
# 0
# Note
# In the first test case, Bob can increase a1
#  by 5
# , making costs equal to [6,10]
# . Tomorrow, Alice will take 10
#  and Bob will take 6
# . The total score will be equal to 10−6=4
# , and it's the minimum possible.
#
# In the second test case, Bob can't change costs. So the score will be equal to (15+10)−12=13
# , since Alice will take 15
# , Bob will take 12
# , and Alice — 10
# .
#
# In the third test case, Bob, for example, can increase a1
#  by 1
# , a2
#  by 3
# , and a3
#  by 2
# . The total change is equal to 1+3+2≤6
#  and costs will be equal to [4,4,4,4]
# . Obviously, the score will be equal to (4+4)−(4+4)=0
# .
#
# In the fourth test case, Bob can increase a1
#  by 3
# , making costs equal to [9,9]
# . The score will be equal to 9−9=0
# .
# Solution
# C++ O(NlogN) O(1) Sorting
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    long long output = 0;
    for (int i = n - 1; i > 0; i -= 2) {
        if (nums[i] == nums[i - 1]) continue;
        int can = std::min(k, nums[i] - nums[i - 1]);
        k -= can;
        output += nums[i] - nums[i - 1] - can;
    }
    if (n & 1) output += nums[0];
    std::cout << output << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) O(1) Sorting
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
    output: int = 0
    for i in range(n - 1, 0, -2):
        if nums[i] == nums[i - 1]: continue
        can: int = min(k, nums[i] - nums[i - 1])
        k -= can
        output += nums[i] - nums[i - 1] - can
    if n & 1: output += nums[0]
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()