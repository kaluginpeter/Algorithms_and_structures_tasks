/*
B. Party Monster
time limit per test2 seconds
memory limit per test256 megabytes
Yousef has given you a sequence s
 of length n
 consisting only of characters '(
' and ')
'. You are allowed to perform the following operation at most once:

Choose a substring∗
 of s
 and remove it. Then, you may reinsert the removed characters back into the remaining string one by one. Each character can be placed at any arbitrary position, independently of the others.
Yousef wants you to determine whether it is possible to obtain a regular bracket sequence†
 after performing the operation at most once.

∗
A substring is a contiguous subsegment of a string. For example, "acab" is a substring of "abacaba" (it starts in position 3
 and ends in position 6
), but "aa" or "d" aren't substrings of this string. So the substring of the string s
 from position l
 to position r
 is s[l,r]=slsl+1…sr
.

†
A regular bracket sequence is a bracket sequence that can be transformed into a correct arithmetic expression by inserting the characters 1
 and +
 between the original characters of the sequence. For example:

bracket sequences ()()
 and (())
 are regular (the resulting expressions are: (1)+(1)
 and ((1+1)+1)
);
bracket sequences )(
, (
 and )
 are not.
Input
The first line contains an integer t
 (1≤t≤104
) — the number of test cases. The descriptions of the test cases follow.

The first line of each test case contains a single integer n
 (1≤n≤2⋅105
) — the length of the string s
.

The second line of each test case contains a sequence s
 of length n
 consisting only of characters '(
' and ')
'.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, output "YES" if the sequence can be made regular, and "NO" otherwise.

You can output the answer in any case (upper or lower). For example, the strings "yEs", "yes", "Yes", and "YES" will be recognized as positive responses.

Example
InputCopy
6
2
()
2
)(
3
(((
6
())(()
4
(()(
5
)()()
OutputCopy
YES
YES
NO
YES
NO
NO
Note
In the first test case, the string s
 is already a regular bracket sequence, therefore the answer is "YES".

In the second test case, we can remove the substring s[2,2]=(
 and reinsert it at the beginning of the string, making s=()
, therefore the answer is "YES".

In the third test case, there is no way to do the operation and get a regular bracket sequence, so the answer is "NO".

In the fourth test case, we can choose the substring s[3,4]=)(
, remove it, then reinsert the characters as follows:

())(()→()()→(()())

Therefore we have made a regular bracket sequence, and the answer is "YES".
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>
#include <string>
#include <cstdint>


void solution() {
    size_t n;
    std::cin >> n;
    std::string sequence = "";
    std::cin >> sequence;
    int32_t x = 0, y = 0;
    for (char& ch : sequence) {
        if (ch == '(') ++x;
        else ++y;
    }
    std::cout << ((std::max(x, y) - std::min(x, y))? "NO" : "YES") << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}