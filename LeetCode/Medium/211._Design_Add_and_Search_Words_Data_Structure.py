# Design a data structure that supports adding new words and finding if a string matches any previously added string.
#
# Implement the WordDictionary class:
#
# WordDictionary() Initializes the object.
# void addWord(word) Adds word to the data structure, it can be matched later.
# bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
#
#
# Example:
#
# Input
# ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
# [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
# Output
# [null,null,null,null,false,true,true,true]
#
# Explanation
# WordDictionary wordDictionary = new WordDictionary();
# wordDictionary.addWord("bad");
# wordDictionary.addWord("dad");
# wordDictionary.addWord("mad");
# wordDictionary.search("pad"); // return False
# wordDictionary.search("bad"); // return True
# wordDictionary.search(".ad"); // return True
# wordDictionary.search("b.."); // return True
#
#
# Constraints:
#
# 1 <= word.length <= 25
# word in addWord consists of lowercase English letters.
# word in search consist of '.' or lowercase English letters.
# There will be at most 2 dots in word for search queries.
# At most 104 calls will be made to addWord and search.
# Solution
# C++ Depth-First-Search Trie HashMap
# Time complexity:
# addWord O(L)
# search O(LC)
# Space complexity: O(C)
# Where L is length of inserted or searched word and C is number of nodes in Trie
class TrieNode {
public:
    TrieNode() : is_end_of_word(false) {};
    std::unordered_map<int, TrieNode*> childrens;
    bool is_end_of_word;
};

class WordDictionary {
private:
    TrieNode* root;
public:
    WordDictionary() {
        root = new TrieNode();
    }

    void addWord(const std::string& word) {
        TrieNode* current_node = root;
        for (char letter : word) {
            if (!current_node->childrens[letter]) {
                current_node->childrens[letter] = new TrieNode();
            }
            current_node = current_node->childrens[letter];
        }
        current_node->is_end_of_word = true;
    }

    bool search(const std::string& word) {
        TrieNode* current_node = root;
        for (size_t index = 0; index < word.size(); ++index) {
            if (word[index] == '.') {
                for (auto& pair : current_node->childrens) {
                    TrieNode* possible_node = pair.second;
                    bool check = possible_search(possible_node, index + 1, word);
                    if (check) {
                        return true;
                    }
                }
                return false;
            }
            if (!current_node->childrens[word[index]]) {
                return false;
            }
            current_node = current_node->childrens[word[index]];
        }
        return current_node->is_end_of_word;
    }

    bool possible_search(TrieNode* current_node, int start, const std::string& word) {
        if (!current_node) {
            return false;
        }
        for (size_t index = start; index < word.size(); ++index) {
            if (word[index] == '.') {
                for (auto& pair : current_node->childrens) {
                    TrieNode* possible_node = pair.second;
                    bool check = possible_search(possible_node, index + 1, word);
                    if (check) {
                        return true;
                    }
                }
                return false;
            }
            if (!current_node->childrens[word[index]]) {
                return false;
            }
            current_node = current_node->childrens[word[index]];
        }
        return current_node->is_end_of_word;
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */

# Python Depth-First-Search Trie HashMap
# Time complexity:
# addWord O(L)
# search O(LC)
# Space complexity: O(C)
# Where L is length of inserted or searched word and C is number of nodes in Trie
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.is_end_of_word: bool = False


class WordDictionary:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def addWord(self, word: str) -> None:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                current_node.childrens[char] = TrieNode()
            current_node = current_node.childrens[char]
        current_node.is_end_of_word = True

    def search(self, word: str) -> bool:
        current_node: TrieNode = self.root
        for idx in range(len(word)):
            if word[idx] == '.':
                for possible_node in current_node.childrens:
                    check: bool = self.possible_changes(
                        current_node.childrens[possible_node], idx + 1, word
                    )
                    if check:
                        return True
                return False
            if word[idx] not in current_node.childrens:
                return False
            current_node = current_node.childrens[word[idx]]
        return current_node.is_end_of_word

    def possible_changes(self, current_node: TrieNode, start: int, word: str) -> bool:
        for idx in range(start, len(word)):
            if word[idx] == '.':
                for possible_node in current_node.childrens:
                    check: bool = self.possible_changes(
                        current_node.childrens[possible_node], idx + 1, word
                    )
                    if check:
                        return True
                return False
            if word[idx] not in current_node.childrens:
                return False
            current_node = current_node.childrens[word[idx]]
        return current_node.is_end_of_word

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)