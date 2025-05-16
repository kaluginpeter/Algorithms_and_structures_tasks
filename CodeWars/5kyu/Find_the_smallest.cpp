/*
You have a positive number n consisting of digits. You can do at most one operation: Choosing the index of a digit in the number, remove this digit at that index and insert it back to another or at the same place in the number in order to find the smallest number you can get.

Task:
Return an array or a tuple or a string depending on the language (see "Sample Tests") with

the smallest number you got
the index i of the digit d you took, i as small as possible
the index j (as small as possible) where you insert this digit d to have the smallest number.
Examples:
smallest(261235) --> [126235, 2, 0] or (126235, 2, 0) or "126235, 2, 0"
126235 is the smallest number gotten by taking 1 at index 2 and putting it at index 0

smallest(209917) --> [29917, 0, 1] or ...

[29917, 1, 0] could be a solution too but index `i` in [29917, 1, 0] is greater than
index `i` in [29917, 0, 1].
29917 is the smallest number gotten by taking 2 at index 0 and putting it at index 1 which gave 029917 which is the number 29917.

smallest(1000000) --> [1, 0, 6] or ...
Note
Have a look at "Sample Tests" to see the input and output in each language

Fundamentals
*/
// Solution
#include <vector>
#include <algorithm>
#include <climits>
#include <string>

using namespace std;

class ToSmallest {
public:
    static vector<long long> smallest(long long n) {
        string numStr = to_string(n);
        vector<long long> result = {n, 0, 0};
        long long minNum = n;
        int len = numStr.length();

        for (int i = 0; i < len; ++i) {
            char digit = numStr[i];
            string tempStr = numStr.substr(0, i) + numStr.substr(i + 1);
            for (int j = 0; j <= tempStr.length(); ++j) {
                string newStr = tempStr.substr(0, j) + digit + tempStr.substr(j);
                long long newNum = stoll(newStr);
                if (newNum < minNum) {
                    minNum = newNum;
                    result = {newNum, i, j};
                } else if (newNum == minNum) {
                    if (i < result[1] || (i == result[1] && j < result[2])) {
                        result = {newNum, i, j};
                    }
                }
            }
        }
        return result;
    }
};