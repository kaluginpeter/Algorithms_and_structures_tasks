/*
A. Eating Game
time limit per test1 second
memory limit per test256 megabytes
There are n
 players playing a game at a circular table. The i
-th player has ai
 dishes to eat. They take turns eating the food, and any player can go first.

During their turn, if player i
 has any dishes remaining, they must eat exactly one dish. Then, player (imodn)+1
 starts their turn. This continues until all dishes are finished.

The player who eats the last dish is considered the winner. Determine the number of players that can possibly be winners.

Input
The first line contains an integer t
 (1≤t≤5000
), the number of test cases.

The first line of each test case contains an integer n
 (1≤n≤10
).

The second line of each test case contains n
 integers, the elements of a
 (1≤ai≤10
).

Output
For each test case, output a line with the answer.

Example
InputCopy
3
1
10
2
6 7
4
1 4 3 4
OutputCopy
1
1
2
Note
In the first test case, player 1
 wins for every starting player.

In the second test case, player 2
 wins for every starting player.

In the third test case, players 2
 and 4
 can win.
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::cout << (std::count(nums.begin(), nums.end(), *std::max_element(nums.begin(), nums.end()))) << "\n";
}



int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}