import sys


def solution() -> None:
    """
    Time Complexity O(N + M)
    Memory Complexity O(N + M)
    """
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    a_even: list[str] = []
    b_even: list[str] = []
    for letter in a:
        if (ord(letter) - 97) & 1: a_even.append(letter)
    for letter in b:
        if (ord(letter) - 97) & 1: b_even.append(letter)
    if a_even == b_even: sys.stdout.write('0\n')
    else: sys.stdout.write(['-1', '1'][a_even > b_even] + '\n')


if __name__ == '__main__':
    solution()