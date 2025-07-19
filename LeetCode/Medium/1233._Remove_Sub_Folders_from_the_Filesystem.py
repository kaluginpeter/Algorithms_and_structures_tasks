# Given a list of folders folder, return the folders after removing all sub-folders in those folders. You may return the answer in any order.
#
# If a folder[i] is located within another folder[j], it is called a sub-folder of it. A sub-folder of folder[j] must start with folder[j], followed by a "/". For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".
#
# The format of a path is one or more concatenated strings of the form: '/' followed by one or more lowercase English letters.
#
# For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.
#
#
# Example 1:
#
# Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
# Output: ["/a","/c/d","/c/f"]
# Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.
# Example 2:
#
# Input: folder = ["/a","/a/b/c","/a/b/d"]
# Output: ["/a"]
# Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".
# Example 3:
#
# Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
# Output: ["/a/b/c","/a/b/ca","/a/b/d"]
#
#
# Constraints:
#
# 1 <= folder.length <= 4 * 104
# 2 <= folder[i].length <= 100
# folder[i] contains only lowercase letters and '/'.
# folder[i] always starts with the character '/'.
# Each folder name is unique.
# Solution
# C++ O(NL) O(NL) Trie Depth-First-Search
class TrieNode {
public:
    std::unordered_map<std::string, TrieNode*> childrens;
    bool isEndOfWord;
    TrieNode() {
        isEndOfWord = false;
    };
};

class Trie {
public:
    TrieNode* root;
    Trie() {
        root = new TrieNode();
    };

    void insertWord(std::string folder) {
        TrieNode* tmp = root;
        std::string word = "";
        for (int index = 1; index < folder.size(); ++index) {
            if (folder[index] == '/') {
                if (!tmp->childrens[word]) {
                    tmp->childrens[word] = new TrieNode();
                }
                tmp = tmp->childrens[word];
                word = "";
            } else {
                word += folder[index];
            }
        }
        if (!tmp->childrens[word]) {
            tmp->childrens[word] = new TrieNode();
        }
        tmp = tmp->childrens[word];
        tmp->isEndOfWord = true;
    };

    void uniqueFolders(TrieNode* node, std::string& path, std::vector<std::string>& output) {
        if (node->isEndOfWord) {
            output.push_back(path);
            return;
        }
        for (std::pair<const std::string, TrieNode*> pair : node->childrens) {
            std::string nextNode = pair.first;
            if (node->childrens[nextNode]) {
                std::string nextFolder = '/' + nextNode;
                path += nextFolder;
                uniqueFolders(pair.second, path, output);
                int k = nextFolder.size();
                path.erase(path.size() - k, k);
            }
        }
    };
};

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        Trie* T= new Trie();
        for (std::string word : folder) {
            T->insertWord(word);
        }
        std::vector<std::string> output;
        std::string path = "";
        T->uniqueFolders(T->root, path, output);
        return output;
    }
};

# Python O(NL) O(NL) Trie Depth-First-Search
class TrieNode:
    def __init__(self) -> None:
        self.childrens: dict[str, TrieNode] = dict()
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert_word(self, word: str) -> None:
        tmp: TrieNode = self.root
        folder: str = ''
        for idx in range(1, len(word)):
            if word[idx] == '/':
                if folder not in tmp.childrens:
                    tmp.childrens[folder] = TrieNode()
                tmp = tmp.childrens[folder]
                folder = ''
            else:
                folder += word[idx]
        if folder not in tmp.childrens:
            if folder not in tmp.childrens:
                tmp.childrens[folder] = TrieNode()
        tmp = tmp.childrens[folder]
        tmp.is_end_of_word = True

    def unique_folders(self, node: TrieNode, path: list[str], output: list[str]) -> None:
        if node.is_end_of_word:
            output.append(''.join(path))
            return
        for pair in node.childrens.items():
            next_char: str = pair[0]
            next_node: TrieNode = pair[1]
            new_folder: str = '/' + next_char
            path.append(new_folder)
            self.unique_folders(next_node, path, output)
            path.pop()


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        T: Trie = Trie()
        for word in folder:
            T.insert_word(word)
        output: list[str] = []
        path: list[str] = []
        T.unique_folders(T.root, path, output)
        return output


# Python O(N * LlogN + NL) O(NL) Sorting
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        pattern: str = folder[0]
        output: list[str] = [pattern]
        pattern += '/'
        for right in range(1, len(folder)):
            if not folder[right].startswith(pattern):
                output.append(folder[right])
                pattern = folder[right] + '/'
        return output

# C++ O(N * LlogN + NL) O(NL) Sorting
class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folder) {
        std::sort(folder.begin(), folder.end());
        std::vector<std::string> output;
        output.push_back(folder[0]);
        std::string pattern = folder[0] + "/";
        for (int right = 1; right < folder.size(); ++right) {
            if (!folder[right].starts_with(pattern)) {
                output.push_back(folder[right]);
                pattern = folder[right];
                pattern.push_back('/');
            }
        }
        return output;
    }
};