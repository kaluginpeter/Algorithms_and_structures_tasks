/*
A. Another Puzzle from Papyrus
time limit per test1 second
memory limit per test256 megabytes
You are filled with determination.
— Undertale
Papyrus came up with another puzzle for Frisk to solve. Papyrus brought two arrays a
 and b
 of length n
 and allowed the following two operations to be performed:

choose any index i
 (1≤i≤n
) and change ai
 to ai−1
. The execution time of such an operation is 1
 second.
reorder all elements of array a
 in any way. The execution time of such an operation is c
 seconds.
You need to convert array a
 into array b
.

Frisk wants to solve the puzzle as soon as possible. Help Frisk determine the minimum time needed to solve the puzzle. If there is no solution, output −1
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains two integers n
 and c
 (1≤n,c≤100
) — the length of arrays a
 and b
 and the cost of the second operation.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤100
) — the elements of the first array.

The third line of each test case contains n
 integers b1,b2,…,bn
 (1≤bi≤100
) — the elements of the second array.

Output
For each test case, output a single integer representing the minimum number of seconds required to solve the puzzle, or −1
 if it is impossible to solve the puzzle.

Example
InputCopy
6
3 5
5 2 3
2 3 4
3 3
1 2 3
4 5 6
4 4
4 5 2 3
3 5 1 2
6 4
2 4 5 3 6 8
5 8 3 1 2 5
5 11
5 8 11 14 17
16 12 10 10 6
3 5
20 14 20
12 18 17
OutputCopy
6
-1
3
8
-1
12
Note
In the first test case, it is impossible to transform a
 into b
 using only subtraction because a2<b2
. Let's rearrange the elements of array a
 as follows: [5,2,3]⇒[2,3,5]
. Now it is enough to subtract one from a3
, and we get that array a
 becomes equal to array b
 in 5+1=6
 seconds.

In the second test case, all elements of a
 are less than all elements of b
, which means a
 cannot be transformed into b
.

In the third test case, you can choose not to rearrange the elements and get an answer of 3
. If you rearrange them at least once, the answer will be at least 4
, so the optimal answer is 3
 seconds.

In the sixth test case, the array can be rearranged as follows: [14,20,20]
. It can be seen that the cost will then be 5+(14−12)+(20−18)+(20−17)=12
.
*/
// Solution
// C++ O(NlogN + MlogM) O(1) Sorting Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    int c = 0;
    std::cin >> n >> c;
    std::vector<int> a(n, 0), b(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> a[i];
    for (size_t i = 0; i < n; ++i) std::cin >> b[i];
    bool was = true;
    int cost1 = 0;
    for (size_t i = 0; i < n; ++i) {
        if (a[i] < b[i]) {
            was = false;
            break;
        } else cost1 += a[i] - b[i];
    }
    std::sort(a.begin(), a.end());
    std::sort(b.begin(), b.end());
    int cost2 = c;
    for (size_t i = 0; i < n; ++i) {
        if (a[i] < b[i]) {
            std::cout << "-1\n";
            return;
        }
        cost2 += a[i] - b[i];
    }
    std::cout << std::min((was ? cost1 : cost2), cost2) << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}