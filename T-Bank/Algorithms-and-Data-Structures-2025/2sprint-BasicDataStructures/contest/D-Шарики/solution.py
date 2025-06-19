import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    stack: list[list[int, int]] = []
    deletions: int = 0
    for _ in range(n):
        num: int = next(nums)
        if not stack or stack[-1][0] != num:
            if stack and stack[-1][-1] > 2:
                deletions += stack.pop()[-1]
                if stack and stack[-1][0] == num:
                    stack[-1][-1] += 1
                else: stack.append([num, 1])
            else: stack.append([num, 1])
        else: stack[-1][-1] += 1
    if stack and stack[-1][-1] > 2: deletions += stack[-1][-1]
    sys.stdout.write('{}\n'.format(deletions))


if __name__ == '__main__':
    solution()