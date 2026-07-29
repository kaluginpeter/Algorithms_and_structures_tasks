/*
Motivation
When compressing sequences of symbols, it is useful to have many equal symbols follow each other, because then they can be encoded with a run length encoding. For example, RLE encoding of "aaaabbbbbbbbbbbcccccc" would give something like 4a 11b 6c.

(Look here for learning more about the run-length-encoding.)

Of course, RLE is interesting only if the string contains many identical consecutive characters. But what bout human readable text? Here comes the Burrows-Wheeler-Transformation.

Transformation
There even exists a transformation, which brings equal symbols closer together, it is called the Burrows-Wheeler-Transformation. The forward transformation works as follows: Let's say we have a sequence with length n, first write every shift of that string into a n x n matrix:

Input: "bananabar"

b a n a n a b a r
r b a n a n a b a
a r b a n a n a b
b a r b a n a n a
a b a r b a n a n
n a b a r b a n a
a n a b a r b a n
n a n a b a r b a
a n a n a b a r b
Then we sort that matrix by its rows. The output of the transformation then is the last column and the row index in which the original string is in:

               .-.
a b a r b a n a n
a n a b a r b a n
a n a n a b a r b
a r b a n a n a b
b a n a n a b a r <- 4
b a r b a n a n a
n a b a r b a n a
n a n a b a r b a
r b a n a n a b a
               '-'

Output: ("nnbbraaaa", 4)
Of course we want to restore the original input, therefore you get the following hints:

The output contains the last matrix column.
The first column can be acquired by sorting the last column.
For every row of the table: Symbols in the first column follow on symbols in the last column, in the same way they do in the input string.
You don't need to reconstruct the whole table to get the input back.
Goal
The goal of this Kata is to write both, the encode and decode functions. Together they should work as the identity function on lists. (Note: For the empty input, the row number is ignored.)

Further studies
You may have noticed that symbols are not always consecutive, but just in proximity, after the transformation. If you're interested in how to deal with that, you should have a look at this Kata.

ListsPuzzlesAlgorithms
*/
// Solution
#include <algorithm>
#include <string>
#include <utility>
#include <vector>

std::pair<std::string, int> encode(const std::string &s) {
    if (s.empty()) return {"", 0};

    int n = s.size();
    std::vector<std::string> rotations;

    for (int i = 0; i < n; ++i)
        rotations.push_back(s.substr(i) + s.substr(0, i));

    std::sort(rotations.begin(), rotations.end());

    std::string last;
    int idx = 0;

    for (int i = 0; i < n; ++i) {
        last += rotations[i].back();
        if (rotations[i] == s)
            idx = i;
    }

    return {last, idx};
}
std::string decode(const std::string& last, int row) {
    if (last.empty()) return "";

    int n = last.size();

    std::string first = last;
    std::sort(first.begin(), first.end());

    std::vector<int> occLast(n), occFirst(n);
    int cnt[256] = {};

    for (int i = 0; i < n; ++i)
        occLast[i] = ++cnt[(unsigned char)last[i]];

    std::fill(cnt, cnt + 256, 0);

    for (int i = 0; i < n; ++i)
        occFirst[i] = ++cnt[(unsigned char)first[i]];

    std::vector<int> lf(n);

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (last[i] == first[j] && occLast[i] == occFirst[j]) {
                lf[i] = j;
                break;
            }
        }
    }

    std::string ans(n, ' ');
    int cur = row;

    for (int i = n - 1; i >= 0; --i) {
        ans[i] = last[cur];
        cur = lf[cur];
    }

    return ans;
}