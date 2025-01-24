# C. Advantage
# time limit per test2 seconds
# memory limit per test256 megabytes
# There are n
#  participants in a competition, participant i
#  having a strength of si
# .
#
# Every participant wonders how much of an advantage they have over the other best participant. In other words, each participant i
#  wants to know the difference between si
#  and sj
# , where j
#  is the strongest participant in the competition, not counting i
#  (a difference can be negative).
#
# So, they ask you for your help! For each i
#  (1≤i≤n
# ) output the difference between si
#  and the maximum strength of any participant other than participant i
# .
#
# Input
# The input consists of multiple test cases. The first line contains an integer t
#  (1≤t≤1000
# ) — the number of test cases. The descriptions of the test cases follow.
#
# The first line of each test case contains an integer n
#  (2≤n≤2⋅105
# ) — the length of the array.
#
# The following line contains n
#  space-separated positive integers s1
# , s2
# , ..., sn
#  (1≤si≤109
# ) — the strengths of the participants.
#
# It is guaranteed that the sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output n
#  space-separated integers. For each i
#  (1≤i≤n
# ) output the difference between si
#  and the maximum strength of any other participant.
#
# Example
# InputCopy
# 5
# 4
# 4 7 3 5
# 2
# 1 2
# 5
# 1 2 3 4 5
# 3
# 4 9 4
# 4
# 4 4 4 4
# OutputCopy
# -3 2 -4 -2
# -1 1
# -4 -3 -2 -1 1
# -5 5 -5
# 0 0 0 0
# Note
# For the first test case:
#
# The first participant has a strength of 4
#  and the largest strength of a participant different from the first one is 7
# , so the answer for the first participant is 4−7=−3
# .
# The second participant has a strength of 7
#  and the largest strength of a participant different from the second one is 5
# , so the answer for the second participant is 7−5=2
# .
# The third participant has a strength of 3
#  and the largest strength of a participant different from the third one is 7
# , so the answer for the third participant is 3−7=−4
# .
# The fourth participant has a strength of 5
#  and the largest strength of a participant different from the fourth one is 7
# , so the answer for the fourth participant is 5−7=−2
# .
# Solution
# C++ O(NlogN) O(N) HashMap Sorting
#include <bits/stdc++.h>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> nums;
        std::unordered_map<int, int> hashmap;
        for (int j = 0; j < n; ++j) {
            int num;
            std::cin >> num;
            nums.push_back(num);
            hashmap[j] = num;
        }
        std::sort(nums.begin(), nums.end());
        for (int j = 0; j < n; ++j) {
            if (hashmap[j] == nums[n - 1]) {
                std::cout << hashmap[j] - nums[n - 2] << " ";
            } else {
                std::cout << hashmap[j] - nums[n - 1] << " ";
            }
        }
        std::cout << "\n";
    }
}


int main() {
    solution();
}

# Python O(NlogN) O(N) Sorting Hashmap
from __future__ import annotations
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        maps: dict[int, int] = {idx:nums[idx] for idx in range(n)}
        nums.sort()
        for i in range(n):
            if maps[i] == nums[-1]:
                sys.stdout.write(f'{maps[i] - nums[-2]} ')
            else:
                sys.stdout.write(f'{maps[i] - nums[-1]} ')
        sys.stdout.write('\n')


if __name__ == '__main__':
    solution()