# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.
# Solution
# Python O(K), where K is length of prefix or word, O(N) Prefix Tree Trie HashMap
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.end_of_word: bool = False
class Trie:

    def __init__(self):
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                current_node.childrens[char] = TrieNode()
            current_node = current_node.childrens[char]
        current_node.end_of_word = True

    def search(self, word: str) -> bool:
        current_node: TrieNode = self.root
        for char in word:
            if char not in current_node.childrens:
                return False
            current_node = current_node.childrens[char]
        return current_node.end_of_word

    def startsWith(self, prefix: str) -> bool:
        current_node: TrieNode = self.root
        for char in prefix:
            if char not in current_node.childrens:
                return False
            current_node = current_node.childrens[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

# C++ O(K), where K is length of prefix or word O(N) Trie Prefix Tree HashMap
class TrieNode {
public:
    TrieNode() {}
    std::unordered_map<char, TrieNode*> childrens;
    bool is_end_of_word = false;
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    void insert(string word) {
        TrieNode* current_node = root;
        for (char letter : word) {
            if (!current_node->childrens[letter]) {
                current_node->childrens[letter] = new TrieNode();
            }
            current_node = current_node->childrens[letter];
        }
        current_node->is_end_of_word = true;
    }

    bool search(string word) {
        TrieNode* current_node = root;
        for (char letter : word) {
            if (!current_node->childrens[letter]) {
                return false;
            }
            current_node = current_node->childrens[letter];
        }
        return current_node->is_end_of_word;
    }

    bool startsWith(string prefix) {
        TrieNode* current_node = root;
        for (char letter : prefix) {
            if (!current_node->childrens[letter]) {
                return false;
            }
            current_node = current_node->childrens[letter];
        }
        return true;
    }
private:
    TrieNode* root;
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */