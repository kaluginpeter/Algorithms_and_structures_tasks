# You are given an integer c representing c power stations, each with a unique identifier id from 1 to c (1‑based indexing).
#
# These stations are interconnected via n bidirectional cables, represented by a 2D array connections, where each element connections[i] = [ui, vi] indicates a connection between station ui and station vi. Stations that are directly or indirectly connected form a power grid.
#
# Initially, all stations are online (operational).
#
# You are also given a 2D array queries, where each query is one of the following two types:
#
# [1, x]: A maintenance check is requested for station x. If station x is online, it resolves the check by itself. If station x is offline, the check is resolved by the operational station with the smallest id in the same power grid as x. If no operational station exists in that grid, return -1.
#
# [2, x]: Station x goes offline (i.e., it becomes non-operational).
#
# Return an array of integers representing the results of each query of type [1, x] in the order they appear.
#
# Note: The power grid preserves its structure; an offline (non‑operational) node remains part of its grid and taking it offline does not alter connectivity.
#
#
#
# Example 1:
#
# Input: c = 5, connections = [[1,2],[2,3],[3,4],[4,5]], queries = [[1,3],[2,1],[1,1],[2,2],[1,2]]
#
# Output: [3,2,3]
#
# Explanation:
#
#
#
# Initially, all stations {1, 2, 3, 4, 5} are online and form a single power grid.
# Query [1,3]: Station 3 is online, so the maintenance check is resolved by station 3.
# Query [2,1]: Station 1 goes offline. The remaining online stations are {2, 3, 4, 5}.
# Query [1,1]: Station 1 is offline, so the check is resolved by the operational station with the smallest id among {2, 3, 4, 5}, which is station 2.
# Query [2,2]: Station 2 goes offline. The remaining online stations are {3, 4, 5}.
# Query [1,2]: Station 2 is offline, so the check is resolved by the operational station with the smallest id among {3, 4, 5}, which is station 3.
# Example 2:
#
# Input: c = 3, connections = [], queries = [[1,1],[2,1],[1,1]]
#
# Output: [1,-1]
#
# Explanation:
#
# There are no connections, so each station is its own isolated grid.
# Query [1,1]: Station 1 is online in its isolated grid, so the maintenance check is resolved by station 1.
# Query [2,1]: Station 1 goes offline.
# Query [1,1]: Station 1 is offline and there are no other stations in its grid, so the result is -1.
#
#
# Constraints:
#
# 1 <= c <= 105
# 0 <= n == connections.length <= min(105, c * (c - 1) / 2)
# connections[i].length == 2
# 1 <= ui, vi <= c
# ui != vi
# 1 <= queries.length <= 2 * 105
# queries[i].length == 2
# queries[i][0] is either 1 or 2.
# 1 <= queries[i][1] <= c
# Solution
# Python O(N + M + K) O(N + M) DisjointSetUnion PriorityQueue HashMap
class DSU:
    def __init__(self, n: int) -> None:
        self.rank: list[int] = [1] * n
        self.parent: list[int] = list(range(n))
        self.powerset: dict[int, list[int]] = dict((i, [i]) for i in range(n))
        self.offline: set[int] = set()

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, u: int, v: int) -> None:
        u_parent: int = self.find(u)
        v_parent: int = self.find(v)
        if u_parent == v_parent: return
        if self.rank[u_parent] >= self.rank[v_parent]:
            self.parent[v_parent] = u_parent
            self.rank[u_parent] += self.rank[v_parent]
            while self.powerset[v_parent]:
                heapq.heappush(self.powerset[u_parent], heapq.heappop(self.powerset[v_parent]))
        else:
            self.parent[u_parent] = v_parent
            self.rank[v_parent] += self.rank[u_parent]
            while self.powerset[u_parent]:
                heapq.heappush(self.powerset[v_parent], heapq.heappop(self.powerset[u_parent]))

    def turn_off(self, x: int) -> None:
        self.offline.add(x)

    def maintain(self, x: int) -> int:
        if x not in self.offline: return x
        root: int = self.find(x)
        while self.powerset[root] and self.powerset[root][0] in self.offline:
            heapq.heappop(self.powerset[root])
        return -1 if not self.powerset[root] else self.powerset[root][0]


class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        dsu: DSU = DSU(c + 1)
        for u, v in connections: dsu.union(u, v)
        output: list[int] = []
        for type_, x in queries:
            match type_:
                case 1:
                    output.append(dsu.maintain(x))
                case 2:
                    dsu.turn_off(x)
        return output

# C++ O(N + M + K) O(N + M) DisjointSetUnion PriorityQueue HashMap
class DSU {
public:
    std::vector<int> parent, rank;
    std::unordered_set<int> offline;
    std::unordered_map<int, std::priority_queue<int, std::vector<int>, std::greater<int>>> powerset;
public:
    DSU (int n) {
        for (int i = 0; i < n; ++i) {
            powerset[i].push(i);
            parent.push_back(i);
            rank.push_back(1);
        }
    };
    int find(int node) {
        while (parent[node] != node) {
            parent[node] = parent[parent[node]];
            node = parent[node];
        }
        return node;
    }
    void union_(int x, int y) {
        int parentX = find(x), parentY = find(y);
        if (parentX == parentY) return;
        if (rank[parentX] >= rank[parentY]) {
            parent[parentY] = parentX;
            rank[parentX] += rank[parentY];
            while (!powerset[parentY].empty()) {
                powerset[parentX].push(powerset[parentY].top());
                powerset[parentY].pop();
            }
        } else {
            parent[parentX] = parentY;
            rank[parentY] += rank[parentX];
            while (!powerset[parentX].empty()) {
                powerset[parentY].push(powerset[parentX].top());
                powerset[parentX].pop();
            }
        }
    }

    int maintain(int node) {
        if (!offline.count(node)) return node;
        int root = find(node);
        while (!powerset[root].empty() && offline.count(powerset[root].top())) {
            powerset[root].pop();
        }
        return (powerset[root].empty() ? -1 : powerset[root].top());
    }

    void turnOff(int node) {
        offline.insert(node);
    }
};

class Solution {
public:
    vector<int> processQueries(int c, vector<vector<int>>& connections, vector<vector<int>>& queries) {
        DSU dsu(c + 1);
        for (std::vector<int>& edge : connections) dsu.union_(edge[0], edge[1]);
        std::vector<int> output;
        for (std::vector<int>& query : queries) {
            if (query[0] == 1) output.push_back(dsu.maintain(query[1]));
            else dsu.turnOff(query[1]);
        }
        return output;
    }
};