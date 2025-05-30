# B. Gifts Fixing
# time limit per test1 second
# memory limit per test256 megabytes
# You have n
#  gifts and you want to give all of them to children. Of course, you don't want to offend anyone, so all gifts should be equal between each other. The i
# -th gift consists of ai
#  candies and bi
#  oranges.
#
# During one move, you can choose some gift 1≤i≤n
#  and do one of the following operations:
#
# eat exactly one candy from this gift (decrease ai
#  by one);
# eat exactly one orange from this gift (decrease bi
#  by one);
# eat exactly one candy and exactly one orange from this gift (decrease both ai
#  and bi
#  by one).
# Of course, you can not eat a candy or orange if it's not present in the gift (so neither ai
#  nor bi
#  can become less than zero).
#
# As said above, all gifts should be equal. This means that after some sequence of moves the following two conditions should be satisfied: a1=a2=⋯=an
#  and b1=b2=⋯=bn
#  (and ai
#  equals bi
#  is not necessary).
#
# Your task is to find the minimum number of moves required to equalize all the given gifts.
#
# You have to answer t
#  independent test cases.
#
# Input
# The first line of the input contains one integer t
#  (1≤t≤1000
# ) — the number of test cases. Then t
#  test cases follow.
#
# The first line of the test case contains one integer n
#  (1≤n≤50
# ) — the number of gifts. The second line of the test case contains n
#  integers a1,a2,…,an
#  (1≤ai≤109
# ), where ai
#  is the number of candies in the i
# -th gift. The third line of the test case contains n
#  integers b1,b2,…,bn
#  (1≤bi≤109
# ), where bi
#  is the number of oranges in the i
# -th gift.
#
# Output
# For each test case, print one integer: the minimum number of moves required to equalize all the given gifts.
#
# Example
# InputCopy
# 5
# 3
# 3 5 6
# 3 2 3
# 5
# 1 2 3 4 5
# 5 4 3 2 1
# 3
# 1 1 1
# 2 2 2
# 6
# 1 1000000000 1000000000 1000000000 1000000000 1000000000
# 1 1 1 1 1 1
# 3
# 10 12 8
# 7 5 4
# OutputCopy
# 6
# 16
# 0
# 4999999995
# 7
# Note
# In the first test case of the example, we can perform the following sequence of moves:
#
# choose the first gift and eat one orange from it, so a=[3,5,6]
#  and b=[2,2,3]
# ;
# choose the second gift and eat one candy from it, so a=[3,4,6]
#  and b=[2,2,3]
# ;
# choose the second gift and eat one candy from it, so a=[3,3,6]
#  and b=[2,2,3]
# ;
# choose the third gift and eat one candy and one orange from it, so a=[3,3,5]
#  and b=[2,2,2]
# ;
# choose the third gift and eat one candy from it, so a=[3,3,4]
#  and b=[2,2,2]
# ;
# choose the third gift and eat one candy from it, so a=[3,3,3]
#  and b=[2,2,2]
# .
# Solution
# C++ O(N) O(1) Math Greedy
#include <iostream>
#include <vector>

void solution(int t) {
    for (int i = 0; i < t; ++i) {
        int n;
        std::cin >> n;
        std::vector<int> candies;
        int minCandy = 1000000000;
        for (int j = 0; j < n; ++j) {
            int candy;
            std::cin >> candy;
            minCandy = std::min(minCandy, candy);
            candies.push_back(candy);
        }
        std::vector<int> oranges;
        int minOrange = 1000000000;
        for (int j = 0; j < n; ++j) {
            int orange;
            std::cin >> orange;
            minOrange = std::min(minOrange, orange);
            oranges.push_back(orange);
        }
        long long moves = 0;
        for (int index = 0; index < n; ++index) {
            int neededCandies = candies[index] - minCandy;
            int neededOranges = oranges[index] - minOrange;
            int mainPart = std::min(neededCandies, neededOranges);
            moves += mainPart;
            moves += neededCandies + neededOranges - mainPart * 2;
        }
        std::cout << moves << "\n";
    }
}

int main() {
    int t;
    std::cin >> t;
    solution(t);
}

# Python O(N) O(1) Math Greedy
import sys


def solution(t: int) -> None:
    for _ in range(t):
        n: int = int(sys.stdin.readline().rstrip())
        candies: list = list(map(int, sys.stdin.readline().rstrip().split()))
        oranges: list = list(map(int, sys.stdin.readline().rstrip().split()))
        min_candy: int = min(candies)
        min_orange: int = min(oranges)
        moves: int = 0
        for idx in range(n):
            needed_candies: int = candies[idx] - min_candy
            needed_oranges: int = oranges[idx] - min_orange
            main_part: int = min(needed_candies, needed_oranges)
            moves += main_part
            moves += needed_candies + needed_oranges - main_part * 2
        sys.stdout.write(str(moves) + '\n')


if __name__ == '__main__':
    t: int = int(sys.stdin.readline().rstrip())
    solution(t)

