/*
In the nation of CodeWars, there lives an Elder who has lived for a long time. Some people call him the Grandpatriarch, but most people just refer to him as the Elder.

There is a secret to his longetivity: he has a lot of young worshippers, who regularly perform a ritual to ensure that the Elder stays immortal:

The worshippers line up in a magic rectangle, of dimensions m and n.
They channel their will to wish for the Elder. In this magic rectangle, any worshipper can donate time equal to the xor of the column and the row (zero-indexed) he's on, in seconds, to the Elder.
However, not every ritual goes perfectly. The donation of time from the worshippers to the Elder will experience a transmission loss l (in seconds). Also, if a specific worshipper cannot channel more than l seconds, the Elder will not be able to receive this worshipper's donation.
The estimated age of the Elder is so old it's probably bigger than the total number of atoms in the universe. However, the lazy programmers (who made a big news by inventing the Y2K bug and other related things) apparently didn't think thoroughly enough about this, and so their simple date-time system can only record time from 0 to t-1 seconds. If the elder received the total amount of time (in seconds) more than the system can store, it will be wrapped around so that the time would be between the range 0 to t-1.

Given m, n, l and t, please find the number of seconds the Elder has received, represented in the poor programmer's date-time system.

(Note: t will never be bigger than 2^32 - 1, and in JS, 2^26 - 1.)

Example:

m=8, n=5, l=1, t=100

Let's draw out the whole magic rectangle:
0 1 2 3 4 5 6 7
1 0 3 2 5 4 7 6
2 3 0 1 6 7 4 5
3 2 1 0 7 6 5 4
4 5 6 7 0 1 2 3

Applying a transmission loss of 1:
0 0 1 2 3 4 5 6
0 0 2 1 4 3 6 5
1 2 0 0 5 6 3 4
2 1 0 0 6 5 4 3
3 4 5 6 0 0 1 2

Adding up all the time gives 105 seconds.

Because the system can only store time between 0 to 99 seconds, the first 100 seconds of time will be lost, giving the answer of 5.
This is no ordinary magic (the Elder's life is at stake), so you need to care about performance. All test cases (900 tests) can be passed within 1 second, but naive solutions will time out easily. Good luck, and do not displease the Elder.

PuzzlesDynamic ProgrammingPerformanceAlgorithms
*/
// Solution
#include <cstdint>
#include <algorithm>

uint64_t getPow(uint64_t n) {
    if (n == 0) return 1;
    uint64_t power = 1;
    while (power < n) power <<= 1;
    return power;
}

uint64_t rangeSumMod(uint64_t l, uint64_t r, uint64_t mod) {
    if (l > r) return 0;
    if (mod == 0) return 0;
    uint64_t M = 2 * mod;
    uint64_t l_mod = l % M;
    uint64_t r_mod = r % M;
    uint64_t A = (l_mod + r_mod) % M;
    uint64_t B = (r - l + 1) % M;
    uint64_t product = (A * B) % M;
    return product / 2;
}

int64_t elder_age(uint64_t m, uint64_t n, uint64_t l, uint64_t t) {
    if (t == 0) return 0;
    if (m == 0 || n == 0) return 0;
    if (m > n) std::swap(m, n);

    uint64_t lm = getPow(m);
    uint64_t ln = getPow(n);
    if (l >= ln) return 0;

    if (lm == ln) {
        uint64_t term1 = rangeSumMod(1, (ln > l ? ln - l - 1 : 0), t);
        term1 = (term1 * ((m + n - ln) % t)) % t;
        uint64_t term2 = elder_age(ln - n, lm - m, l, t);
        return (term1 + term2) % t;
    }

    lm = ln / 2;
    uint64_t low = (lm > l) ? (lm - l) : 0;
    uint64_t high = (ln > l) ? (ln - l - 1) : 0;
    if (low > high) {
        low = 0;
        high = 0;
    }
    uint64_t part1 = rangeSumMod(1, high, t);
    uint64_t part2 = rangeSumMod(low, high, t);

    uint64_t tmp = (part1 * (m % t)) % t;
    uint64_t subtract = (((ln - n) % t) * part2) % t;
    tmp = (tmp + t - subtract) % t;

    if (l <= lm) {
        uint64_t term3 = 1;
        term3 = (term3 * ((lm - l) % t)) % t;
        term3 = (term3 * ((lm - m) % t)) % t;
        term3 = (term3 * ((ln - n) % t)) % t;
        uint64_t term4 = elder_age(lm - m, ln - n, 0, t);
        tmp = (tmp + term3 + term4) % t;
    } else {
        uint64_t term4 = elder_age(lm - m, ln - n, l - lm, t);
        tmp = (tmp + term4) % t;
    }
    return tmp % t;
}