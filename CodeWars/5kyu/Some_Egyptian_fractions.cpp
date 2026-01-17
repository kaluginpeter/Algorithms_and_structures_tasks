/*
Given a rational number n

 n >= 0, with denominator strictly positive

as a string (example: "2/3" in Ruby, Python, Clojure, JS, CS, Go)
or as two strings (example: "2" "3" in Haskell, Java, CSharp, C++, Swift, Dart)
or as a rational or decimal number (example: 3/4, 0.67 in R)
or two integers (Fortran)
decompose this number as a sum of rationals with numerators equal to one and without repetitions (2/3 = 1/2 + 1/6 is correct but not 2/3 = 1/3 + 1/3, 1/3 is repeated).

The algorithm must be "greedy", so at each stage the new rational obtained in the decomposition must have a denominator as small as possible. In this manner the sum of a few fractions in the decomposition gives a rather good approximation of the rational to decompose.

2/3 = 1/3 + 1/3 doesn't fit because of the repetition but also because the first 1/3 has a denominator bigger than the one in 1/2 in the decomposition 2/3 = 1/2 + 1/6.

Example:
(You can see other examples in "Sample Tests:")

decompose("21/23") or "21" "23" or 21/23 should return

["1/2", "1/3", "1/13", "1/359", "1/644046"] in Ruby, Python, Clojure, JS, CS, Haskell, Go, Scala

"[1/2, 1/3, 1/13, 1/359, 1/644046]" in Java, CSharp, C++, Dart

"1/2,1/3,1/13,1/359,1/644046" in C, Swift, R
Notes
The decomposition of 21/23 as

21/23 = 1/2 + 1/3 + 1/13 + 1/598 + 1/897
is exact but don't fulfill our requirement because 598 is bigger than 359. Same for

21/23 = 1/2 + 1/3 + 1/23 + 1/46 + 1/69 (23 is bigger than 13)
or
21/23 = 1/2 + 1/3 + 1/15 + 1/110 + 1/253 (15 is bigger than 13).
The rational given to decompose could be greater than one or equal to one, in which case the first "fraction" will be an integer (with an implicit denominator of 1).

If the numerator parses to zero the function "decompose" returns [] (or "",, or "[]").

The number could also be a decimal which can be expressed as a rational.

Example:
0.6 in Ruby, Python, Clojure,JS, CS, Julia, Go

"66" "100" in Haskell, Java, CSharp, C++, C, Swift, Scala, Kotlin, Dart, ...

0.67 in R.

Ref: http://en.wikipedia.org/wiki/Egyptian_fraction

AlgorithmsMathematics
*/
// Solution
#include <string>
#include <vector>
#include <numeric>
#include <sstream>

class Decomp
{
public:
    static std::string decompose(const std::string &nrStr, const std::string &drStr)
    {
        long long n = std::stoll(nrStr);
        long long d = std::stoll(drStr);

        if (n == 0) return "[]";

        std::vector<std::string> result;
        if (n >= d)
        {
            long long integerPart = n / d;
            result.push_back(std::to_string(integerPart));
            n %= d;
            if (n == 0) return format(result);
        }
        while (n != 0)
        {
            long long k = (d + n - 1) / n;
            result.push_back("1/" + std::to_string(k));

            n = n * k - d;
            d = d * k;
            long long g = std::gcd(n, d);
            n /= g;
            d /= g;
        }

        return format(result);
    }

private:
    static std::string format(const std::vector<std::string> &parts)
    {
        std::ostringstream out;
        out << "[";
        for (size_t i = 0; i < parts.size(); ++i)
        {
            out << parts[i];
            if (i + 1 < parts.size()) out << ", ";
        }
        out << "]";
        return out.str();
    }
};