/*
C. Replace and Sum
time limit per test2 seconds
memory limit per test256 megabytes
Today, KQ has an exam at the Grail Academy. A strict teacher gave a task that KQ could not solve. He was given two arrays a
 and b
 of length n
. KQ is allowed to perform the following operations on the arrays:

Choose an index i
 (1≤i<n
) and replace ai
 with ai+1
.
Choose an index i
 (1≤i≤n
) and replace ai
 with bi
.
Now he has q
 queries. Each query is described by two numbers l
 and r
. His task is to find the maximum value of the sum (al+al+1+al+2+⋯+ar)
 for each query, if he can perform any number of operations on any elements of the array. Since he is not skilled enough for this, he asks for your help.
Input
Each test consists of several test cases. The first line contains one integer t
 (1≤t≤104
) — the number of test cases. The description of the test cases follows.

The first line of each test case contains two integers n
, q
 (1≤n,q≤2⋅105)
.

The second line of each test case contains n
 integers a1,a2,...,an
 (1≤ai≤104)
.

The third line of each test case contains n
 integers b1,b2,...,bn
 (1≤bi≤104)
.

The following q
 lines contain two integers l
 and r
 (1≤l≤r≤n)
.

It is guaranteed that the sum of the values of n
 and the sum of the values of q
 across all test cases do not exceed 2⋅105
.

Output
For each test case, output q
 numbers separated by spaces — the maximum values of the sums (al+al+1+al+2+⋯+ar)
.

Example
InputCopy
4
3 1
3 2 1
1 2 3
1 3
1 1
1
2
1 1
3 2
6 7 5
9 6 8
1 2
2 3
4 3
4 3 2 1
5 1 3 1
1 2
2 4
3 4
OutputCopy
9
2
17 16
8 7 4
Note
Consider the first test case. Replace a3
 with b3
, a=[3,2,3]
. Replace a2
 with a3
, a=[3,3,3]
. The sum a1+a2+a3=9
.
*/
// Solution
// C++ O(N) O(N) PrefixSum Greedy
#include <iostream>
#include <vector>


void solution() {
    size_t n, q;
    std::cin >> n >> q;
    std::vector<int> a(n, 0), b(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> a[i];
    for (size_t i = 0; i < n; ++i) std::cin >> b[i];
    for (size_t i = n; i > 0; --i) {
        if (i < n && a[i] > a[i - 1]) a[i - 1] = a[i];
        if (b[i - 1] > a[i - 1]) a[i - 1] = b[i - 1];
    }
    std::vector<int> prefix = {0};
    for (size_t i = 0; i < n; ++i) prefix.push_back(prefix.back() + a[i]);
    for (size_t i = 0; i < q; ++i) {
        size_t l, r;
        std::cin >> l >> r;
        std::printf("%d ", prefix[r] - prefix[l - 1]);
    }
    std::cout << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}