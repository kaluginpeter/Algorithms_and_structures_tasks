import sys


keyboard: dict[str, str] = {
    '2' : 'abc', '3' : 'def', '4' : 'ghi',
    '5' : 'jkl', '6' : 'mno', '7' : 'pqrs',
    '8' : 'tuv', '9' : 'wxyz'
}


printed_first_time: bool = False


def backtracking(idx: int, buttons: str, typing: list[str]) -> None:
    n: int = len(buttons)
    if idx == n:
        global printed_first_time
        if printed_first_time:
            sys.stdout.write(' ')
        sys.stdout.write(''.join(typing))
        printed_first_time = True
        return
    button: str = buttons[idx]
    for key in keyboard[button]:
        typing.append(key)
        backtracking(idx + 1, buttons, typing)
        typing.pop()


def solution(buttons: str) -> None:
    """
    Time Complexity O(N**K), where N is length of buttons and K is number of keyboards
    Memory Complexity O(N)
    """
    printed_first_time = False
    backtracking(0, buttons, [])


if __name__ == '__main__':
    buttons: str = sys.stdin.readline().rstrip()
    solution(buttons)

