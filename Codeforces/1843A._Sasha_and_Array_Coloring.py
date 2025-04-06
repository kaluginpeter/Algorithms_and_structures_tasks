# A. Sasha and Array Coloring
# time limit per test1 second
# memory limit per test256 megabytes
# Sasha found an array a
#  consisting of n
#  integers and asked you to paint elements.
#
# You have to paint each element of the array. You can use as many colors as you want, but each element should be painted into exactly one color, and for each color, there should be at least one element of that color.
#
# The cost of one color is the value of max(S)−min(S)
# , where S
#  is the sequence of elements of that color. The cost of the whole coloring is the sum of costs over all colors.
#
# For example, suppose you have an array a=[1,5,6,3,4]
# , and you painted its elements into two colors as follows: elements on positions 1
# , 2
#  and 5
#  have color 1
# ; elements on positions 3
#  and 4
#  have color 2
# . Then:
#
# the cost of the color 1
#  is max([1,5,4])−min([1,5,4])=5−1=4
# ;
# the cost of the color 2
#  is max([6,3])−min([6,3])=6−3=3
# ;
# the total cost of the coloring is 7
# .
# For the given array a
# , you have to calculate the maximum possible cost of the coloring.
#
# Input
# The first line contains one integer t
#  (1≤t≤1000
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤50
# ) — length of a
# .
#
# The second line contains n
#  integers a1,a2,…,an
#  (1≤ai≤50
# ) — array a
# .
#
# Output
# For each test case output the maximum possible cost of the coloring.
#
# Example
# InputCopy
# 6
# 5
# 1 5 6 3 4
# 1
# 5
# 4
# 1 6 3 9
# 6
# 1 13 9 3 7 2
# 4
# 2 2 2 2
# 5
# 4 5 2 2 3
# OutputCopy
# 7
# 0
# 11
# 23
# 0
# 5
# Note
# In the first example one of the optimal coloring is [1,5,6,3,4]
# . The answer is (5−1)+(6−3)=7
# .
#
# In the second example, the only possible coloring is [5]
# , for which the answer is 5−5=0
# .
#
# In the third example, the optimal coloring is [1,6,3,9]
# , the answer is (9−1)+(6−3)=11
# .
# Solution
# C++ O(NlogN) O(1) Sorting Two Pointers
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        std::vector<int> nums (n, 0);
        for (int j = 0; j < n; ++j) std::scanf("%d", &nums[j]);
        std::sort(nums.begin(), nums.end());
        int score = 0;
        int left = 0, right = n - 1;
        while (left < right) {
            score += nums[right] - nums[left];
            ++left;
            --right;
        }
        std::printf("%d\n", score);
    }
}


int main() {
    solution();
}

# Python O(NlogN) O(1) Sorting TwoPointers
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = sorted(map(int, sys.stdin.readline().rstrip().split()))
        score: int = 0
        left: int = 0
        right: int = n - 1
        while left < right:
            score += nums[right] - nums[left]
            left += 1
            right -= 1
        sys.stdout.write('{}\n'.format(score))


if __name__ == '__main__':
    solution()