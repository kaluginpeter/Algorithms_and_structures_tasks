/*
Consider the sequence a(1) = 7, a(n) = a(n-1) + gcd(n, a(n-1)) for n >= 2:

7, 8, 9, 10, 15, 18, 19, 20, 21, 22, 33, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 69, 72, 73....

Let us take the differences between successive elements of the sequence and get a second sequence g: 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1....

For the sake of uniformity of the lengths of sequences we add a 1 at the head of g:

g: 1, 1, 1, 1, 5, 3, 1, 1, 1, 1, 11, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 23, 3, 1...

Removing the 1s gives a third sequence: p: 5, 3, 11, 3, 23, 3... where you can see prime numbers.

Task:
Write functions:

1: an(n) with parameter n: returns the first n terms of the series of a(n) (not tested)

2: gn(n) with parameter n: returns the first n terms of the series of g(n) (not tested)

3: countOnes(n) with parameter n: returns the number of 1 in the series gn(n)
    (don't forget to add a `1` at the head) # (tested)

4:  p(n) with parameter n: returns an array filled with the n first distinct primes in the same order they are found in the sequence gn (not tested)

5: maxPn(n) with parameter n: returns the biggest prime number of the above p(n) # (tested)

6: anOver(n) with parameter n: returns an array (n terms) of the a(i)/i for every i such g(i) != 1 (not tested but interesting result)

7: anOverAverage(n) with parameter n: returns as an *integer* the average of anOver(n) # (tested)
Note:
You can write directly functions 3:, 5: and 7:. There is no need to write functions 1:, 2:, 4: 6: except out of pure curiosity.

FundamentalsMathematics
*/
// Solution
#include <bits/stdc++.h>
using namespace std;
vector<long long> a{0,7}, g{0,1}, pre{0,1}, p, sum;
unordered_set<long long> us{1};
class WeirdPrimeGen
{
    static bool ok(long long x) {
        if(us.count(x)) return false;
        us.insert(x);
        for(int i = 2; i * i <= x; i++) {
            if(x % i) continue;
            return false;
        }
        return true;
    }
    static void calc(long long n) {
        if(a.size() > n) return;
        calc(n-1);
        a.push_back(a.back() + __gcd(n, a.back()));
        g.push_back(a.back() - a[a.size()-2]);
        pre.push_back(pre.back() + (g.back() == 1));
        if(ok(g.back())) p.push_back(g.back());
        if(g.back() != 1) {
            sum.push_back((sum.size() ? sum.back() : 0) + a.back() / n);
        }
    }
public:
    static long long countOnes(long long n) {
        calc(n);
        return pre[n];
    }
    static long long maxPn(long long n) {
        while(p.size() < n) {
            calc(a.size());
        }
        long long res = 0;
        for(int i = 0; i < n; i++) res = max(res, p[i]);
        return res;
    }
    static int anOverAverage(long long n) {
        while(sum.size() < n) {
            calc(a.size());
        }
        return sum[n-1] / n;
    }
};