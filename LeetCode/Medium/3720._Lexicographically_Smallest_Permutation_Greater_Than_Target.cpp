/*
You are given two strings s and target, both having length n, consisting of lowercase English letters.

Return the lexicographically smallest permutation of s that is strictly greater than target. If no permutation of s is lexicographically strictly greater than target, return an empty string.

A string a is lexicographically strictly greater than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears later in the alphabet than the corresponding letter in b.

 

Example 1:

Input: s = "abc", target = "bba"

Output: "bca"

Explanation:

The permutations of s (in lexicographical order) are "abc", "acb", "bac", "bca", "cab", and "cba".
The lexicographically smallest permutation that is strictly greater than target is "bca".
Example 2:

Input: s = "leet", target = "code"

Output: "eelt"

Explanation:

The permutations of s (in lexicographical order) are "eelt", "eetl", "elet", "elte", "etel", "etle", "leet", "lete", "ltee", "teel", "tele", and "tlee".
The lexicographically smallest permutation that is strictly greater than target is "eelt".
Example 3:

Input: s = "baba", target = "bbaa"

Output: ""

Explanation:

The permutations of s (in lexicographical order) are "aabb", "abab", "abba", "baab", "baba", and "bbaa".
None of them is lexicographically strictly greater than target. Therefore, the answer is "".
 

Constraints:

1 <= s.length == target.length <= 300
s and target consist of only lowercase English letters.
*/
// Solution
// C++ O(N^2) O(N) Greedy
class Solution {
public:
    void insertSmallest(std::string& s, std::string& target, std::array<int, 26>& hashmap, std::array<int,  26>& targetHashmap, size_t& i, std::string& output) {
        --targetHashmap[target[i] - 'a'];
        for (size_t ptr = 0; ptr < 26; ++ptr) {
            if (hashmap[ptr]) {
                output.push_back(ptr + 'a');
                --hashmap[ptr];
                break;
            }
        }
    };
    bool canSkip(std::string& s, std::string& target, std::array<int, 26> hashmap, size_t start) {
        for (size_t i = start; i < target.size(); ++i) {
            for (size_t ptr = target[i] - 'a' + 1; ptr < 26; ++ptr) {
                if (hashmap[ptr]) return true;
            }
            if (!hashmap[target[i] - 'a']) return false;
            --hashmap[target[i] - 'a'];
        }
        return false;
    };
    string lexGreaterPermutation(string s, string target) {
        std::array<int, 26> hashmap{}, targetHashmap{};
        for (char& ch : s) ++hashmap[ch - 'a'];
        for (char& ch : target) ++targetHashmap[ch - 'a'];
        size_t n = s.size();
        std::string output = "";
        bool isGreater = false;
        for (size_t i = 0; i < n; ++i) {
            if (isGreater) {
                insertSmallest(s, target, hashmap, targetHashmap, i, output);
                continue;
            }
            if (hashmap[target[i] - 'a']) {
                --hashmap[target[i] - 'a'];
                bool can = canSkip(s, target, hashmap, i + 1);
                if (can) {
                    --targetHashmap[target[i] - 'a'];
                    output.push_back(target[i]);
                    continue;
                }
                ++hashmap[target[i] - 'a'];
            }
            // try to find a peak
            for (size_t ptr = target[i] - 'a' + 1; ptr < 26; ++ptr) {
                if (!hashmap[ptr]) continue;
                isGreater = true;
                --hashmap[ptr];
                output.push_back(ptr + 'a');
                --targetHashmap[target[i] - 'a'];
                break;
            }
        }
        if (!(output > target)) return "";
        return output;
    }
};
