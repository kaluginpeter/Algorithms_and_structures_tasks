/*
Consider the string "adfa" and the following rules:

a) each character MUST be changed either to the one before or the one after in alphabet.
b) "a" can only be changed to "b" and "z" to "y".
From our string, we get:

"adfa" -> ["begb","beeb","bcgb","bceb"]

Here is another example:
"bd" -> ["ae","ac","ce","cc"]

--We see that in each example, one of the outcomes is a palindrome. That is, "beeb" and "cc".
You will be given a lowercase string and your task is to return True if at least one of the outcomes is a palindrome or False otherwise.

More examples in test cases. Good luck!

Algorithms
*/
// Solution
#include <string>
#include <algorithm>

using namespace std;

static string options(char c) {
    if (c == 'a') return "b";
    if (c == 'z') return "y";
    return string{char(c - 1), char(c + 1)};
}

bool solve(string st) {
    int l = 0, r = st.size() - 1;

    while (l < r) {
        string left = options(st[l]);
        string right = options(st[r]);

        bool ok = false;
        for (char a : left) {
            for (char b : right) {
                if (a == b) {
                    ok = true;
                    break;
                }
            }
            if (ok) break;
        }

        if (!ok) return false;
        ++l;
        --r;
    }

    return true;
}