/*
You are given two arrays of strings wordsContainer and wordsQuery.

For each wordsQuery[i], you need to find a string from wordsContainer that has the longest common suffix with wordsQuery[i]. If there are two or more strings in wordsContainer that share the longest common suffix, find the string that is the smallest in length. If there are two or more such strings that have the same smallest length, find the one that occurred earlier in wordsContainer.

Return an array of integers ans, where ans[i] is the index of the string in wordsContainer that has the longest common suffix with wordsQuery[i].



Example 1:

Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery = ["cd","bcd","xyz"]

Output: [1,1,1]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "cd", strings from wordsContainer that share the longest common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[1] = "bcd", strings from wordsContainer that share the longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
For wordsQuery[2] = "xyz", there is no string from wordsContainer that shares a common suffix. Hence the longest common suffix is "", that is shared with strings at index 0, 1, and 2. Among these, the answer is the string at index 1 because it has the shortest length of 3.
Example 2:

Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery = ["gh","acbfgh","acbfegh"]

Output: [2,0,2]

Explanation:

Let's look at each wordsQuery[i] separately:

For wordsQuery[0] = "gh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.
For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest common suffix "fgh". Hence it is the answer, even though the string at index 2 is shorter.
For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the longest common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is the string at index 2 because it has the shortest length of 6.


Constraints:

1 <= wordsContainer.length, wordsQuery.length <= 104
1 <= wordsContainer[i].length <= 5 * 103
1 <= wordsQuery[i].length <= 5 * 103
wordsContainer[i] consists only of lowercase English letters.
wordsQuery[i] consists only of lowercase English letters.
Sum of wordsContainer[i].length is at most 5 * 105.
Sum of wordsQuery[i].length is at most 5 * 105.
*/
// Solution
// C++ O(N + MD) O(D) Trie
class TrieNode {
public:
    std::array<TrieNode*, 26> children{};
    int pos = INT32_MAX, posSize = INT32_MAX;
    TrieNode() {
        children.fill(nullptr);
    }
};

class Trie {
private:
    TrieNode* root;
public:
    Trie() {
        root = new TrieNode();
    }

    void insert(std::string& s, size_t& pos, int bound) {
        TrieNode* node = root;
        size_t length = s.size();
        for (size_t i = 0; i < bound; ++i) {
            int idx = s[i] - 'a';
            if (!node->children[idx]) {
                node->children[idx] = new TrieNode();
            }
            if (node->posSize > length) {
                node->posSize = length;
                node->pos = pos;
            }
            node = node->children[idx];
        }
        if (node->posSize > length) {
            node->posSize = length;
            node->pos = pos;
        }
    }

    uint16_t getLongestCommonSuffix(std::string& q) {
        TrieNode* node = root;
        for (char& c : q) {
            int idx = c - 'a';
            if (!node->children[idx]) break;
            node = node->children[idx];
        }
        return node->pos;
    }
};

class Solution {
public:
    vector<int> stringIndices(vector<string>& wordsContainer, vector<string>& wordsQuery) {
        size_t n = wordsContainer.size(), m = wordsQuery.size();
        Trie trie;
        size_t bound = 0;
        for (std::string& q : wordsQuery) bound = std::max(bound, q.size());
        for (size_t i = 0; i < n; ++i) {
            std::reverse(wordsContainer[i].begin(), wordsContainer[i].end());
            trie.insert(wordsContainer[i], i, std::min(bound, wordsContainer[i].size()));
        }
        std::vector<int> output;
        for (std::string& q : wordsQuery) {
            std::reverse(q.begin(), q.end());
            output.push_back(trie.getLongestCommonSuffix(q));
        }
        return output;
    }
};