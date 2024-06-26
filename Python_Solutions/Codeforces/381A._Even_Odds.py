# A. Even Odds
# time limit per test1 second
# memory limit per test256 megabytes
# inputstandard input
# outputstandard output
# Being a nonconformist, Volodya is displeased with the current state of things, particularly with the order of natural numbers (natural number is positive integer number). He is determined to rearrange them. But there are too many natural numbers, so Volodya decided to start with the first n. He writes down the following sequence of numbers: firstly all odd integers from 1 to n (in ascending order), then all even integers from 1 to n (also in ascending order). Help our hero to find out which number will stand at the position number k.
#
# Input
# The only line of input contains integers n and k (1 ≤ k ≤ n ≤ 1012).
#
# Please, do not use the %lld specifier to read or write 64-bit integers in C++. It is preferred to use the cin, cout streams or the %I64d specifier.
#
# Output
# Print the number that will stand at the position number k after Volodya's manipulations.
#
# Examples
# inputCopy
# 10 3
# outputCopy
# 5
# inputCopy
# 7 7
# outputCopy
# 6
# Note
# In the first sample Volodya's sequence will look like this: {1, 3, 5, 7, 9, 2, 4, 6, 8, 10}. The third place in the sequence is therefore occupied by the number 5.
# Solution Math O(1) O(1)
import sys

def solution(n: int, k: int) -> str:
    odd = (n + 1) // 2
    even = n // 2
    if k <= odd:
        return str(1 + (k - 1)*2)
    k -= odd
    return str(2 + (k - 1) * 2)

if __name__ == '__main__':
    n, k = map(int, sys.stdin.readline().rstrip().split())
    sys.stdout.write(solution(n, k))