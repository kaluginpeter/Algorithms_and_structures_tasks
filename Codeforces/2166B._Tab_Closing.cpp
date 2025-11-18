/*
B. Tab Closing
time limit per test1.5 seconds
memory limit per test256 megabytes
You've been staring at your computer screen for too long; it is time to give it a break and go touch some grass.

Your screen is a line of length a
, and there are n
 tabs displayed on it. You want to close all of the tabs by clicking on the x's at their right endpoint.

Every tab is a segment of length len=min(b,am)
, where m
 is the number of remaining tabs. The tabs are always tightly arranged in sequence from the left endpoint of the screen; that is, the x's will be at len,2⋅len,3⋅len,…,m⋅len
 units away from the left endpoint. Please note that the length of each tab will change as you are closing tabs.

Now your cursor is at the left endpoint of the screen. You wonder what the minimum number of times you need to move the mouse to close all tabs is.

If you have difficulty understanding the statement, you may also refer to your browser tab for a visualization, or click here.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

Each test case is a line of three integers a
, b
, and n
 (1≤b≤a≤109
, 1≤n≤109
).

Output
For each test case, output a single integer — the minimum number of times you need to move the mouse to close all tabs.

Example
InputCopy
12
8 1 6
9 6 2
10 3 1
10 1 10
9 2 1
5 5 6
6 2 7
9 1 9
3 2 6
8 1 7
8 1 9
8 2 4
OutputCopy
1
2
1
1
1
1
2
1
2
1
2
1
Note
In the first test case, a possible course of action is to move your cursor to 1
 and press 6
 times.

In the second test case, a possible course of action is to move your cursor to 4.5
 and press once, then move it to 6
 and press again. It can be proved that the tabs cannot be closed with less than 2
 moves.
*/
// Solution
// C++ O(1) O(1) Math
#include <iostream>


void solution() {
    long long a, b, n;
    std::cin >> a >> b >> n;
    std::cout << ((b * n <= a) || (b == a) ? 1 : 2) << std::endl;
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}