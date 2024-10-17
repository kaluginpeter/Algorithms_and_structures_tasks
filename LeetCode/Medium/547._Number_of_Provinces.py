# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
#
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
#
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
#
# Return the total number of provinces.
#
#
#
# Example 1:
#
#
# Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
# Output: 2
# Example 2:
#
#
# Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
# Output: 3
#
#
# Constraints:
#
# 1 <= n <= 200
# n == isConnected.length
# n == isConnected[i].length
# isConnected[i][j] is 1 or 0.
# isConnected[i][i] == 1
# isConnected[i][j] == isConnected[j][i]
# Solution
# Python O(NM) O(N) UnionFind
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = list(range(n))
        self.ranks: list[int] = [0] * n
        self.connections: int = n

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def union(self, i: int, j: int) -> None:
        parent_i: int = self.find(i)
        parent_j: int = self.find(j)
        if parent_i == parent_j:
            return
        self.connections -= 1
        if self.ranks[parent_i] >= self.ranks[parent_j]:
            self.parents[parent_j] = parent_i
            self.ranks[parent_i] += 1
        else:
            self.parents[parent_i] = parent_j
            self.ranks[parent_j] += 1


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        union_find: UnionFind = UnionFind(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    union_find.union(i, j)
        return union_find.connections

# C++ O(NM) O(N) UnionFind
class UnionFind {
public:
    UnionFind(int n) {
        connections = n;
        for (int rank = 0; rank < n; ++rank) {
            parents.push_back(rank);
        }
        ranks = std::vector<int>(n, 0);
    };
    int connections;
    std::vector<int> parents;
    std::vector<int> ranks;

    int find(int city) {
        while (city != parents[city]) {
            parents[city] = parents[parents[city]];
            city = parents[city];
        }
        return city;
    };

    void unionFind(int city1, int city2) {
        int parentCity1 = find(city1);
        int parentCity2 = find(city2);
        if (parentCity1 == parentCity2) {
            return;
        }
        --connections;
        if (ranks[parentCity1] >= ranks[parentCity2]) {
            parents[parentCity2] = parentCity1;
            ++ranks[parentCity1];
        } else {
            parents[parentCity1] = parentCity2;
            ++ranks[parentCity2];
        }
    }
};

class Solution {
public:
    int findCircleNum(vector<vector<int>>& isConnected) {
        int n = static_cast<int>(isConnected.size());
        UnionFind* UF = new UnionFind(n);
        for (int city1 = 0; city1 < n; ++city1) {
            for (int city2 = 0; city2 < n; ++city2) {
                if (isConnected[city1][city2]) {
                    UF->unionFind(city1, city2);
                }
            }
        }
        return UF->connections;
    }
};