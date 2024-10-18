# You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.
#
# You can swap the characters at any pair of indices in the given pairs any number of times.
#
# Return the lexicographically smallest string that s can be changed to after using the swaps.
#
#
#
# Example 1:
#
# Input: s = "dcab", pairs = [[0,3],[1,2]]
# Output: "bacd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[1] and s[2], s = "bacd"
# Example 2:
#
# Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
# Output: "abcd"
# Explaination:
# Swap s[0] and s[3], s = "bcad"
# Swap s[0] and s[2], s = "acbd"
# Swap s[1] and s[2], s = "abcd"
# Example 3:
#
# Input: s = "cba", pairs = [[0,1],[1,2]]
# Output: "abc"
# Explaination:
# Swap s[0] and s[1], s = "bca"
# Swap s[1] and s[2], s = "bac"
# Swap s[0] and s[1], s = "abc"
#
#
# Constraints:
#
# 1 <= s.length <= 10^5
# 0 <= pairs.length <= 10^5
# 0 <= pairs[i][0], pairs[i][1] < s.length
# s only contains lower case English letters.
# Solution
# Python O(NlogN) O(N) Union Find HashMap Sorting
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = list(range(n))
        self.ranks: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union_find(self, x: int, y: int) -> None:
        root_x: int = self.find(x)
        root_y: int = self.find(y)
        if root_x == root_y:
            return
        if self.ranks[root_x] >= self.ranks[root_y]:
            self.parents[root_y] = root_x
            self.ranks[root_x] += self.ranks[root_y]
        else:
            self.parents[root_x] = root_y
            self.ranks[root_y] += self.ranks[root_x]


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        UF: UnionFind = UnionFind(len(s))
        for pair in pairs:
            UF.union_find(*pair)
        hashmap: dict[int, list[int]] = dict()
        for node in range(len(s)):
            parent: int = UF.find(node)
            if parent not in hashmap:
                hashmap[parent] = list()
            hashmap[parent].append(node)
        answer: list[str] = list()
        for component in hashmap:
            hashmap[component].sort(key=lambda idx: s[idx], reverse=True)
        for component_idx in range(len(s)):
            answer.append(s[hashmap[UF.find(component_idx)].pop()])
        return ''.join(answer)

# C++ O(NlogN) O(N) UnionFind Priority Queue
class UnionFind {
public:
    std::vector<int> parents;
    std::vector<int> ranks;
    UnionFind(int n) {
        parents.resize(n);
        std::iota(parents.begin(), parents.end(), 0);
        ranks.resize(n, 1);
    };

    int find(int x) {
        while (x != parents[x]) {
            parents[x] = parents[parents[x]];
            x = parents[x];
        }
        return x;
    }

    void unionFind(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) {
            return;
        }
        if (ranks[rootX] >= ranks[rootY]) {
            parents[rootY] = rootX;
            ranks[rootX] += ranks[rootY];
        } else {
            parents[rootX] = rootY;
            ranks[rootY] += ranks[rootX];
        }
    }
};

class Solution {
public:
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        UnionFind* UF = new UnionFind(static_cast<int>(s.size()));
        for (std::vector<int>& pair : pairs) {
            UF->unionFind(pair[0], pair[1]);
        }
        std::map<int, priority_queue<char, vector<char>, greater<char>>> pq;
        for(int index = 0; index < s.size(); ++index){
            pq[UF->find(index)].push(s[index]);
        }
        for (int index = 0; index < s.size(); ++index) {
            s[index] = pq[UF->find(index)].top();
            pq[UF->find(index)].pop();
        }
        return s;
    }
};