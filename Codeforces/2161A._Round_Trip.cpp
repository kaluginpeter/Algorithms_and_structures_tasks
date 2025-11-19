/*
A. Round Trip
time limit per test1 second
memory limit per test512 megabytes
They say that if you do 1000 rounds, there's a secret cartoon in the end (c)
Petya and Vasya love participating in Codeforces contests. Vasya made a bet with Petya that he will take part in more rated rounds than him. Initially, Vasya's rating is R0
. There will be n
 rounds conducted in total, each of one of two types:

div. 1 — rated for all participants
div. 2 — rated for participants with rating strictly less than X
, and unrated for all others,
In an unrated round, Vasya cannot change his rating. If Vasya's rating before a rated round was R
, then for any non-negative integer x
 between R−D
 and R+D
 (inclusive) Vasya can adopt a strategy such that his rating becomes exactly x
 afterwards (here D
 is a positive integer). Note that rating may never become negative.

Help Vasya determine the maximum number of rated rounds he can participate in.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤1000
). The description of the test cases follows.

The first line of each test case contains four integers: R0,X,D,n
 (0≤R0≤109
, 1≤X≤109
, 1≤D,n≤1000
) — Vasya's initial rating, the rating threshold between divisions, the maximum rating delta, and the number of rounds.

The second line of each test case contains a string of size n
. The string will only contain the characters "1" and "2", representing div. 1 and div. 2 rounds respectively.

The sum of n
 across all test cases does not exceed 3⋅104
.

Output
For each test case, print a single integer — the maximum number of rated rounds Vasya can participate in.

Example
InputCopy
4
2100 2100 5 3
222
2098 2100 5 6
111211
2115 2100 226 7
2211121
0 10 4 8
22111121
OutputCopy
0
6
5
8
Note
In the first example, since R0≥X
, each div. 2 round is unrated for Vasya, so his rating never changes. Therefore, he cannot make any round rated for himself, and the answer is 0
.

In the second example, one of the optimal sequences of ratings after each round is: 2098→2103→2101→2099→2097→2097→2092
.
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    int r0, x, d, n;
    std::cin >> r0 >> x >> d >> n;
    int output = 0;
    for (size_t i = 0; i < n; ++i) {
        char match;
        std::cin >> match;
        if (match == '1') {
            ++output;
            r0 = std::max(0, r0 - d);
        } else {
            if (r0 < x) {
                ++output;
                r0 = std::min(0, r0 - d);
            }
        }
    }
    std::cout << output << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}