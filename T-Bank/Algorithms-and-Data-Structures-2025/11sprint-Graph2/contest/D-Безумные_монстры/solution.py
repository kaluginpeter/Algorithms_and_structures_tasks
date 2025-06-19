import sys


def solution() -> None:
    """
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    """
    n: int = int(sys.stdin.readline().rstrip())
    a: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    d: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    left: list[int] = list(range(-1, n-1))
    right: list[int] = list(range(1, n+1))
    right[-1] = -1
    alive: list[bool] = [True] * n
    current_candidates: set[int] = set(range(n))
    output: list[int] = [0] * n
    for round_num in range(n):
        if not current_candidates: break
        to_die: list[int] = []
        next_candidates: set[int] = set()
        
        for j in current_candidates:
            if not alive[j]: continue
            L: int = left[j]
            while L != -1 and not alive[L]: L = left[L]
            R: int = right[j]
            while R != -1 and not alive[R]: R = right[R]
            
            damage: int = 0
            if L != -1: damage += a[L]
            if R != -1: damage += a[R]
            if damage > d[j]: to_die.append(j)
        
        for j in to_die:
            alive[j] = False
            original_L: int = left[j]
            original_R: int = right[j]
            if original_L != -1:
                right[original_L] = original_R
                if alive[original_L]: next_candidates.add(original_L)
            
            if original_R != -1:
                left[original_R] = original_L
                if alive[original_R]: next_candidates.add(original_R)
        output[round_num] = len(to_die)
        current_candidates = next_candidates
    sys.stdout.write('{}\n'.format(' '.join(map(str, output))))

if __name__ == '__main__':
    solution()

