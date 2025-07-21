# C. I Will Definitely Make It
# time limit per test1 second
# memory limit per test256 megabytes
# You are given n
#  towers, numbered from 1
#  to n
# . Tower i
#  has a height of hi
# . At time 0
# , you are on the tower with index k
# , and the current water level is 1
# .
#
# Every second, the water level rises by 1
#  unit. At any moment, if the water level becomes strictly greater than the height of the tower you are on, you perish.
#
# You have a magical ability: at moment x
# , you can start teleporting from tower i
#  to tower j
# , which will take |hi−hj|
#  seconds. That is, until moment x+|hi−hj|
# , you will be on tower i
# , and at moment x+|hi−hj|
# , you will move to tower j
# . You can start a new teleportation at the same moment you just arrived at tower j
# .
#
# For example, if n=k=4
# , h=[4,4,4,2]
# , then if you start teleporting from tower 4
#  to tower 1
#  at moment 0
# , the movement will look as follows:
#
#
# Note that if the height of tower 1
#  were 5
# , you would not be able to teleport to it immediately, as you would be submerged at moment 2
# .
#
# Your goal is to reach any tower with the maximum height before the water covers you.
#
# Determine if this is possible.
#
# Input
# Each test consists of several test cases. The first line contains a single integer t
#  (1≤t≤104
# ) — the number of test cases. The description of the test cases follows.
#
# The first line of each test case contains two integers n
#  and k
#  (1≤k≤n≤105
# ) — the number of towers and the index of the tower you are initially on.
#
# The second line contains n
#  integers h1,h2,…,hn
#  (1≤hi≤109
# ) — the heights of the towers.
#
# It is guaranteed that the sum of all n
#  across all test cases does not exceed 105
# .
#
# Output
# For each test case, output one line: "YES", if you can reach the tower with the maximum height before the water covers you, or "NO" otherwise.
#
# You may output each letter in any case (lowercase or uppercase). For example, the strings "yEs", "yes", "Yes", and "YES" will be accepted as a positive answer.
#
# Example
# InputCopy
# 5
# 5 3
# 3 2 1 4 5
# 3 1
# 1 3 4
# 4 4
# 4 4 4 2
# 6 2
# 2 3 6 9 1 2
# 4 2
# 1 2 5 6
# OutputCopy
# YES
# NO
# YES
# YES
# NO
# Note
# In the first test case, the only possible path is: 3→2→1→4→5
# .
#
# In the second test case, regardless of the order, it will not be possible to reach the tallest tower.
#
# In the third test case, one of the possible paths is: 4→1
# .
# Solution
# C++ O(NlogN) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int n, k;
    std::cin >> n >> k;
    std::vector<int> nums(n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    int start = nums[k - 1];
    std::sort(nums.begin(), nums.end());
    int water = 0;
    int cur = 0;
    for (int i = 0; i < n; ++i) {
        if (nums[i] == start) cur = i;
    }
    for (int i = cur + 1; i < n; ++i) {
        int wasted = nums[i] - nums[i - 1];
        water += wasted;
        if (water > nums[i - 1]) break;
        cur = i;
    }
    std::cout << (nums[cur] == nums[n - 1] ? "YES" : "NO") << std::endl;
}


int main() {
    int t;
    std::cin >> t;
    while (t--) solution();
}

# Python O(NlogN) O(1) Sorting Greedy
import sys


def solution() -> None:
    n, k = map(int, sys.stdin.readline().rstrip().split())
    nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    start: int = nums[k - 1]
    nums.sort()
    cur: int = 0
    for i in range(n):
        if nums[i] == start: cur = i
    water: int = 0
    for i in range(cur + 1, n):
        wasted: int = nums[i] - nums[i - 1]
        water += wasted
        if water > nums[i - 1]: break
        cur = i
    sys.stdout.write('{}\n'.format('YES' if nums[cur] == nums[-1] else 'NO'))


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t): solution()