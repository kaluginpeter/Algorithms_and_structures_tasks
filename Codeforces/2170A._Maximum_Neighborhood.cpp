/*
A. Maximum Neighborhood
time limit per test2 seconds
memory limit per test512 megabytes
Consider an n×n
 grid filled with numbers as follows:

the first row contains integers from 1
 to n
 from left to right;
the second row contains integers from (n+1)
 to 2n
 from left to right;
this pattern continues until the n
-th row, which contains integers from (n2−n+1)
 to n2
 from left to right.
Let's define the cost of a cell as its value plus the sum of its neighboring cells' values. Two cells are considered neighboring if they share a side.

Your task is to calculate the maximum cost among all cells in the grid.

The grid for n=4
 and the optimal answer for it. The yellow cell has the maximum possible cost; the green cells are its neighbors. The cost of the cell is 15+11+14+16=56
.
Input
The first line contains a single integer t
 (1≤t≤100
) — the number of test cases.

The only line of each test case contains a single integer n
 (1≤n≤100
).

Output
For each test case, print a single integer — the maximum cost among all cells in the grid.

Example
InputCopy
5
1
2
3
4
5
OutputCopy
1
9
29
56
95
Note
In the first example, there is only 1
 cell with the cost 1
.

In the second example, the cell with value 4
 has the maximum cost: 4+2+3=9
.

In the third example, the cell with value 8
 has the maximum cost: 8+5+7+9=29
.

In the fourth example, the cell with value 15
 has the maximum cost: 15+11+14+16=56
.

In the fifth example, the cell with value 19
 has the maximum cost: 19+14+18+20+24=95
.
*/
// Solution
// C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    if (n == 1) {
        std::cout << "1\n";
        return;
    } else if (n == 2) {
        std::cout << "9\n";
        return;
    } else if (n < 5) {
        int m = n * n;
        std::cout << (m * 3 - 3 + (m - 1 - n)) << "\n";
        return;
    }
    int m = n * n - 1 - n;
    std::cout << (m * 5) << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}