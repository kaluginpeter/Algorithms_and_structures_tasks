/*
A. Destroying Towers
time limit per test1 second
memory limit per test256 megabytes
Quack the Duck has returned to his homeland and found n
 towers standing in a line. The height of the i
-th tower is ai
. He wants vengeance for the destruction of his ecosystem, and has vowed to wreak as much havoc as possible with his laser gun.

Quack will operate on each tower exactly once, in any order he chooses. The operation on tower i
 is as follows:

Quack climbs to the top of tower i
 and shoots a laser to the right, cutting the first taller tower it hits down to the same height as tower i
.
Formally, let j
 be the smallest index such that j>i
 and aj>ai
, where ai
 and aj
 are the current heights of the towers. If such j
 exists, then aj
 is replaced with ai
. Otherwise, nothing happens.

Find the minimum possible final sum of tower heights over all possible orders of operations.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains an integer n
 (1≤n≤100
) — the number of towers.

The following line contains n
 integers a1,a2,…,an
 (1≤ai≤1000
) — the heights of the towers.

Output
For each test case, output a single integer — the minimum possible final sum of tower heights over all possible orders of operations.

Example
InputCopy
10
3
1 3 5
3
5 4 3
4
3 2 5 1
4
2 1 4 3
5
4 1 3 5 2
5
2 2 3 1 4
1
7
6
6 1 5 2 4 3
4
1 1 1 1
5
10 3 8 6 9
OutputCopy
3
12
8
5
8
8
7
11
4
22
Note
In the first test case, one optimal order is 3,1,2
. The heights change as follows:

[1,3,5]→[1,3,5]→[1,1,5]→[1,1,1].

Thus the final sum is 1+1+1=3
.

In the second test case, no operation can change any tower. For every tower, there is no higher tower to its right. Therefore the final heights remain [5,4,3]
, and the answer is 5+4+3=12
.

In the third test case, one optimal order is 4,1,3,2
. The heights change as follows:

[3,2,5,1]→[3,2,5,1]→[3,2,3,1]→[3,2,3,1]→[3,2,2,1].

Therefore the final sum is 3+2+2+1=8
.
*/
// Solution
// C++ O(N) O(1) Math
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    size_t output = 0, bound = -1;
    for (int& num : nums) {
        if (num < bound) bound = num;
        output += bound;
    }
    std::cout << output << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}