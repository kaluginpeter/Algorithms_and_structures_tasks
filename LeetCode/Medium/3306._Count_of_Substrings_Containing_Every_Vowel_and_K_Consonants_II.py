# You are given a string word and a non-negative integer k.
#
# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.
#
#
#
# Example 1:
#
# Input: word = "aeioqq", k = 1
#
# Output: 0
#
# Explanation:
#
# There is no substring with every vowel.
#
# Example 2:
#
# Input: word = "aeiou", k = 0
#
# Output: 1
#
# Explanation:
#
# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".
#
# Example 3:
#
# Input: word = "ieaouqqieaouqq", k = 1
#
# Output: 3
#
# Explanation:
#
# The substrings with every vowel and one consonant are:
#
# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".
#
#
# Constraints:
#
# 5 <= word.length <= 2 * 105
# word consists only of lowercase English letters.
# 0 <= k <= word.length - 5
# Solution
# Python O(N) O(D) SlidingWindow HashMap
class Solution:
    def get_consonants(self, hashmap: list[int], left: int, right: int, vowels: str) -> int:
        vows: int = 0
        for letter in vowels:
            vows += hashmap[ord(letter) - 97]
        return (right - left + 1) - vows

    def is_valid_window(self, hashmap: list[int], left: int, right: int, vowels: str, k: int) -> bool:
        vows: int = 0
        for letter in vowels:
            if not hashmap[ord(letter) - 97]: return False
            vows += hashmap[ord(letter) - 97]
        return (right - left + 1) - vows == k

    def countOfSubstrings(self, word: str, k: int) -> int:
        output: int = 0
        left: int = 0
        hashmap: list[int] = [0] * 26
        vowels: str = 'aeiou'
        cur_valid_subs: int = 0
        for right in range(len(word)):
            if word[right] not in vowels:
                cur_valid_subs = 0
            hashmap[ord(word[right]) - 97] += 1
            while self.get_consonants(hashmap, left, right, vowels) > k:
                hashmap[ord(word[left]) - 97] -= 1
                left += 1
            while self.is_valid_window(hashmap, left, right, vowels, k):
                cur_valid_subs += 1
                hashmap[ord(word[left]) - 97] -= 1
                left += 1
            output += cur_valid_subs
        return output

# C++ O(N) O(D) SlidingWindow HashMap
class Solution {
public:
    int getConsonants(std::vector<int>& hashmap, std::string& vowels, int& left, int& right) {
        int vows = 0;
        for (char& vowel : vowels) {
            vows += hashmap[vowel - 'a'];
        }
        return (right - left + 1) - vows;
    }
    bool isValidWindow(std::vector<int>& hashmap, std::string& vowels, int& left, int& right, int& k) {
        int vows = 0;
        for (char& letter : vowels) {
            if (!hashmap[letter - 'a']) return false;
            vows += hashmap[letter - 'a'];
        }
        return (right - left + 1) - vows == k;
    }

    long long countOfSubstrings(string word, int k) {
        std::string vowels = "aeoiu";
        std::vector<int> hashmap (26, 0);
        long long output = 0;
        int left = 0;
        long long curValidSubs = 0;
        for (int right = 0; right < word.size(); ++right) {
            ++hashmap[word[right] - 'a'];
            if (!std::count(vowels.begin(), vowels.end(), word[right])) curValidSubs = 0;
            while (getConsonants(hashmap, vowels, left, right) > k) {
                --hashmap[word[left] - 'a'];
                ++left;
            }
            while (isValidWindow(hashmap, vowels, left, right, k)) {
                ++curValidSubs;
                --hashmap[word[left] - 'a'];
                ++left;
            }
            output += curValidSubs;
        }
        return output;
    }
};