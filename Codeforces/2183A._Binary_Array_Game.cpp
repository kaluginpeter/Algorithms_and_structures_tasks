/*
A. Binary Array Game
time limit per test1 second
memory limit per test256 megabytes
Alice and Bob are playing a game on an array a
 of size n
, containing only numbers 0 and 1. Alice moves first, with each player alternating turns.

In a player's turn, he or she chooses two integers l
 and r
 such that 1≤l<r≤|a|
 (here, |a|
 denotes the current length of a
). Then, the subarray [al,al+1,…,ar]
 is replaced with a single number 1−min(al,al+1,…,ar)
. That is, if all numbers in the subarray are 1
, then the subarray [al,al+1,…,ar]
 is removed, and the number 0
 is inserted where the subarray was. Otherwise, the subarray [al,al+1,…,ar]
 is removed, and the number 1
 is inserted where the subarray was.

The game ends when there is exactly one number left in the array (where the player to go cannot make legal moves). Alice wins if the final number is 0
. Otherwise, Bob wins. Please determine who wins this game with optimal play.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The first line of each test case contains a positive integer n
 (3≤n≤100
), denoting the length of the array a
.

The second line of each test case contains n
 integers a1,a2,…,an
 (0≤ai≤1
).

Output
For each test case, output Alice if Alice wins, and Bob otherwise. You may output each character in any case. For example, the answers Alice, alice, ALICE, AliCe will all be interpreted the same.

Example
InputCopy
7
3
1 1 0
3
1 1 1
3
0 1 0
4
0 0 0 0
5
1 0 1 0 1
6
0 1 0 1 0 1
6
0 1 0 1 0 0
OutputCopy
Alice
Alice
Bob
Bob
Alice
Alice
Bob
Note
In the first test case, Alice can win by choosing l=2
 and r=3
. Since 1−min(a2,a3)=1
, the subarray [1,0]
 is replaced with a single integer 1
, and a
 becomes [1,1]
. At this point, it is Bob's turn, and the only move he has is to choose l=1
 and r=2
. Since 1−min(a1,a2)=0
, the array a
 becomes [0]
. The game now ends, and Alice wins because the last number is 0
.

In the second test case, Alice can win by choosing l=1
 and r=3
 in her first move. The array becomes [0]
, and the game ends as a win for Alice immediately.
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>


void solution() {
    size_t n;
    std::cin >> n;
    int ones = 0, zeros = 0;
    bool isFirst, isLast;
    for (size_t i = 0; i < n; ++i) {
        int x;
        std::cin >> x;
        if (!i) isFirst = x;
        if (i + 1 == n) isLast = x;

        if (!x) ++zeros;
        else ++ones;
    }
    if (ones == n || zeros == n) {
        std::cout << (ones >= zeros ? "Alice" : "Bob") << "\n";
        return;
    }
    std::cout << (isFirst || isLast ? "Alice" : "Bob") << "\n";

}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}