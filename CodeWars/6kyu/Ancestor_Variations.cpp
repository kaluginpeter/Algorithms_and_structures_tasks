/*
Description
You have a father, a grandfather, a great-grandfather, great-great-grandfather, etc...

Let's say:

0 = father
1 = grandfather
2 = great-grandfather
3 = great-great-grandfather
...
n = great-great-great- ... (n-1 times) -grandfather
Given any number n, how many different ways can I call n?

Since the answer can be very large, return it modulo 1000000007

Example
n = 2

We know that 2 = great-grandfather

Answer: There's 4 different ways I can call my great-grandfather.

Explanation
My great-grandfather
The father of my grandfather
The father of the father of my father
The grandfather of my father
Constraint
0 <= n <= 10^18

AlgorithmsMathematics
*/
// Solution
#include <bits/stdc++.h>
using namespace std;

static const long long MOD = 1000000007;

long long modpow(long long base, long long exp) {
    long long result = 1;
    base %= MOD;
    while (exp > 0) {
        if (exp & 1) result = (result * base) % MOD;
        base = (base * base) % MOD;
        exp >>= 1;
    }
    return result;
}

int ancestor_variations(long long n) {
    return modpow(2, n);
}