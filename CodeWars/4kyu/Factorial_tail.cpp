/*
The problem
How many zeroes are at the end of the factorial of 10? 10! = 3628800, i.e. there are 2 zeroes. 16! (or 0x10!) in hexadecimal would be 0x130777758000, which has 3 zeroes.

Scalability
Unfortunately, machine integer numbers has not enough precision for larger values. Floating point numbers drop the tail we need. We can fall back to arbitrary-precision ones - built-ins or from a library, but calculating the full product isn't an efficient way to find just the tail of a factorial. Calculating 100'000! in compiled language takes around 10 seconds. 1'000'000! would be around 10 minutes, even using efficient Karatsuba algorithm

Your task
is to write a function, which will find the number of zeroes at the end of (number) factorial in arbitrary radix = base for larger numbers.

base is an integer from 2 to 256
number is an integer from 1 to 1'000'000
Note Second argument: number is always declared, passed and displayed as a regular decimal number. If you see a test described as 42! in base 20 it's 4210 not 4220 = 8210.

Algorithms
*/
// Solution
#include <climits>
#include <vector>

int Zeroes(int base, int number)
{
    std::vector<std::pair<int,int>> factors;
    for (int p = 2; p * p <= base; ++p) {
        if (base % p) continue;
        int cnt = 0;
        while (base % p == 0) {
            base /= p;
            ++cnt;
        }
        factors.push_back({p, cnt});
    }
    if (base > 1) factors.push_back({base, 1});
    int ans = INT_MAX;
    for (auto [p, need] : factors) {
        long long have = 0;
        long long pw = p;
        while (pw <= number) {
            have += number / pw;
            if (pw > number / p) break;
            pw *= p;
        }
        ans = std::min(ans, static_cast<int>(have / need));
    }

    return ans;
}