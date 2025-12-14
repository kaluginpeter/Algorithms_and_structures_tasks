/*
A. Sleeping Through Classes
time limit per test1 second
memory limit per test256 megabytes
You have n
 classes today, which are numbered from 1
 to n
.

The classes are described by a binary string∗
 s
 of length n
. We call class i
 important if and only if si=1
. For each important class, you must stay awake and listen to it.

You are very tired and wish to sleep through as many classes as possible. However, falling asleep takes time. If you listen to an important class i
, then you cannot fall asleep for the next k
 classes, i.e., you must also stay awake in classes i+1,i+2,…,i+k
 (or until the end of the day, if fewer than k
 classes remain).

For classes that are not important, you may sleep through them unless the rule above forces you to stay awake.

Your task is to find out the maximum number of classes you can sleep through today.

∗
A binary string is a string where each character is either 0
 or 1
.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤500
). The description of the test cases follows.

The first line of each test case contains two integers n
 and k
 (1≤n,k≤100
).

The second line of each test case contains the string s
 of length n
 (si=0
 or 1
).

Output
For each test case, output a single integer — the maximum number of classes you can sleep through today.

Example
InputCopy
4
4 1
1001
3 3
000
3 1
001
8 2
01000101
OutputCopy
1
3
2
2
Note
In the first test case, you must listen to class 1
 and class 4
. After listening to class 1
, you cannot fall asleep in class 2
. So the only class you can sleep through is class 3
.

In the second test case, you can sleep through all the classes.

In the fourth test case, you can only sleep through classes 1
 and 5
.
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>
#include <string>


void solution() {
    size_t n;
    int k;
    std::cin >> n >> k;
    std::string seq;
    std::cin >> seq;
    int output = 0, i = 0, bound = -1;
    while (i < n) {
        if (seq[i] == '1') bound = i + k;
        else if (bound < i) ++output;
        ++i;
    }
    std::cout << output << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}