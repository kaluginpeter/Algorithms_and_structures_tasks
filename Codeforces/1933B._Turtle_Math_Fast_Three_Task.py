# B. Turtle Math: Fast Three Task
# time limit per test2 seconds
# memory limit per test256 megabytes
# You are given an array a1,a2,…,an
# .
#
# In one move, you can perform either of the following two operations:
#
# Choose an element from the array and remove it from the array. As a result, the length of the array decreases by 1
# ;
# Choose an element from the array and increase its value by 1
# .
# You can perform any number of moves. If the current array becomes empty, then no more moves can be made.
#
# Your task is to find the minimum number of moves required to make the sum of the elements of the array a
#  divisible by 3
# . It is possible that you may need 0
#  moves.
#
# Note that the sum of the elements of an empty array (an array of length 0
# ) is equal to 0
# .
#
# Input
# The first line of the input contains a single integer t
#  (1≤t≤104
# ) — the number of test cases.
#
# The first line of each test case contains a single integer n
#  (1≤n≤105
# ).
#
# The second line of each test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤104
# ).
#
# The sum of n
#  over all test cases does not exceed 2⋅105
# .
#
# Output
# For each test case, output a single integer: the minimum number of moves.
#
# Example
# InputCopy
# 8
# 4
# 2 2 5 4
# 3
# 1 3 2
# 4
# 3 7 6 8
# 1
# 1
# 4
# 2 2 4 2
# 2
# 5 5
# 7
# 2 4 8 1 9 3 4
# 2
# 4 10
# OutputCopy
# 1
# 0
# 0
# 1
# 1
# 2
# 1
# 1
# Note
# In the first test case, initially the array a=[2,2,5,4]
# . One of the optimal ways to make moves is:
#
# remove the current 4
# th element and get a=[2,2,5]
# ;
# As a result, the sum of the elements of the array a
#  will be divisible by 3
#  (indeed, a1+a2+a3=2+2+5=9
# ).
# In the second test case, initially, the sum of the array is 1+3+2=6
# , which is divisible by 3
# . Therefore, no moves are required. Hence, the answer is 0
# .
#
# In the fourth test case, initially, the sum of the array is 1
# , which is not divisible by 3
# . By removing its only element, you will get an empty array, so its sum is 0
# . Hence, the answer is 1
# .
# Solution
# C++ O(N) O(1) HashMap Greedy
#include <iostream>
#include <vector>


void solution() {
    int t;
    std::scanf("%d", &t);
    for (int i = 0; i < t; ++i) {
        int n;
        std::scanf("%d", &n);
        long long totalSum = 0;
        std::vector<int> hashmap(3, 0);
        for (int j = 0; j < n; ++j) {
            int x;
            std::scanf("%d", &x);
            ++hashmap[x % 3];
            totalSum += x;
        }
        if (totalSum % 3 == 0) {
            std::printf("0\n");
            continue;
        }
        int rm = (hashmap[totalSum % 3] ? 1 : 3);
        int add = 3 - totalSum % 3;
        std::printf("%d\n", std::min(rm, add));
    }
}


int main() {
    solution();
}

# Python O(N) O(1) HashMap
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        nums: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        hashmap: list[int] = [0] * 3
        total_sum: int = 0
        for num in nums:
            hashmap[num % 3] += 1
            total_sum += num
        if total_sum % 3 == 0:
            sys.stdout.write('0\n')
            continue
        rm: int = [3, 1][bool(hashmap[total_sum % 3])]
        add: int = 3 - total_sum % 3
        sys.stdout.write('{}\n'.format(min(rm, add)))


if __name__ == '__main__':
    solution()