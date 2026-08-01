/*
In this Kata, you will check if it is possible to convert a string to a palindrome by changing one character.

For instance:

solve ("abbx") = True, because we can convert 'x' to 'a' and get a palindrome.
solve ("abba") = False, because we cannot get a palindrome by changing any character.
solve ("abcba") = True. We can change the middle character.
solve ("aa") = False
solve ("ab") = True
Good luck!

Please also try Single Character Palindromes

Algorithms
*/
// Solution
#include <string>

bool solve(const std::string& s){
    int left = 0, right = s.size() - 1;
    bool was = false;
    while (left < right) {
        if (s[left] != s[right]) {
            if (was) return false;
            was = true;
        }
        ++left;
        --right;
    }
    return was || (s.size() & 1);
}