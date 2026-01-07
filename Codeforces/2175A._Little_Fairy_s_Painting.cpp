/*
A. Little Fairy's Painting
time limit per test1 second
memory limit per test256 megabytes
The little fairy has a ribbon with 1018
 cells and an infinite variety of colors. The first n
 cells of the ribbon have already been colored, where the i
-th cell is colored with color ai
.

Little fairy will color the remaining cells in order from n+1
 to 1018
. For the i
-th cell:

Little fairy first counts the number of distinct colors currently present on the ribbon, denoted as ci
.
Then she will color the i
-th cell with color ci
.
What color will the fairy use for the 1018
-th cell?

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤100
) — the number of colored cells.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤103
) — the colors of the cells.

Output
For each test case, print the color of the last cell.

Example
InputCopy
5
6
1 1 1 1 1 1
1
1000
5
8 10 15 20 25
8
2 5 2 4 1 2 5 3
6
40 4 1 95 8 40
OutputCopy
1
1000
8
5
8
Note
In the first example, each time there is only one distinct color on the ribbon, so the fairy always chooses the color 1
.

In the second example, the fairy will color the next 1000
 cells with colors from 1
 to 1000
 sequentially, after that all next cells will be colored with color 1000
.
*/
// Solution
// C++ O(1000) O(1000) Greedy
#include <iostream>
#include <unordered_set>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::unordered_set<int> nums;
    for (size_t i = 0; i < n; ++i)  {
        int color;
        std::cin >> color;
        nums.insert(color);
    }
    int prev = nums.size();
    while (true) {
        int tmp = prev;
        nums.insert(prev);
        prev = nums.size();
        if (tmp == prev) break;
    }
    std::cout << prev << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}