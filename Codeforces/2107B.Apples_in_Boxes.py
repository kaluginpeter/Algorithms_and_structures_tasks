# Apples in Boxes
# Input file: standard input
# Output file: standard output
# Time limit: 1 second
# Memory limit: 256 megabytes
# Tom and Jerry found some apples in the basement. They decided to play a game to get some apples.
# There are n boxes, and the i-th box has ai apples inside. Tom and Jerry take turns picking up apples.
# Tom goes first. On their turn, they have to do the following:
# • Choose a box i (1 ≤ i ≤ n) with a positive number of apples, i.e. ai > 0, and pick 1 apple from this
# box. Note that this reduces ai by 1.
# • If no valid box exists, the current player loses.
# • If after the move, max(a1, a2, . . . , an) − min(a1, a2, . . . , an) > k holds, then the current player
# (who made the last move) also loses.
# If both players play optimally, predict the winner of the game.
# Input
# Each test contains multiple test cases. The first line contains the number of test cases t (1 ≤ t ≤ 104
# ).
# The description of the test cases follows.
# The first line of each test case contains two integers n, k (2 ≤ n ≤ 105
# , 1 ≤ k ≤ 109
# ).
# The second line of each test case contains n integers a1, a2, . . . , an (1 ≤ ai ≤ 109
# ).
# It is guaranteed that the sum of n over all test cases does not exceed 105
# .
# Output
# For each test case, print “Tom” (without quotes) if Tom will win, or “Jerry” (without quotes) otherwise.
# Example
# standard input standard output
# 3
# 3 1
# 2 1 2
# 3 1
# 1 1 3
# 2 1
# 1 4
# Tom
# Tom
# Jerry
# Note
# Note that neither player is necessarily playing an optimal strategy in the following games, just to give
# you an idea of how the game is going.
# In the first test case of the example, one possible situation is shown as follows.
# • Tom takes an apple from the first box. The array a becomes [1, 1, 2]. Tom does not lose because
# max(1, 1, 2) − min(1, 1, 2) = 1 ≤ k.
# • Jerry takes an apple from the first box as well. The array a becomes [0, 1, 2]. Jerry loses because
# max(0, 1, 2) − min(0, 1, 2) = 2 > k.
# Page 1 of 1
# Solution
# C++ O(N) O(1) Greedy Math
#include <iostream>


void solution() {
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int n, k;
        std::cin >> n >> k;
        int minNumber = 2e9, maxNumber = 0, maxNumberFreq = 0;
        long long totalApples = 0;
        for (int j = 0; j < n; ++j) {
            int apple;
            std::cin >> apple;
            totalApples += apple;
            minNumber = std::min(minNumber, apple);
            if (apple == maxNumber) ++maxNumberFreq;
            else if (apple > maxNumber) {
                maxNumber = apple;
                maxNumberFreq = 1;
            }
        }
        if ((maxNumber - minNumber - 1 > k) || (maxNumber - minNumber > k && maxNumberFreq > 1)) {
            std::cout << "Jerry\n";
            continue;
        }
        std::cout << (totalApples & 1 ? "Tom" : "Jerry") << "\n";
    }
}


int main() {
    solution();
}

# Python O(N) O(1) Greedy Math
import sys


def solution() -> None:
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().rstrip().split())
        apples: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
        total_apples: int = sum(apples)
        min_number: int = min(apples)
        max_number: int = max(apples)
        max_number_freq: int = apples.count(max_number)
        if (max_number - min_number - 1 > k) or (max_number - min_number > k and max_number_freq > 1):
            sys.stdout.write('Jerry\n')
            continue
        sys.stdout.write('{}\n'.format(['Jerry', 'Tom'][total_apples & 1]))


if __name__ == '__main__':
    solution()