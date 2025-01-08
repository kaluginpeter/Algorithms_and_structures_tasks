# You are given a 0-indexed string array words.
#
# Let's define a boolean function isPrefixAndSuffix that takes two strings, str1 and str2:
#
# isPrefixAndSuffix(str1, str2) returns true if str1 is both a
# prefix
#  and a
# suffix
#  of str2, and false otherwise.
# For example, isPrefixAndSuffix("aba", "ababa") is true because "aba" is a prefix of "ababa" and also a suffix, but isPrefixAndSuffix("abc", "abcd") is false.
#
# Return an integer denoting the number of index pairs (i, j) such that i < j, and isPrefixAndSuffix(words[i], words[j]) is true.
#
#
#
# Example 1:
#
# Input: words = ["a","aba","ababa","aa"]
# Output: 4
# Explanation: In this example, the counted index pairs are:
# i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
# i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
# i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
# i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
# Therefore, the answer is 4.
# Example 2:
#
# Input: words = ["pa","papa","ma","mama"]
# Output: 2
# Explanation: In this example, the counted index pairs are:
# i = 0 and j = 1 because isPrefixAndSuffix("pa", "papa") is true.
# i = 2 and j = 3 because isPrefixAndSuffix("ma", "mama") is true.
# Therefore, the answer is 2.
# Example 3:
#
# Input: words = ["abab","ab"]
# Output: 0
# Explanation: In this example, the only valid index pair is i = 0 and j = 1, and isPrefixAndSuffix("abab", "ab") is false.
# Therefore, the answer is 0.
#
#
# Constraints:
#
# 1 <= words.length <= 105
# 1 <= words[i].length <= 105
# words[i] consists only of lowercase English letters.
# The sum of the lengths of all words[i] does not exceed 5 * 105.
# Solution
# Python O(KM) O(KM), where K is the length of words and M is the length of longest word. Trie
class TrieNode:
    def __init__(self) -> None:
        self.childs: dict[tuple[str, str], TrieNode] = dict()
        self.count: int = 0


class PrefixTrie:
    def __init__(self) -> None:
        self.head: TrieNode = TrieNode()

    def insert_word(self, word: str) -> None:
        tmp: TrieNode = self.head
        for letter_idx in range(len(word)):
            letter: str = word[letter_idx]
            pair: tuple[str, str] = (letter, word[len(word) - letter_idx - 1])
            if pair not in tmp.childs:
                tmp.childs[pair] = TrieNode()
            tmp = tmp.childs[pair]
        tmp.count += 1

    def get_prefix(self, word: str) -> int:
        prefixes: int = 0
        tmp: TrieNode = self.head
        for idx in range(len(word)):
            pair: tuple[str, str] = (word[idx], word[len(word) - idx - 1])
            if pair not in tmp.childs:
                break
            tmp = tmp.childs[pair]
            prefixes += tmp.count
        return prefixes


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        prefix_trie: PrefixTrie = PrefixTrie()
        output: int = 0
        for word in words:
            output += prefix_trie.get_prefix(word)
            prefix_trie.insert_word(word)
        return output

# C++ O(KM) O(KM) where K is the length of words and M is the length of the longest word. Trie
struct TupleHash {
    size_t operator()(const std::tuple<char, char>& tuple) const {
        size_t hash1 = std::hash<char>()(std::get<0>(tuple));
        size_t hash2 = std::hash<char>()(std::get<1>(tuple));
        return hash1 ^ (hash2 << 1);
    }
};


class TrieNode {
public:
    std::unordered_map<std::tuple<char, char>, TrieNode, TupleHash> childs;
    int count = 0;
    TrieNode() {};
};

class PrefixTrie {
public:
    TrieNode* head;
    PrefixTrie() {
        head = new TrieNode();
    };

    void insertWord(std::string& word) {
        TrieNode* tmp = head;
        int n = word.size();
        for (int idx = 0; idx < n; ++idx) {
            std::tuple<char, char> pair = {word[idx], word[n - idx - 1]};
            if (!tmp->childs.count(pair)) {
                tmp->childs[pair] = TrieNode();
            }
            tmp = &tmp->childs[pair];
        }
        ++tmp->count;
    }

    long long getPrefixes(std::string& word) {
        long long prefixes = 0;
        int n = word.size();
        TrieNode* tmp = head;
        for (int idx = 0; idx < n; ++idx) {
            std::tuple<char, char> pair = {word[idx], word[n - idx - 1]};
            if (!tmp->childs.count(pair)) {
                break;
            }
            tmp = &tmp->childs[pair];
            prefixes += tmp->count;
        }
        return prefixes;
    }
};

class Solution {
public:
    long long countPrefixSuffixPairs(vector<string>& words) {
        PrefixTrie prefixTrie = PrefixTrie();
        long long output = 0;
        for (std::string& word : words) {
            output += prefixTrie.getPrefixes(word);
            prefixTrie.insertWord(word);
        }
        return output;
    }
};