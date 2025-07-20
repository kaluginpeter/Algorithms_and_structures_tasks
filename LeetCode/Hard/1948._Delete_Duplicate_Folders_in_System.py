# Due to a bug, there are many duplicate folders in a file system. You are given a 2D array paths, where paths[i] is an array representing an absolute path to the ith folder in the file system.
#
# For example, ["one", "two", "three"] represents the path "/one/two/three".
# Two folders (not necessarily on the same level) are identical if they contain the same non-empty set of identical subfolders and underlying subfolder structure. The folders do not need to be at the root level to be identical. If two or more folders are identical, then mark the folders as well as all their subfolders.
#
# For example, folders "/a" and "/b" in the file structure below are identical. They (as well as their subfolders) should all be marked:
# /a
# /a/x
# /a/x/y
# /a/z
# /b
# /b/x
# /b/x/y
# /b/z
# However, if the file structure also included the path "/b/w", then the folders "/a" and "/b" would not be identical. Note that "/a/x" and "/b/x" would still be considered identical even with the added folder.
# Once all the identical folders and their subfolders have been marked, the file system will delete all of them. The file system only runs the deletion once, so any folders that become identical after the initial deletion are not deleted.
#
# Return the 2D array ans containing the paths of the remaining folders after deleting all the marked folders. The paths may be returned in any order.
#
#
#
# Example 1:
#
#
# Input: paths = [["a"],["c"],["d"],["a","b"],["c","b"],["d","a"]]
# Output: [["d"],["d","a"]]
# Explanation: The file structure is as shown.
# Folders "/a" and "/c" (and their subfolders) are marked for deletion because they both contain an empty
# folder named "b".
# Example 2:
#
#
# Input: paths = [["a"],["c"],["a","b"],["c","b"],["a","b","x"],["a","b","x","y"],["w"],["w","y"]]
# Output: [["c"],["c","b"],["a"],["a","b"]]
# Explanation: The file structure is as shown.
# Folders "/a/b/x" and "/w" (and their subfolders) are marked for deletion because they both contain an empty folder named "y".
# Note that folders "/a" and "/c" are identical after the deletion, but they are not deleted because they were not marked beforehand.
# Example 3:
#
#
# Input: paths = [["a","b"],["c","d"],["c"],["a"]]
# Output: [["c"],["c","d"],["a"],["a","b"]]
# Explanation: All folders are unique in the file system.
# Note that the returned array can be in a different order as the order does not matter.
#
#
# Constraints:
#
# 1 <= paths.length <= 2 * 104
# 1 <= paths[i].length <= 500
# 1 <= paths[i][j].length <= 10
# 1 <= sum(paths[i][j].length) <= 2 * 105
# path[i][j] consists of lowercase English letters.
# No two paths lead to the same folder.
# For any folder not at the root level, its parent folder will also be in the input.
# Solution
# Python O(NL) O(NL) Trie String
class Trie:
    folder_name: str = ''
    children: dict[str, 'Trie']
    def __init__(self) -> None:
        self.children = dict()

class Solution:
    def build(self, node: Trie, hashmap: dict[str, int]) -> None:
        if not node.children: return
        v: list[str] = []
        for folder, child in node.children.items():
            self.build(child, hashmap)
            v.append(folder + '(' + child.folder_name + ')')
        v.sort()
        for s in v: node.folder_name += s
        hashmap[node.folder_name] = hashmap.get(node.folder_name, 0) + 1

    def traverse(self, node: Trie, hashmap: dict[str, int], output: list[list[str]], path: list[str]) -> None:
        if hashmap.get(node.folder_name, 0) > 1: return
        if path: output.append(path[:])
        for folder, child in node.children.items():
            path.append(folder)
            self.traverse(child, hashmap, output, path)
            path.pop()

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root: Trie = Trie()
        for path in paths:
            cur: Trie = root
            for dir_ in path:
                if dir_ not in cur.children:
                    cur.children[dir_] = Trie()
                cur = cur.children[dir_]
        hashmap: dict[str, int] = dict()
        self.build(root, hashmap)
        output: list[list[str]] = []
        path: list[str] = []
        self.traverse(root, hashmap, output, path)
        return output

# C++ O(NL) O(NL) Trie String
struct Trie {
    std::string folderName;
    std::unordered_map<std::string, Trie*> children;
};

class Solution {
public:
    void build(Trie *node, std::unordered_map<std::string, int> &hashmap) {
        if (node->children.empty()) return;
        std::vector<std::string> v;
        for (const auto& [folder, child] : node->children) {
            build(child, hashmap);
            v.push_back(folder + "(" + child->folderName + ")");
        }
        sort(v.begin(), v.end());
        for (std::string &s : v) node->folderName += move(s);
        ++hashmap[node->folderName];
    };

    void traverse(Trie *node, std::unordered_map<std::string, int> &hashmap, std::vector<std::vector<std::string>> &output, std::vector<std::string> &path) {
        if (hashmap[node->folderName] > 1) return;
        if (!path.empty()) output.push_back(path);
        for (const auto& [folder, child] : node->children) {
            path.push_back(folder);
            traverse(child, hashmap, output, path);
            path.pop_back();
        }
    };

    vector<vector<string>> deleteDuplicateFolder(vector<vector<string>>& paths) {
        Trie* root = new Trie();
        for (const std::vector<std::string> &path : paths) {
            Trie* cur = root;
            for (const std::string &dir : path) {
                if (!cur->children.count(dir)) {
                    cur->children[dir] = new Trie();
                }
                cur = cur->children[dir];
            }
        }
        std::unordered_map<std::string, int> hashmap;
        build(root, hashmap);
        std::vector<std::vector<std::string>> output;
        std::vector<std::string> path;
        traverse(root, hashmap, output, path);
        return output;
    }
};