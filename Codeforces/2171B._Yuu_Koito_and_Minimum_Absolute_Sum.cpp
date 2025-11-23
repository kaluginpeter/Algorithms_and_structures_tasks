/*
B. Yuu Koito and Minimum Absolute Sum
time limit per test2 seconds
memory limit per test256 megabytes
The words in shoujo manga and love songs... they're always sparkling brightly. I don't need a dictionary to understand the meaning... but I've never felt them for myself.
— Yuu Koito
Yuu is trying out the student council! Unfortunately, she is being forced to do clerical work... Touko wants her to fill out the blanks in various student council documents.

You are given a partially filled array of nonnegative integers a1,a2,…,an
, where blank elements are denoted with −1
. You would like to fill in the blank elements with nonnegative integers, such that the absolute value of the sum of the elements in its difference array is minimized.

More formally, let b
 be the array of length n−1
 such that bi=ai+1−ai
 for all 1≤i≤n−1
. Find the minimum possible value of |b1+b2+⋯+bn−1|
, across all possible ways to fill in the blank elements of a
.

Additionally, output the array that achieves this minimum. If there are multiple such arrays, output the one that is lexicographically smallest∗
.

∗
For two arbitrary arrays c
 and d
 of length n
, we say that c
 is lexicographically smaller than d
 if there exists an index i
 (1≤i≤n
) such that cj=dj
 for all j<i
, and ci<di
. In other words, c
 and d
 differ in at least one index, and at the first index at which they differ, ci
 is smaller than di
.

Input
The first line contains a single integer t
 (1≤t≤104
)  — the number of test cases.

The first line of each test case contains a single integer n
 (2≤n≤2⋅105
).

The second line of each test case contains n
 integers, a1,a2,…,an
 (−1≤ai≤106
).

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, on the first line, output the minimum possible value of |b1+b2+⋯+bn−1|
. Then, on the second line, output n
 integers, the values of a1,a2,…,an
 in the lexicographically smallest array achieving this minimum.

Example
InputCopy
6
4
2 -1 7 1
4
-1 2 4 -1
8
2 -1 1 5 11 12 1 -1
3
-1 -1 -1
3
2 5 4
2
-1 5
OutputCopy
1
2 0 7 1
0
0 2 4 0
0
2 0 1 5 11 12 1 2
0
0 0 0
2
2 5 4
0
5 5
Note
In the first example, we fill in the array a=[2,0,7,1]
, which yields the difference array b=[−2,7,−6]
.

The absolute value of the sum of the elements in b
 is 1
. It can be proven that this is the minimum possible. Furthermore, it can be proven that this is the lexicographically smallest array a
 that achieves this minimum.
*/
// Solution
// C++ O(N) O(N) Greedy
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector <int> a;
    for (size_t i = 0; i < n; ++i) {
        int value;
        std::cin >> value;
        a.push_back(value);
    }
    for (size_t i = 0; i < n; ++i) {
        if (a[i] == -1) {
            if (i == 0) {
                if (a[n - 1] != -1) a[i] = a[n - 1];
                if (a[n - 1] == -1) a[i] = 0;
            }
            if (i == n - 1) a[n - 1] = a[0];
            if (i != n - 1 && i != 0) a[i] = 0;
        }
    }
    std::vector <int> b;
    for (size_t i = 0; i < n - 1; ++i) b.push_back(a[i+1] - a[i]);
    std::cout << abs(a[n-1] - a[0]) << std::endl;
    for (int i = 0; i < n; ++i) std::cout << a[i] << " ";
    std::cout << std::endl;
}



int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}