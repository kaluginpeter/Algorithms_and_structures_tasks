import sys


def solution(braces: str) -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    stack: list[str] = []
    valid_open_braces: dict[str, str] = {
        ')': '(', ']': '[', '}': '{',
    }
    is_valid: bool = True
    for brace in braces:
        if brace in '([{':
            stack.append(brace)
        else:
            if not stack or stack[-1] != valid_open_braces[brace]:
                is_valid = False
                break
            stack.pop()
    sys.stdout.write(["False", "True"][is_valid and not stack] + '\n')

if __name__ == '__main__':
    braces: str = sys.stdin.readline().rstrip()
    solution(braces)
