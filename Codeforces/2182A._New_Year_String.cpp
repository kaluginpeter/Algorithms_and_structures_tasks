/*
A. New Year String
time limit per test2 seconds
memory limit per test512 megabytes
We will call a string consisting of characters 0, 2, 5, and/or 6 a New Year string if at least one of the two conditions is met:

it contains the string 2026 as a continuous substring;
it does not contain the string 2025 as a continuous substring.
For example, the strings 20252026, 21026, 20262026, 000 are New Year strings. The strings 2025, 20256, 20252025, 000202500020226 are not New Year strings.

You are given a string s
. You can perform the following operation any number of times (possibly zero):

choose a character in the string s
 and replace it with 0, 2, 5, or 6 (you can choose any one of these four characters).
Calculate the minimum number of operations needed to make the string s
 a New Year string.

Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer n
 (4≤n≤20
) — the number of characters in s
;
the second line contains s
 — a sequence of n
 characters 0, 2, 5, and/or 6.
Output
For each test case, output one integer — the minimum number of operations needed to make the string s
 a New Year string.

Example
InputCopy
7
4
0000
4
2025
4
2026
8
20252026
8
20252025
9
202520256
9
202520265
OutputCopy
0
1
0
0
1
1
0
Note
In the second example from the statement, you can replace the 2
-nd character of the string with 2. Then the string will become 2225.

In the fifth example from the statement, you can replace the 4
-th character with 6. Then the string will become 20262025.

In the sixth example from the statement, you can replace the 8
-th character with 6. Then the string will become 202520266.
*/
// Solution
// C++ O(N) O(1) Greedy String
#include <iostream>
#include <string>

void solution() {
    int n;
    std::cin >> n;
    std::string sequence, pat = "2025";
    std::cin >> sequence;
    std::cout << (sequence.find(pat) != std::string::npos ? sequence.find("2026") != std::string::npos ? 0 : 1 : 0) << "\n";
}

int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}