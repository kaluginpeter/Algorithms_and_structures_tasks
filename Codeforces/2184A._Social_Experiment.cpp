/*
A. Social Experiment
time limit per test1 second
memory limit per test256 megabytes
Right now, the largest social experiment in the history of Codeforces is taking place, involving n
 people. They are required to form teams of 2−3
 people, after which each team chooses one of two civilizations to participate in the social experiment.

The organizers of this social experiment want to know what the possible difference in the number of people in the civilizations could be. Find the minimum possible difference.

Input
Each test consists of several test cases. The first line contains a single integer t
 (1≤t≤104)
 — the number of test cases. The following lines describe the test cases.

In the only line of each test case, there is an integer n
 — the number of people participating in the social experiment (2≤n≤104)
.

Output
For each number n
, output the minimum possible difference between the number of people in the civilizations.

Example
InputCopy
3
2
5
12
OutputCopy
2
1
0
Note
In the first test case, only one team can be formed, which will choose one of the civilizations, while the other will have no one, so the answer is 2
.

In the second test case, two teams can be formed: one with two people and the other with three. These teams will choose different civilizations; thus, the answer will be 1
.

In the third test case, four teams of three people will be formed, with the first two choosing the first civilization and the remaining two choosing the second. The answer is 0
.
*/
// Solution
// C++ O(1) O(1) Math
#include <iostream>


void solution() {
    int n;
    std::cin >> n;
    std::cout << (n <= 3 ? n : n & 1) << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}