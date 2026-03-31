/*
Buddy pairs
You know what divisors of a number are. The divisors of a positive integer n are said to be proper when you consider only the divisors other than n itself. In the following description, divisors will mean proper divisors. For example for 100 they are 1, 2, 4, 5, 10, 20, 25, and 50.

Let s(n) be the sum of these proper divisors of n. Call buddy two positive integers such that the sum of the proper divisors of each number is one more than the other number:

(n, m) are a pair of buddy if s(m) = n + 1 and s(n) = m + 1

For example 48 & 75 is such a pair:

Divisors of 48 are: 1, 2, 3, 4, 6, 8, 12, 16, 24 --> sum: 76 = 75 + 1
Divisors of 75 are: 1, 3, 5, 15, 25 --> sum: 49 = 48 + 1
Task
Given two positive integers start and limit, the function buddy(start, limit) should return the first pair (n m) of buddy pairs such that n (positive integer) is between start (inclusive) and limit (inclusive); m can be greater than limit and has to be greater than n

If there is no buddy pair satisfying the conditions, then return "Nothing" or (for Go lang) nil or (for Dart) null; (for Lua, Pascal, Perl, D) [-1, -1]; (for Erlang {-1, -1}).

Examples
(depending on the languages)

buddy(10, 50) returns [48, 75]
buddy(48, 50) returns [48, 75]
or
buddy(10, 50) returns "(48 75)"
buddy(48, 50) returns "(48 75)"
Notes
for C: The returned string will be free'd.
See more examples in "Sample Tests:" of your language.
FundamentalsMathematics
*/
// Solution
#include <string>
#include <cmath>

using namespace std;

namespace Bud
{
    long long sum_divisors(long long n) {
        if (n == 1) return 0;

        long long sum = 1;

        for (long long i = 2; i * i <= n; ++i) {
            if (n % i == 0) {
                sum += i;
                if (i != n / i)
                    sum += n / i;
            }
        }

        return sum;
    }

    string buddy(long long start, long long limit)
    {
        for (long long n = start; n <= limit; ++n) {
            long long s_n = sum_divisors(n);

            long long m = s_n - 1;

            if (m > n) {
                long long s_m = sum_divisors(m);
                if (s_m == n + 1) {
                    return "(" + to_string(n) + " " + to_string(m) + ")";
                }
            }
        }
        return "Nothing";
    }
}