/*
In number theory, the Carmichael function of a positive integer n, denoted λ(n), is defined as the smallest positive integer m such that

a^m = 1 mod [n]
for every integer a ≤ n that is coprime to n. The Carmichael function is also known as the reduced totient function (as it is linked to Euler Totient function) or the least universal exponent function. The Carmichael function is important in number theory.

For example let n = 8. The list of integer a ≤ 8, coprime to 8: 1, 3, 5, 7.

1^1 = 1 mod [8]
3^1 = 3 mod [8]
So λ(8) > 1.

1^2 = 1 = 1 mod [8]
3^2 = 9 = 1 mod [8]
5^2 = 25 = 1 mod [8]
7^2 = 49 = 1 mod [8]
So λ(8) = 2.

There is generally two approach to this function:

Iteratively checking a^m ?= 1 mod [n] for growing m and every a ≤ n, coprime to n. This may not work for big numbers.

Using an exact formula like for Euler Totient. This is an explicit formula for calculating λ(n) depending on the prime decomposition of n.

For the second method the formula is deduced from the lcm formula for λ and the totient function (see the associated kata):

lcm formula, where p1,...,pn are the prime factor of n, w1,...,wn, the powers associated.:

λ(n) = λ(p1^w1 * p2^w2 * ... * pn^wn)
λ(n) = lcm(λ(p1^w1),λ(p2^w2),...,λ(pn^wn))
Then for p prime, we have a link between λ(p^w) and φ(p^w), the Euler Totient function:

if p is prime:
λ(p^w) =  φ(p^w)               if p>2
λ(p^w) =  φ(p^w)               if ( p=2 and w<3 )
λ(p^w) = 1/2 * φ(p^w)           if ( p=2 and w>=3)
You have to code Carmichael function, that take an integer 1 ≤ n as input and return λ(n). You also have to check if n is a number, integer and that 1 ≤ n, if it is not the case, the function should return 0.

Input range: 1 ≤ n ≤ 1e10

Algorithms
*/
// Solution
#include <numeric>   // std::gcd
#include <cmath>

long long lcm(long long a, long long b) // pure math
{
    return a / std::gcd(a, b) * b;
}

long long Carmichael(long long n)
{
    if (n < 1) return 0;
    if (n == 1) return 1;

    long long output = 1;
    long long temp = n;

    for (long long p = 2; p * p <= temp; p += (p == 2 ? 1 : 2)) // sieve
    {
        if (temp % p == 0)
        {
            long long w = 0;
            while (temp % p == 0)
            {
                temp /= p;
                ++w;
            }
            long long phi = (p - 1);
            for (int i = 1; i < w; ++i) phi *= p;

            long long lambda;
            if (p == 2 && w >= 3) lambda = phi / 2;
            else lambda = phi;

            output = lcm(output, lambda);
        }
    }
    if (temp > 1)
    {
        long long p = temp;
        long long phi = p - 1;
        output = lcm(output, phi);
    }
    return output;
}