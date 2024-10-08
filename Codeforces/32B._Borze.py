# B. Borze
# time limit per test2 seconds
# memory limit per test256 megabytes
# Ternary numeric notation is quite popular in Berland. To telegraph the ternary number the Borze alphabet is used. Digit 0 is transmitted as «.», 1 as «-.» and 2 as «--». You are to decode the Borze code, i.e. to find out the ternary number given its representation in Borze alphabet.
#
# Input
# The first line contains a number in Borze code. The length of the string is between 1 and 200 characters. It's guaranteed that the given string is a valid Borze code of some ternary number (this number can have leading zeroes).
#
# Output
# Output the decoded ternary number. It can have leading zeroes.
#
# Examples
# inputCopy
# .-.--
# outputCopy
# 012
# inputCopy
# --.
# outputCopy
# 20
# inputCopy
# -..-.--
# outputCopy
# 1012
# Solution Simulation HashMap O(N) O(N)
import sys


def solution(n: str) -> str:
    operations: dict[str, tuple[int, int]] = {'.': ('0', 1), '-.': ('1', 2), '--': ('2', 2)}
    decoded: list[str] = []
    idx: int = 0
    while idx < len(n):
        for operation in operations:
            if n[idx: idx + 2] == operation or n[idx: idx + 1] == operation:
                digit, move = operations[operation]
                decoded.append(digit)
                idx += move
    return ''.join(decoded)

if __name__ == '__main__':
    n: str = sys.stdin.readline().rstrip()
    sys.stdout.write(solution(n))
