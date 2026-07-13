/*
A. Bigrams
time limit per test2 seconds
memory limit per test512 megabytes
A bigram in a string is a pair of adjacent characters. For example, the string helloello contains 8
 bigrams: he, el, ll, lo, oe, el, ll, lo.

Monocarp has cards with letters: c1
 cards with the letter a, c2
 cards with the letter b, ..., ck
 cards with the k
-th letter of the Latin alphabet. He wants to make a string from these cards, using each card exactly once. The resulting string must contain at least two equal bigrams. The order of characters in each bigram matters; for example, the string aba does not have two equal bigrams.

Determine whether it is possible to make a string that satisfies these requirements.

Input
The first line contains one integer t
 (1≤t≤104
) — the number of test cases.

Each test case consists of two lines:

the first line contains one integer k
 (1≤k≤10
);
the second line contains k
 integers c1,c2,…,ck
 (1≤ci≤108
), where ci
 is the number of cards with the i
-th letter of the Latin alphabet.
Output
For each test case, output YES if it is possible to construct a string satisfying the condition, or NO otherwise.

Each letter can be output in any case. For example, yes, Yes, yEs will be recognized as a positive answer.

Example
InputCopy
7
1
1
1
3
1
4
2
2 1
2
3 2
3
1 1 2
4
1 1 2 2
OutputCopy
NO
YES
YES
NO
YES
NO
YES
Note
In the first example, you can only make the string a, which contains no bigrams.

In the second example, you can make the string aaa, which contains two bigrams aa.

In the third example, you can make the string aaaa, which contains three bigrams aa.

In the fourth example, you can make the string aab, aba, or baa. None of these strings contains two equal bigrams.

In the fifth example, you can make the string aabab, which contains two bigrams ab.
*/
// Solution
// C++ O(N) O(1) Greedy
#include <iostream>
#include <vector>


void solution() {
    size_t n;
    std::cin >> n;
    std::vector<int> nums;
    for (size_t i = 0; i < n; ++i) {
        int c;
        std::cin >> c;
        nums.push_back(c);
    }
    bool isValid = false, single = false;
    for (size_t i = 0; i < n; ++i) {
        if (nums[i] > 2) isValid = true;
        if (nums[i] >= 2) {
            if (single) isValid = true;
            single = true;
        }
    }
    std::cout << (isValid ? "YES" : "NO") << "\n";
}


int main() {
    size_t t;
    std::cin >> t;
    while (t--) solution();
}