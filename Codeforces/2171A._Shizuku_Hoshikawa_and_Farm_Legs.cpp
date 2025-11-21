/*
A. Shizuku Hoshikawa and Farm Legs
time limit per test1 second
memory limit per test256 megabytes
Nothing's ever been the same since... that summer with her.
— Shizuku Hoshikawa
Kaori wants to spend the day with Shizuku! However, the zoo is closed, so they are visiting Farmer John's farm instead.

At Farmer John's farm, Shizuku counts n
 legs. It is known that only chickens and cows live on the farm; a chicken has 2
 legs, while a cow has 4
.

Count how many different configurations of Farmer John's farm are possible. Two configurations are considered different if they contain either a different number of chickens, a different number of cows, or both.

Note that Farmer John's farm may contain zero chickens or zero cows.

Input
The first line contains a single integer t
 (1≤t≤100
)  — the number of test cases.

The only line of each test case contains a single integer n
 (1≤n≤100
).

Output
For each test case, output a single integer, the number of different configurations of Farmer John's farm that are possible.

Example
InputCopy
5
2
3
4
6
100
OutputCopy
1
0
2
2
26
Note
For n=4
, there are two possible configurations of Farmer John's farm:

he can have two chickens and zero cows, or
he can have zero chickens and one cow.
It can be shown that these are the only possible configurations of Farmer John's farm.
For n=3
, it can be shown that there are no possible configurations of Farmer John's farm.
*/
// Solution
// C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    if (n & 1) {
        std::cout << "0\n";
        return;
    }
    std::cout << n / 4 + 1 << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}