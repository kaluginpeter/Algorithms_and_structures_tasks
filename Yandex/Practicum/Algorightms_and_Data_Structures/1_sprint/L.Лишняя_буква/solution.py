import sys


def solution(x: str, y: str) -> None:
    """
    Time Complexity O(XlogX + YlogY)
    Memory Complexity O(1)
    """
    x_list: list[str] = sorted(x)
    y_list: list[str] = sorted(y)
    x_idx: int = 0
    y_idx: int = 0
    x_length: int = len(x)
    y_length: int = len(y)
    while x_idx < x_length and y_idx < y_length:
        if x_list[x_idx] != y_list[y_idx]:
            sys.stdout.write(y_list[y_idx] + '\n')
            return
        x_idx += 1
        y_idx += 1
    sys.stdout.write(y_list[y_idx] + '\n')


if __name__ == '__main__':
    x: str = sys.stdin.readline().rstrip()
    y: str = sys.stdin.readline().rstrip()
    solution(x, y)



import sys


def solution(x: str, y: str) -> None:
    """
    Time Complexity O(X + Y)
    Memory Complexity O({X} + {Y})
    """
    x_hashset: dict[str, int] = dict()
    y_hashset: dict[str, int] = dict()
    for letter in x:
        x_hashset[letter] = x_hashset.get(letter, 0) + 1
    for letter in y:
        y_hashset[letter] = y_hashset.get(letter, 0) + 1
    for letter in y_hashset:
        if letter not in x_hashset or y_hashset[letter] != x_hashset[letter]:
            sys.stdout.write(letter + '\n')


if __name__ == '__main__':
    x: str = sys.stdin.readline().rstrip()
    y: str = sys.stdin.readline().rstrip()
    solution(x, y)


