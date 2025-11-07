/*
Don't give me five!
In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
The result may contain fives. ;-)
The start number will always be smaller than the end number. Both numbers can be also negative!

I'm very curious for your solutions and the way you solve it. Maybe someone of you will find an easy pure mathematics solution.

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!

MathematicsArraysAlgorithms
*/
// Solution
#include <bits/stdc++.h>
using namespace std;
#define ll long long

static ll F_nonneg(ll n) {
    if (n < 0) return 0;
    string s = to_string(n);
    int L = s.size();
    ll count = 0;
    vector<ll> pow9(L+1, 1);
    for (int i = 1; i <= L; ++i) pow9[i] = pow9[i-1] * 9LL;
    bool prefix_has_5 = false;
    for (int i = 0; i < L; ++i) {
        int d = s[i] - '0';
        int choices_less = 0;
        for (int dig = 0; dig < d; ++dig) if (dig != 5) ++choices_less;
        int remaining = L - i - 1;
        count += (ll)choices_less * pow9[remaining];
        if (d == 5) { prefix_has_5 = true; break; }
    }
    if (!prefix_has_5) count += 1;
    return count;
}

ll dontGiveMeFive(ll start, ll end) {
    if (end < 0) {
        ll a = -end;
        ll b = -start;
        return F_nonneg(b) - F_nonneg(a - 1);
    } else if (start >= 0) return F_nonneg(end) - F_nonneg(start - 1);
    else {
        ll neg_count = F_nonneg(-start) - F_nonneg(0);
        ll nonneg_count = F_nonneg(end);
        return neg_count + nonneg_count;
    }
}