# A. Almost Prime
# time limit per test2 seconds
# memory limit per test256 megabytes
# A number is called almost prime if it has exactly two distinct prime divisors. For example, numbers 6, 18, 24 are almost prime, while 4, 8, 9, 42 are not. Find the amount of almost prime numbers which are between 1 and n, inclusive.
#
# Input
# Input contains one integer number n (1 ≤ n ≤ 3000).
#
# Output
# Output the amount of almost prime numbers between 1 and n, inclusive.
#
# Examples
# InputCopy
# 10
# OutputCopy
# 2
# InputCopy
# 21
# OutputCopy
# 8
# Solution
# C++ O(N * Nsqrt(N)) O(1) Math BruteForce
#include <iostream>
#include <cmath>


bool isPrime(int n) {
    int bound = std::sqrt(n) + 1;
    for (int d = 2; d <= bound; ++d) {
        if (d == n) continue;
        if (n % d == 0) return false;
    }
    return true;
}


bool isAlmostPrime(int n) {
    int divisors = 0;
    for (int d = 2; d <= n / 2 + 1; ++d) {
        if (n % d == 0) {
            if (isPrime(d)) ++divisors;
        }
    }
    return divisors == 2;
}


void solution() {
    int n;
    std::scanf("%d", &n);
    int almostPrime = 0;
    for (int num = 6; num <= n; ++num) {
        if (isAlmostPrime(num)) ++almostPrime;
    }
    std::printf("%d\n", almostPrime);
}


int main() {
    solution();
}

# Python O(N * Nsqrt(N)) O(1) Math BruteForce
import sys


def is_prime(n: int) -> bool:
    bound: int = int(n**.5) + 1
    return all(n % d != 0 for d in range(2, bound))


def is_almost_prime(n: int) -> bool:
    divisors: int = 0
    for d in range(2, n // 2 + 1):
        if d == n: continue
        elif n % d == 0 and is_prime(d): divisors += 1
    return divisors == 2


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    almost_primes: int = 0
    for num in range(6, n + 1):
        if is_almost_prime(num): almost_primes += 1
    sys.stdout.write('{}\n'.format(almost_primes))


if __name__ == '__main__':
    solution()