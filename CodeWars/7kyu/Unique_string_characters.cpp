/*
In this Kata, you will be given two strings a and b and your task will be to return the characters that are not common in the two strings.

For example:

solve("xyab","xzca") = "ybzc"
--The first string has 'yb' which is not in the second string.
--The second string has 'zc' which is not in the first string.
Notice also that you return the characters from the first string concatenated with those from the second string.

More examples in the tests cases.

Good luck!

Please also try Simple remove duplicates

StringsFundamentals
*/
// Solution
#include <unordered_set>

std::string solve(std::string a, std::string b) {
    std::string output = "";
    std::unordered_set<char> seenA, seenB ;
    for (char &letter : a) seenA.insert(letter);
    for (char &letter : b) seenB.insert(letter);
    for (char &letter : a) {
        if (!seenB.count(letter)) output.push_back(letter);
    }
    for (char &letter : b) {
        if (!seenA.count(letter)) output.push_back(letter);
    }
    return output;
}