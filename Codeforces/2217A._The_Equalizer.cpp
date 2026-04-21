/*
A. The Equalizer
time limit per test1 second
memory limit per test256 megabytes

To settle a long-time feud, Shaunak and Yash decided to play a game on an array a
 of n
 integers, with Shaunak going first. The players take turns, and the last player to make a move wins. On a player's turn, he chooses some ai>0
 and decrements it by 1
.

To make things interesting, Shaunak is allowed to use a special move at most once during the game. This move replaces his normal turn. When used, all elements ai
 (1≤i≤n
) are set to a special value k
 that is given initially.

Assuming that both players play optimally, determine if Shaunak can always win.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains two integers n
 and k
 (1≤n≤100
, 1≤k≤500
), denoting the size of the array and the special value.

The second line contains n
 integers a1,a2,…,an
 (1≤ai≤103
).

Output
For each test case, print "YES" if Shaunak can always win, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
InputCopy
4
1 1
1
2 67
67 67
3 2
3 3 3
11 3
1 2 3 4 5 6 7 8 9 10 11
OutputCopy
YES
YES
YES
NO
Note
In the third test case, n=3
, k=2
 and the initial array is [3,3,3]
. One possible way the game could proceed is shown:

Shaunak decrements a3
. Array becomes [3,3,2]
.
Yash decrements a3
. Array becomes [3,3,1]
.
Shaunak uses the special move. Array becomes [2,2,2]
.
Yash decrements a1
. Array becomes [1,2,2]
.
Shaunak decrements a2
. Array becomes [1,1,2]
.
Yash decrements a3
. Array becomes [1,1,1]
.
Shaunak decrements a1
. Array becomes [0,1,1]
.
Yash decrements a3
. Array becomes [0,1,0]
.
Shaunak decrements a2
. Array becomes [0,0,0]
.
Since there are no ai>0
 remaining, Yash cannot make any further moves and Shaunak wins.
*/
// Solution
// C++ O(N) O(1) Math
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    int k = 0;
    std::cin >> n >> k;
    std::vector<int> nums(n, 0);
    int total = 0;
    for (size_t i = 0; i < n; ++i) {
        std::cin >> nums[i];
        total += nums[i];
    }
    if (total & 1) {
        std::cout << "YES\n";
        return;
    }
    std::cout << (!(n * k & 1) ? "YES" : "NO") << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}
