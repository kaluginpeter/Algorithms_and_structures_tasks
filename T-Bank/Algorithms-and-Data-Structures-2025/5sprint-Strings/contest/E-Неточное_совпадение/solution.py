import sys


def compute_z_function(s: str) -> list[int]:
    n: int = len(s)
    z: list[int] = [0] * n
    l, r = 0, 0
    for i in range(1, n):
        if i <= r: z[i] = min(r - i + 1, z[i - l])
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1
        if i + z[i] - 1 > r: l, r = i, i + z[i] - 1
    return z


def solution() -> None:
    """
    Time Complexity O(|P| + |T|)
    Memory Complexity O(|P| + |T|)
    """
    p: str = sys.stdin.readline().rstrip()
    t: str = sys.stdin.readline().rstrip()
    s: str = p + '$' + t
    z: list[int] = compute_z_function(s)
    p_len: int = len(p)
    t_len: int = len(t)
    result: list[int] = []

    for i in range(t_len - p_len + 1):
        pos: int = p_len + 1 + i
        prefix: int = z[pos]
        if prefix >= p_len: result.append(i + 1)
        else:
            mismatch_count: int = 0
            remaining: int = min(p_len - prefix, len(s) - (pos + prefix))
            for j in range(remaining):
                if s[prefix + j] != s[pos + prefix + j]:
                    mismatch_count += 1
                    if mismatch_count > 1: break
            if mismatch_count <= 1: result.append(i + 1)

    sys.stdout.write('{}\n'.format(len(result)))
    if result: sys.stdout.write('{}\n'.format(' '.join(str(pos) for pos in result)))


if __name__ == '__main__':
    solution()