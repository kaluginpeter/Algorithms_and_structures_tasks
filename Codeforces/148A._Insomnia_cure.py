# A. Insomnia cure
# time limit per test2 seconds
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# «One dragon. Two dragon. Three dragon», — the princess was counting. She had trouble falling asleep, and she got bored of counting lambs when she was nine.
#
# However, just counting dragons was boring as well, so she entertained herself at best she could. Tonight she imagined that all dragons were here to steal her, and she was fighting them off. Every k-th dragon got punched in the face with a frying pan. Every l-th dragon got his tail shut into the balcony door. Every m-th dragon got his paws trampled with sharp heels. Finally, she threatened every n-th dragon to call her mom, and he withdrew in panic.
#
# How many imaginary dragons suffered moral or physical damage tonight, if the princess counted a total of d dragons?
#
# Input
# Input data contains integer numbers k, l, m, n and d, each number in a separate line (1 ≤ k, l, m, n ≤ 10, 1 ≤ d ≤ 105).
#
# Output
# Output the number of damaged dragons.
#
# Examples
# inputCopy
# 1
# 2
# 3
# 4
# 12
# outputCopy
# 12
# inputCopy
# 2
# 3
# 4
# 5
# 24
# outputCopy
# 17
# Note
# In the first case every first dragon got punched with a frying pan. Some of the dragons suffered from other reasons as well, but the pan alone would be enough.
#
# In the second case dragons 1, 7, 11, 13, 17, 19 and 23 escaped unharmed.
# Solution O(N) O(1) Math Simulation
import sys

def solution(k: int, l: int, m: int, n: int, d: int) -> str:
    suffered: int = 0
    punishments: list = [k, l, m, n]
    for dragon in range(1, d + 1):
        if any(dragon % punishment == 0 for punishment in punishments):
            suffered += 1
    return str(suffered)

if __name__ == '__main__':
    k: int = int(sys.stdin.readline().rstrip())
    l: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    n: int = int(sys.stdin.readline().rstrip())
    d: int = int(sys.stdin.readline().rstrip())
    sys.stdout.write(solution(k, l, m, n, d))