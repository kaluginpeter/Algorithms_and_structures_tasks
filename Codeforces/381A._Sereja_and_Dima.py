# A. Sereja and Dima
# time limit per test1 second
# memory limit per test256 megabytes
# Sereja and Dima play a game. The rules of the game are very simple. The players have n cards in a row. Each card contains a number, all numbers on the cards are distinct. The players take turns, Sereja moves first. During his turn a player can take one card: either the leftmost card in a row, or the rightmost one. The game ends when there is no more cards. The player who has the maximum sum of numbers on his cards by the end of the game, wins.
#
# Sereja and Dima are being greedy. Each of them chooses the card with the larger number during his move.
#
# Inna is a friend of Sereja and Dima. She knows which strategy the guys are using, so she wants to determine the final score, given the initial state of the game. Help her.
#
# Input
# The first line contains integer n (1 ≤ n ≤ 1000) — the number of cards on the table. The second line contains space-separated numbers on the cards from left to right. The numbers on the cards are distinct integers from 1 to 1000.
#
# Output
# On a single line, print two integers. The first number is the number of Sereja's points at the end of the game, the second number is the number of Dima's points at the end of the game.
#
# Examples
# inputCopy
# 4
# 4 1 2 10
# outputCopy
# 12 5
# inputCopy
# 7
# 1 2 3 4 5 6 7
# outputCopy
# 16 12
# Note
# In the first sample Sereja will take cards with numbers 10 and 2, so Sereja's sum is 12. Dima will take cards with numbers 4 and 1, so Dima's sum is 5.
# Solution Greedy Two Pointers O(N) O(1)
import sys


def solution(n: int, cards: list) -> str:
    dima: int = 0
    serj: int = 0
    flag: bool = True
    left: int = 0
    right: int = n - 1
    while left <= right:
        if cards[left] > cards[right]:
            current_card: int = cards[left]
            left += 1
        else:
            current_card: int = cards[right]
            right -= 1
        if flag:
            serj += current_card
        else:
            dima += current_card
        flag = not flag
    return f'{serj} {dima}'


if __name__ == '__main__':
    n: int = int(sys.stdin.readline().rstrip())
    cards: list = list(map(int, sys.stdin.readline().rstrip().split()))
    sys.stdout.write(solution(n, cards))