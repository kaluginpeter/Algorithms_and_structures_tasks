/*
A. Convergence
time limit per test1 second
memory limit per test256 megabytes
Alice is inviting her friends to a party to eat cakes. However, each friend may not be at the same place, so everyone has to meet up at the same location first.

Alice has n
 friends, where the i
-th friend is at position ai
. To make everyone be at the same place, Alice has to make multiple group calls. Unfortunately, the signal is weak, and Alice can only call 2
 other people at a time.

Being a good person, Alice doesn't want her friends to walk too far. So, for each group call containing the i
-th friend and the j
-th friend, Alice will tell both of them to meet at some integer location between min(ai,aj)
 and max(ai,aj)
 inclusive. After that, both of them will move to that location so quickly that Alice cannot make any group call during their movement. Please note that Alice can call these friends again once they reach that location.

The party is starting soon, so Alice needs to make group calls fast. Help her find the minimum number of group calls she needs to make.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains an integer n
 (2≤n≤100
) — the number of friends Alice has.

The second line of each test case contains n
 integers a1,a2,…,an
 (1≤ai≤109
) — the locations of her friends.

Output
For each test case, output the minimum number of group calls she needs to make in order for all of her friends to be in the same location.

Example
InputCopy
4
5
1 2 3 4 5
5
1 1 1 2 2
11
3 1 4 1 5 9 2 6 5 3 5
5
1 2 2 2 2
OutputCopy
2
2
5
1
Note
In the first test case, the minimum number of group calls is 2. One way to make everyone at the same location is as follows:

Call the 1
-st and 4
-th friend and tell them to move to location 3
. Their locations are now [3,2,3,3,5]
.
Call the 2
-nd and 5
-th friend and tell them to move to location 3
. Their locations are now [3,3,3,3,3]
.
In the second test case, the minimum number of group calls is 2. One way to make everyone at the same location is as follows:

Call the 1
-st and 4
-th friend and tell them to move to location 1
. Their locations are now [1,1,1,1,2]
.
Call the 4
-th and 5
-th friend and tell them to move to location 1
. Their locations are now [1,1,1,1,1]
.
*/
// Solution
// C++ O(N) O(1) Greedy Math
#include <iostream>
#include <vector>
#include <algorithm>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums(n, 0);
    for (size_t i = 0; i < n; ++i) std::cin >> nums[i];
    std::sort(nums.begin(), nums.end());
    int target = nums[n >> 1];
    int lessThan = 0, greaterThan = 0;
    for (int& num : nums) {
        if (num < target) ++lessThan;
        else if (num > target) ++greaterThan;
    }
    int diff = std::min(lessThan, greaterThan);
    std::cout << diff + std::max(lessThan, greaterThan) - diff << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}