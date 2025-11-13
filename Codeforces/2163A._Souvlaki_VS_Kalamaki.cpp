/*
A. Souvlaki VS. Kalamaki
time limit per test1 second
memory limit per test256 megabytes
Two players, Souvlaki and Kalamaki, are given a sequence a
 of n
 integers.

They will play a game that consists of n−1
 rounds, which are numbered from 1
 to n−1
. Souvlaki plays on odd-numbered rounds, and Kalamaki on even-numbered rounds.

On the i
-th round, a player can choose to take exactly one of the following actions:

Skip his turn and proceed to round i+1
 (or finish the game if round i
 was the last one).
Swap elements ai
 and ai+1
.
Souvlaki wins if after the end of the last round, a
 is sorted in non-decreasing order. In other words, he wins if ai≤ai+1
 holds for every 1≤i<n
. Otherwise, Kalamaki wins.

However, Souvlaki does not like losing, so before the start of the game, he may re-order the elements of a
 in anyway he wants. Is it possible for him to do so such that he has a guaranteed winning strategy?

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤100
). The description of the test cases follows.

The first line of each test case contains a single integer, n
 (3≤n≤100
) — the number of integers in a
.

The second line contains exactly n
 integers a1,a2,…,an
 (1≤ai≤n
) — where ai
 represents the i
-th element of a
.

Output
For each test case, output on a separate line "'YES"' if it is possible for Souvlaki to re-order the elements of a
 such that he has a guaranteed winning strategy, and "'NO"' otherwise.

You can output the answer in any case (upper or lower). For example, the strings "'yEs"', "'yes"', "'Yes"', and "'YES"' will be recognized as positive responses.

Example
InputCopy
5
4
4 2 2 1
4
1 1 1 1
5
1 5 1 5 1
3
1 2 3
5
1 3 2 3 5
OutputCopy
YES
YES
YES
NO
NO
Note
In the first example, a=[4,2,2,1]
. A possible way to re-order the elements so that Souvlaki can win is the following: a=[2,1,2,4]
. Then, the game might go as follows:

On round 1
, it is Souvlaki's turn. He will choose to swap a1
 with a2
, and now a=[1,2,2,4]
.
On round 2
, it is Kalamaki's turn. Whether he chooses to skip his turn or swap elements a2
 and a3
, a
 will remain the same. Suppose he skips his turn.
On round 3
, it is Souvlaki's turn. He can choose to skip his turn as well, because if he swapped the last two elements he would lose.
After every round, a=[1,2,2,4]
, sorted in non-decreasing order, so Souvlaki wins, no matter how Kalamaki chooses to play.

On the second example, since every element is equal, Souvlaki will always win because a
 is always sorted in non-decreasing order.
*/
// Solution
// C++ O(NlogN) O(1) Sorting Math
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    bool isValid = true;
    for (size_t i = 1; i < n - 1; i += 2) {
        if (nums[i] != nums[i + 1]) {
            isValid = false;
            break;
        }
    }
    std::cout << (isValid ? "YES" : "NO") << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}