import sys


def solution(k: int, bucket: list[int]) -> int:
    """
    Time Complexity O(NM)
    Memory Complexity O(M)
    Topics: Matrix, Counting
    """
    score: int = 0
    n: int = len(bucket)
    for chunk in range(n):
        if bucket[chunk] and bucket[chunk] <= k * 2:
            score += 1
    return score


if __name__ == '__main__':
    k: int = int(sys.stdin.readline().rstrip())
    bucket: list[int] = [0] * 10
    for _ in range(4):
        row: str = sys.stdin.readline().rstrip()
        for element in row:
            if element != '.':
                bucket[int(element)] += 1
    sys.stdout.write(str(solution(k, bucket)) + '\n')
