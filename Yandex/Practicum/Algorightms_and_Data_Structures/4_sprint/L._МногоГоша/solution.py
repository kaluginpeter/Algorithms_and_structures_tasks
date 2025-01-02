import sys

MOD1: int = 100000003
MOD2: int = 100000019
MOD3: int = 100000037
q1: int = 100000009
q2: int = 100000007
q3: int = 100000021


def solution() -> None:
    """
    Time Complexity O(N)
    Memory Complexity O(N)
    """
    n, k = map(int, sys.stdin.readline().rstrip().split())
    L: str = sys.stdin.readline().rstrip()
    hashmap: dict[tuple[int, int, int], list[int, int]] = dict()
    first: bool = True

    cur_hash1: int = 0
    cur_hash2: int = 0
    cur_hash3: int = 0
    q_pow_k1: int = pow(q1, n, MOD1)
    q_pow_k2: int = pow(q2, n, MOD2)
    q_pow_k3: int = pow(q3, n, MOD3)

    for i in range(len(L)):
        cur_hash1 = (cur_hash1 * q1 + ord(L[i])) % MOD1
        cur_hash2 = (cur_hash2 * q2 + ord(L[i])) % MOD2
        cur_hash3 = (cur_hash3 * q3 + ord(L[i])) % MOD3

        if i >= n - 1:
            if i >= n:
                cur_hash1 = (cur_hash1 - ord(L[i - n]) * q_pow_k1) % MOD1
                cur_hash2 = (cur_hash2 - ord(L[i - n]) * q_pow_k2) % MOD2
                cur_hash3 = (cur_hash3 - ord(L[i - n]) * q_pow_k3) % MOD3
            triplet: tuple[int, int, int] = (cur_hash1, cur_hash2, cur_hash3)
            if triplet not in hashmap:
                hashmap[triplet] = [0, i - n + 1]
            hashmap[triplet][0] += 1
            if hashmap[triplet][0] == k:
                if not first:
                    sys.stdout.write(' ')
                sys.stdout.write(str(hashmap[triplet][1]))
                first = False


if __name__ == '__main__':
    solution()