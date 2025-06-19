import sys


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    sequence: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    prefix_sum: list[int] = [0]
    nums: list[int] = []
    for _ in range(n):
        num: int = next(sequence)
        prefix_sum.append(prefix_sum[-1] + num)
        nums.append(num)
    
    stack: list[int] = []
    segments: list[list[int, int]] = []
    for idx in range(n):
        while stack and nums[stack[-1]] >= nums[idx]:
            segments[stack.pop()][1] = idx
        if not stack: segments.append([-1, n])
        else: segments.append([stack[-1], n])
        stack.append(idx)
    answer: int = 0
    for i in range(n):
        left: int = segments[i][0] + 1 
        right: int = segments[i][1]
        part: int = (prefix_sum[right] - prefix_sum[left]) * nums[i]
        answer = max(answer, part)
    sys.stdout.write(f'{answer}\n')


if __name__ == '__main__':
    solution()