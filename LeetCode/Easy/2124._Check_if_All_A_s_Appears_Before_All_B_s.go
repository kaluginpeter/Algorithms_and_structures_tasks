/*
Given a string s consisting of only the characters 'a' and 'b', return true if every 'a' appears before every 'b' in the string. Otherwise, return false.

 

Example 1:

Input: s = "aaabbb"
Output: true
Explanation:
The 'a's are at indices 0, 1, and 2, while the 'b's are at indices 3, 4, and 5.
Hence, every 'a' appears before every 'b' and we return true.
Example 2:

Input: s = "abab"
Output: false
Explanation:
There is an 'a' at index 2 and a 'b' at index 1.
Hence, not every 'a' appears before every 'b' and we return false.
Example 3:

Input: s = "bbb"
Output: true
Explanation:
There are no 'a's, hence, every 'a' appears before every 'b' and we return true.
 

Constraints:

1 <= s.length <= 100
s[i] is either 'a' or 'b'.
*/
// Solution
// C++ O(N) O(1) Greedy TwoPointers
class Solution {
public:
    bool checkString(string s) {
        size_t left = 0, right = s.size() - 1;
        while (left < right && s[left] == 'a') ++left;
        while (right > left && s[right] == 'b') --right;
        return left >= right;
    }
};
// Go O(N) O(1) Greedy
func checkString(s string) bool {
    var seen bool = false
    for _, ch := range s {
        if ch == 'b' {
            seen = true;
        } else if seen { return false }
    }
    return true
}