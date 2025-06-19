import sys


def solution() -> None:
    """
    Time Complexity O(|a| + |b|)
    Memory Complexity O(|a| + |b|)
    """
    a: str = sys.stdin.readline().rstrip()
    b: str = sys.stdin.readline().rstrip()
    k: int = len(b)
    if k > len(a):
        sys.stdout.write('-1\n')
        return
    q1, m1 = 100000009, 100000003
    q2, m2 = 100000007, 100000019
    hashmap: dict[int, dict[int, int]] = dict()
    prefix_sum1: list[int] = [0]
    prefix_sum2: list[int] = [0]
    h1 = h2 = 0
    for i in range(2 * k - 1):
        h1 = (h1 * q1 + ord(b[i % k])) % m1
        h2 = (h2 * q2 + ord(b[i % k])) % m2
        if i + 1 >= k:
            if h1 not in hashmap: hashmap[h1] = dict()
            if h2 not in hashmap[h1]: hashmap[h1][h2] = 0
            if i >= k:
                q_pow1: int = pow(q1, k, m1)
                q_pow2: int = pow(q2, k, m2)
                hash_code1: int = (h1 - prefix_sum1[i - k + 1] * q_pow1 % m1 + m1) % m1
                hash_code2: int = (h2 - prefix_sum2[i - k + 1] * q_pow2 % m2 + m2) % m2
                if hash_code1 not in hashmap: hashmap[hash_code1] = dict()
                if hash_code2 not in hashmap[hash_code1]: hashmap[hash_code1][hash_code2] = 0 
                hashmap[hash_code1][hash_code2] += 1
            else:
                hashmap[h1][h2] += 1
        prefix_sum1.append(h1)
        prefix_sum2.append(h2)
    output: int = 0 
    prefix_sum1 = [0]
    prefix_sum2 = [0]
    h1 = h2 = 0
    for i in range(len(a)):
        h1 = (h1 * q1 + ord(a[i])) % m1
        h2 = (h2 * q2 + ord(a[i])) % m2
        if i + 1 >= k:
            if i >= k:
                q_pow1: int = pow(q1, k, m1)
                q_pow2: int = pow(q2, k, m2)
                hash_code1: int = (h1 - prefix_sum1[i - k + 1] * q_pow1 % m1 + m1) % m1
                hash_code2: int = (h2 - prefix_sum2[i - k + 1] * q_pow2 % m2 + m2) % m2
                if hash_code1 in hashmap and hash_code2 in hashmap[hash_code1]: output += 1
            else:
                if h1 in hashmap and h2 in hashmap[h1]: output += 1
                
        prefix_sum1.append(h1)
        prefix_sum2.append(h2)
    sys.stdout.write('{}\n'.format(output))


if __name__ == '__main__':
    solution()