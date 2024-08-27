# A. Boredom
# time limit per test1 second
# memory limit per test256 megabytes
# Alex doesn't like boredom. That's why whenever he gets bored, he comes up with games. One long winter evening he came up with a game and decided to play it.
#
# Given a sequence a consisting of n integers. The player can make several steps. In a single step he can choose an element of the sequence (let's denote it ak) and delete it, at that all elements equal to ak + 1 and ak - 1 also must be deleted from the sequence. That step brings ak points to the player.
#
# Alex is a perfectionist, so he decided to get as many points as possible. Help him.
#
# Input
# The first line contains integer n (1 ≤ n ≤ 105) that shows how many numbers are in Alex's sequence.
#
# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 105).
#
# Output
# Print a single integer — the maximum number of points that Alex can earn.
#
# Examples
# inputCopy
# 2
# 1 2
# outputCopy
# 2
# inputCopy
# 3
# 1 2 3
# outputCopy
# 4
# inputCopy
# 9
# 1 2 1 3 2 2 2 2 3
# outputCopy
# 10
# Note
# Consider the third test example. At first step we need to choose any element equal to 2. After that step our sequence looks like this [2, 2, 2, 2]. Then we do 4 steps, on each step we choose any element equals to 2. In total we earn 10 points.
# Solution Dynamic Programming O(N) O(N)
from typing import List
import sys


def solution(n: int, scores: List[int]) -> str:
    modules: dict[int, int] = dict()
    for num in scores:
        modules[num] = modules.get(num, 0) + 1
    moves: List[int] = sorted(modules.keys())
    dp: List[int] = [0] * len(moves)
    dp[0] = moves[0] * modules[moves[0]]
    move_idx: int = 1
    if move_idx < len(moves) and moves[move_idx] - 1 == moves[0]:
        dp[move_idx] = max(dp[0], moves[move_idx] * modules[moves[move_idx]])
        move_idx += 1
    while move_idx < len(moves):
        cur_num: int = moves[move_idx]
        cur_weight: int = cur_num * modules[cur_num]
        if cur_num - 1 == moves[move_idx - 1]:
            dp[move_idx] = max(dp[move_idx - 1], cur_weight + dp[move_idx - 2])
        else:
            dp[move_idx] = max(dp[move_idx - 1], cur_weight + dp[move_idx - 1])
        move_idx += 1
    return str(max(dp))



if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    scores: List[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(n, scores))