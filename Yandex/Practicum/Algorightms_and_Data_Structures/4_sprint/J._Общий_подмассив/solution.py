import sys

MOD1: int = 100000003
MOD2: int = 100000019
MOD3: int = 100000037
q1: int = 100000009
q2: int = 100000007
q3: int = 100000021


def has_common_substring_with_length_k(k: int, A: list[int], B: list[int]) -> bool:
    if k == 0:
        return True
    if len(A) < k or len(B) < k:
        return False

    pool: set[tuple[int, int, int]] = set()
    cur_hash1: int = 0
    cur_hash2: int = 0
    cur_hash3: int = 0
    q_pow_k1: int = pow(q1, k, MOD1)
    q_pow_k2: int = pow(q2, k, MOD2)
    q_pow_k3: int = pow(q3, k, MOD3)

    for idx in range(len(A)):
        cur_hash1 = (cur_hash1 * q1 + A[idx]) % MOD1
        cur_hash2 = (cur_hash2 * q2 + A[idx]) % MOD2
        cur_hash3 = (cur_hash3 * q3 + A[idx]) % MOD3

        if idx >= k - 1:
            if idx >= k:
                cur_hash1 = (cur_hash1 - A[idx - k] * q_pow_k1) % MOD1
                cur_hash2 = (cur_hash2 - A[idx - k] * q_pow_k2) % MOD2
                cur_hash3 = (cur_hash3 - A[idx - k] * q_pow_k3) % MOD3

            pool.add((cur_hash1, cur_hash2, cur_hash3))

    cur_hash1 = 0
    cur_hash2 = 0
    cur_hash3 = 0
    for idx in range(len(B)):
        cur_hash1 = (cur_hash1 * q1 + B[idx]) % MOD1
        cur_hash2 = (cur_hash2 * q2 + B[idx]) % MOD2
        cur_hash3 = (cur_hash3 * q3 + B[idx]) % MOD3

        if idx >= k - 1:
            if idx >= k:
                cur_hash1 = (cur_hash1 - B[idx - k] * q_pow_k1) % MOD1
                cur_hash2 = (cur_hash2 - B[idx - k] * q_pow_k2) % MOD2
                cur_hash3 = (cur_hash3 - B[idx - k] * q_pow_k3) % MOD3

            if (cur_hash1, cur_hash2, cur_hash3) in pool:
                return True

    return False


def solution() -> None:
    """
    Time Complexity O( (NM)log(min(N, M) )
    Memory Complexity O(max(N, M))
    """
    n: int = int(sys.stdin.readline().rstrip())
    A: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    m: int = int(sys.stdin.readline().rstrip())
    B: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))

    left: int = 0
    right: int = min(n, m)
    max_common: int = 0
    while left <= right:
        middle: int = left + ((right - left) >> 1)
        if has_common_substring_with_length_k(middle, A, B):
            max_common = middle
            left = middle + 1
        else:
            right = middle - 1
    sys.stdout.write(str(max_common) + '\n')


if __name__ == '__main__':
    solution()
