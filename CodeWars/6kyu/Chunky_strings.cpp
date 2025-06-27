/*
This kata concerns a string composed of 'chunks'.

A chunk is either:

A single alphabetic character
or:

Two chunks enclosed in square brackets [ and ]
A 'chunky string' is a string consisting of exactly one chunk. Here are some examples of chunky strings:

'x'
'[xy]'
'[x[yy]]'
'[[xy]y]'
'[[ab][ab]]'
'[c[o[d[e[w[a[rs]]]]]]]'
For this task you will be given a valid chunky string from which all the closing brackets have been removed. You must restore the brackets and return the original valid chunky string.

For example:

Input               Restored String
'x'                 'x'
'[xy'               '[xy]'
'[x[yy'             '[x[yy]]'
'[[xyy'             '[[xy]y]'
'[[ab[ab'           '[[ab][ab]]'
'[c[o[d[e[w[a[rs'   '[c[o[d[e[w[a[rs]]]]]]]'
In the tests all input strings will be valid chunky strings (with closing brackets removed).

StringsRecursion
*/
// Solution
#include <string>
#include <stack>
#include <cctype>

std::string restore_brackets(const std::string& s) {
    std::string result = "";
    std::stack<int> chunk_counts;
    for (char c : s) {
        if (c == '[') {
            result += '[';
            chunk_counts.push(0);
        } else {
            result += c;
            if (!chunk_counts.empty()) {
                ++chunk_counts.top();
            }
        }
        while (!chunk_counts.empty() && chunk_counts.top() == 2) {
            result += ']';
            chunk_counts.pop();
            if (!chunk_counts.empty()) ++chunk_counts.top();
        }
    }
    return result;
}