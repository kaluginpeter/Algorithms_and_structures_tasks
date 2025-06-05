# You are given two strings of the same length s1 and s2 and a string baseStr.
#
# We say s1[i] and s2[i] are equivalent characters.
#
# For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
# Equivalent characters follow the usual rules of any equivalence relation:
#
# Reflexivity: 'a' == 'a'.
# Symmetry: 'a' == 'b' implies 'b' == 'a'.
# Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
# For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.
#
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
#
#
#
# Example 1:
#
# Input: s1 = "parker", s2 = "morris", baseStr = "parser"
# Output: "makkek"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [m,p], [a,o], [k,r,s], [e,i].
# The characters in each group are equivalent and sorted in lexicographical order.
# So the answer is "makkek".
# Example 2:
#
# Input: s1 = "hello", s2 = "world", baseStr = "hold"
# Output: "hdld"
# Explanation: Based on the equivalency information in s1 and s2, we can group their characters as [h,w], [d,e,o], [l,r].
# So only the second letter 'o' in baseStr is changed to 'd', the answer is "hdld".
# Example 3:
#
# Input: s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"
# Output: "aauaaaaada"
# Explanation: We group the equivalent characters in s1 and s2 as [a,o,e,r,s,c], [l,p], [g,t] and [d,m], thus all letters in baseStr except 'u' and 'd' are transformed to 'a', the answer is "aauaaaaada".
#
#
# Constraints:
#
# 1 <= s1.length, s2.length, baseStr <= 1000
# s1.length == s2.length
# s1, s2, and baseStr consist of lowercase English letters.
# Python O(N + M) O(N) Disjoint-Set-Union Graph String
class DSU:
    def __init__(self, n: int) -> None:
        self.n: int = n
        self.smallest_vertex: list[int] = list(range(n))
        self.rank: list[int] = [1] * n
        self.parent: list[int] = list(range(n))

    def get_parent(self, x: str) -> int:
        x_: int = ord(x) - 97
        while x_ != self.parent[x_]:
            self.parent[x_] = self.parent[self.parent[x_]]
            x_ = self.parent[x_]
        return x_

    def union(self, x: str, y: str) -> None:
        x_parent: int = self.get_parent(x)
        y_parent: int = self.get_parent(y)
        if x_parent == y_parent: return
        if self.rank[x_parent] > self.rank[y_parent]:
            self.rank[x_parent] += self.rank[y_parent]
            self.parent[y_parent] = x_parent
            self.smallest_vertex[x_parent] = min(self.smallest_vertex[x_parent], self.smallest_vertex[y_parent])
        else:
            self.rank[y_parent] += self.rank[x_parent]
            self.parent[x_parent] = y_parent
            self.smallest_vertex[y_parent] = min(self.smallest_vertex[y_parent], self.smallest_vertex[x_parent])


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n: int = 26
        dsu: DSU = DSU(n)
        for i in range(len(s1)):
            dsu.union(s1[i], s2[i])
        output: list[str] = []
        for i in range(len(baseStr)):
            output.append(chr(dsu.smallest_vertex[dsu.get_parent(baseStr[i])] + 97))
        return ''.join(output)

# C++ O(N + M) O(N) Disjoint-Set-Union Graph String
class DSU {
public:
    int n_;
    vector<int> smallestVertex;
    vector<int> parent, rank;
    DSU(int n) : n_(n) {
        for (int i = 0; i < n; ++i){
            smallestVertex.push_back(i);
            parent.push_back(i);
        }
        rank.resize(n, 1);
    };
    int getParent(char x) {
        int x_ = x - 'a';
        while (x_ != parent[x_]) {
            parent[x_] = parent[parent[x_]];
            x_ = parent[x_];
        }
        return x_;
    }

    void union_(char x, char y) {
        int xParent = getParent(x);
        int yParent = getParent(y);
        if (parent[xParent] == parent[yParent]) return;
        if (rank[xParent] > rank[yParent]) {
            parent[yParent] = xParent;
            rank[xParent] += rank[yParent];
            smallestVertex[xParent] = min(smallestVertex[xParent], smallestVertex[yParent]);
        } else {
            parent[xParent] = yParent;
            rank[yParent] += rank[xParent];
            smallestVertex[yParent] = min(smallestVertex[yParent], smallestVertex[xParent]);
        }
    }
};
class Solution {
public:
    string smallestEquivalentString(string s1, string s2, string baseStr) {
        DSU dsu = DSU(26);
        for (int i = 0; i < s1.size(); ++i) {
            dsu.union_(s1[i], s2[i]);
        }
        string output = "";
        for (int i = 0; i < baseStr.size(); ++i) {
            output.push_back(char(dsu.smallestVertex[dsu.getParent(baseStr[i])]) + 97);
        }
        return output;
    }
};