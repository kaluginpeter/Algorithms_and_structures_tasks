# You are given two 0-indexed strings source and target, both of length n and consisting of lowercase English characters. You are also given two 0-indexed string arrays original and changed, and an integer array cost, where cost[i] represents the cost of converting the string original[i] to the string changed[i].
#
# You start with the string source. In one operation, you can pick a substring x from the string, and change it to y at a cost of z if there exists any index j such that cost[j] == z, original[j] == x, and changed[j] == y. You are allowed to do any number of operations, but any pair of operations must satisfy either of these two conditions:
#
# The substrings picked in the operations are source[a..b] and source[c..d] with either b < c or d < a. In other words, the indices picked in both operations are disjoint.
# The substrings picked in the operations are source[a..b] and source[c..d] with a == c and b == d. In other words, the indices picked in both operations are identical.
# Return the minimum cost to convert the string source to the string target using any number of operations. If it is impossible to convert source to target, return -1.
#
# Note that there may exist indices i, j such that original[j] == original[i] and changed[j] == changed[i].
#
#
#
# Example 1:
#
# Input: source = "abcd", target = "acbe", original = ["a","b","c","c","e","d"], changed = ["b","c","b","e","b","e"], cost = [2,5,5,1,2,20]
# Output: 28
# Explanation: To convert "abcd" to "acbe", do the following operations:
# - Change substring source[1..1] from "b" to "c" at a cost of 5.
# - Change substring source[2..2] from "c" to "e" at a cost of 1.
# - Change substring source[2..2] from "e" to "b" at a cost of 2.
# - Change substring source[3..3] from "d" to "e" at a cost of 20.
# The total cost incurred is 5 + 1 + 2 + 20 = 28.
# It can be shown that this is the minimum possible cost.
# Example 2:
#
# Input: source = "abcdefgh", target = "acdeeghh", original = ["bcd","fgh","thh"], changed = ["cde","thh","ghh"], cost = [1,3,5]
# Output: 9
# Explanation: To convert "abcdefgh" to "acdeeghh", do the following operations:
# - Change substring source[1..3] from "bcd" to "cde" at a cost of 1.
# - Change substring source[5..7] from "fgh" to "thh" at a cost of 3. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation.
# - Change substring source[5..7] from "thh" to "ghh" at a cost of 5. We can do this operation because indices [5,7] are disjoint with indices picked in the first operation, and identical with indices picked in the second operation.
# The total cost incurred is 1 + 3 + 5 = 9.
# It can be shown that this is the minimum possible cost.
# Example 3:
#
# Input: source = "abcdefgh", target = "addddddd", original = ["bcd","defgh"], changed = ["ddd","ddddd"], cost = [100,1578]
# Output: -1
# Explanation: It is impossible to convert "abcdefgh" to "addddddd".
# If you select substring source[1..3] as the first operation to change "abcdefgh" to "adddefgh", you cannot select substring source[3..7] as the second operation because it has a common index, 3, with the first operation.
# If you select substring source[3..7] as the first operation to change "abcdefgh" to "abcddddd", you cannot select substring source[1..3] as the second operation because it has a common index, 3, with the first operation.
#
#
# Constraints:
#
# 1 <= source.length == target.length <= 1000
# source, target consist only of lowercase English characters.
# 1 <= cost.length == original.length == changed.length <= 100
# 1 <= original[i].length == changed[i].length <= source.length
# original[i], changed[i] consist only of lowercase English characters.
# original[i] != changed[i]
# 1 <= cost[i] <= 106
# Solution
# C++ O(N^2 + M^3 + ML) O(N + M^2 + ML) Trie Graph
static constexpr int inf = INT_MAX / 2;
struct Trie {
    Trie* child[26];
    int id;
    Trie() {
        for (int i = 0; i < 26; ++i) child[i] = nullptr;
        id = -1;
    }
};

int add(Trie* node, const string& word, int& index) {
    for (char ch : word) {
        int i = ch - 'a';
        if (!node->child[i]) node->child[i] = new Trie();
        node = node->child[i];
    }
    if (node->id == -1) node->id = ++index;
    return node->id;
}

void update(long long& x, long long y) {
    if (x == -1 || y < x) x = y;
}

class Solution {
public:
    long long minimumCost(string source, string target, vector<string>& original, vector<string>& changed, vector<int>& cost) {
        int n = source.size();
        int m = original.size();
        Trie* root = new Trie();
        int p = -1;
        vector<vector<int>> G(m * 2, vector<int>(m * 2, inf));
        for (int i = 0; i < m * 2; ++i) G[i][i] = 0;
        for (int i = 0; i < m; ++i) {
            int x = add(root, original[i], p);
            int y = add(root, changed[i], p);
            G[x][y] = min(G[x][y], cost[i]);
        }
        for (int k = 0; k <= p; ++k) {
            for (int i = 0; i <= p; ++i) {
                for (int j = 0; j <= p; ++j) {
                    G[i][j] = min(G[i][j], G[i][k] + G[k][j]);
                }
            }
        }
        vector<long long> f(n, -1);
        for (int j = 0; j < n; ++j) {
            if (j > 0 && f[j - 1] == -1) continue;
            long long base = (j == 0 ? 0 : f[j - 1]);
            if (source[j] == target[j]) update(f[j], base);
            Trie* u = root;
            Trie* v = root;
            for (int i = j; i < n; ++i) {
                u = u->child[source[i] - 'a'];
                v = v->child[target[i] - 'a'];
                if (!u || !v) break;
                if (u->id != -1 && v->id != -1 && G[u->id][v->id] != inf) update(f[i], base + G[u->id][v->id]);
            }
        }
        return f[n - 1];
    }
};