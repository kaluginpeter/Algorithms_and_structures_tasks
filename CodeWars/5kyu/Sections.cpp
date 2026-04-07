/*
Consider the following equation of a surface S: z*z*z = x*x * y*y.
Take a cross section of S by a plane P: z = k where k is a positive integer (k > 0).
Call this cross section C(k).

Task
Find the number of points of C(k) whose coordinates are positive integers.

Examples
If we call c(k) the function which returns this number we have

c(1) -> 1
c(4) -> 4
c(4096576) -> 160
c(2019) -> 0 which means that no point of C(2019) has integer coordinates.
Notes
k can go up to about 10,000,000,000 (1e10), so mind the time complexity of your code
Prolog: the function cis called section.
COBOL: the function cis called sections.
Visual Representation
Here is what the surface looks like in 3D:
*/
// Solution
#include <cmath>
namespace sections
{
    int c(long long k)
    {
        long long t = std::sqrt(k);
        if (t * t != k) return 0;
        long long n = t;
        int result = 1;
        for (long long i = 2; i * i <= n; ++i) {
            if (n % i == 0) {
                int count = 0;
                while (n % i == 0) {
                    n /= i;
                    count++;
                }
                result *= (3 * count + 1);
            }
        }
        if (n > 1) result *= 4;
        return result;
    }
}