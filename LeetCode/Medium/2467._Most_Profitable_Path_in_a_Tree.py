# There is an undirected tree with n nodes labeled from 0 to n - 1, rooted at node 0. You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.
#
# At every node i, there is a gate. You are also given an array of even integers amount, where amount[i] represents:
#
# the price needed to open the gate at node i, if amount[i] is negative, or,
# the cash reward obtained on opening the gate at node i, otherwise.
# The game goes on as follows:
#
# Initially, Alice is at node 0 and Bob is at node bob.
# At every second, Alice and Bob each move to an adjacent node. Alice moves towards some leaf node, while Bob moves towards node 0.
# For every node along their path, Alice and Bob either spend money to open the gate at that node, or accept the reward. Note that:
# If the gate is already open, no price will be required, nor will there be any cash reward.
# If Alice and Bob reach the node simultaneously, they share the price/reward for opening the gate there. In other words, if the price to open the gate is c, then both Alice and Bob pay c / 2 each. Similarly, if the reward at the gate is c, both of them receive c / 2 each.
# If Alice reaches a leaf node, she stops moving. Similarly, if Bob reaches node 0, he stops moving. Note that these events are independent of each other.
# Return the maximum net income Alice can have if she travels towards the optimal leaf node.
#
#
#
# Example 1:
#
#
# Input: edges = [[0,1],[1,2],[1,3],[3,4]], bob = 3, amount = [-2,4,2,-4,6]
# Output: 6
# Explanation:
# The above diagram represents the given tree. The game goes as follows:
# - Alice is initially on node 0, Bob on node 3. They open the gates of their respective nodes.
#   Alice's net income is now -2.
# - Both Alice and Bob move to node 1.
#   Since they reach here simultaneously, they open the gate together and share the reward.
#   Alice's net income becomes -2 + (4 / 2) = 0.
# - Alice moves on to node 3. Since Bob already opened its gate, Alice's income remains unchanged.
#   Bob moves on to node 0, and stops moving.
# - Alice moves on to node 4 and opens the gate there. Her net income becomes 0 + 6 = 6.
# Now, neither Alice nor Bob can make any further moves, and the game ends.
# It is not possible for Alice to get a higher net income.
# Example 2:
#
#
# Input: edges = [[0,1]], bob = 1, amount = [-7280,2350]
# Output: -7280
# Explanation:
# Alice follows the path 0->1 whereas Bob follows the path 1->0.
# Thus, Alice opens the gate at node 0 only. Hence, her net income is -7280.
#
#
# Constraints:
#
# 2 <= n <= 105
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# edges represents a valid tree.
# 1 <= bob < n
# amount.length == n
# amount[i] is an even integer in the range [-104, 104].
# Solution
# C++ O(N) O(N) Depth-First-Search Breadth-First-Search Tree
class Solution {
public:
    bool makeBobMove(int source, int time, unordered_map<int, int>& bobPath, vector<bool>& seen, vector<vector<int>>& tree) {
        seen[source] = true;
        bobPath[source] = time;
        if (source == 0) return true;
        for (int& vertex : tree[source]) {
            if (!seen[vertex]) {
                if (makeBobMove(vertex, time + 1, bobPath, seen, tree)) return true;
            }
        }
        bobPath.erase(source);
        return false;
    }
    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        int n = amount.size();
        vector<vector<int>> tree (n, vector<int>());
        for (vector<int>& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            tree[x].push_back(y);
            tree[y].push_back(x);
        }
        vector<bool> seen (n, false);
        unordered_map<int, int> bobPath;
        makeBobMove(bob, 0, bobPath, seen, tree);
        seen = vector<bool>(n, false);
        int maxIncome = INT_MIN;
        deque<tuple<int, int, int>> path;
        path.push_back({0, 0, 0});
        while (!path.empty()) {
            auto [source, time, income] = path.front();
            path.pop_front();
            if (!bobPath.count(source) || bobPath[source] > time) {
                income += amount[source];
            } else if (bobPath[source] == time) {
                income += amount[source] / 2;
            }
            for (int& vertex : tree[source]) {
                if (!seen[vertex]) {
                    path.push_back({vertex, time + 1, income});
                }
            }
            if (tree[source].size() == 1 && source != 0) {
                maxIncome = max(maxIncome, income);
            }
            seen[source] = true;
        }
        return maxIncome;
    }
};

# Python O(N) O(N) Depth-First-Search Breadth-First-Search Tree
class Solution:
    def __init__(self) -> None:
        self.bob_path: dict[int, int] = dict()
        self.visited: list[bool] = []
        self.tree: list[list[int]] = []

    def mostProfitablePath(self, edges: list[list[int, int]], bob: int, amount: list[int]) -> int:
        n: int = len(amount)
        max_income: float = float("-inf")
        self.tree = [[] for _ in range(n)]
        self.bob_path = {}
        self.visited = [False] * n
        node_queue: deque[tuple[int, int, int]] = deque([(0, 0, 0)])
        for edge in edges:
            self.tree[edge[0]].append(edge[1])
            self.tree[edge[1]].append(edge[0])
        self.find_bob_path(bob, 0)
        self.visited = [False] * n
        while node_queue:
            source_node, time, income = node_queue.popleft()
            if (
                source_node not in self.bob_path
                or time < self.bob_path[source_node]
            ):
                income += amount[source_node]
            elif time == self.bob_path[source_node]:
                income += amount[source_node] // 2
            if len(self.tree[source_node]) == 1 and source_node != 0:
                max_income = max(max_income, income)
            for adjacent_node in self.tree[source_node]:
                if not self.visited[adjacent_node]:
                    node_queue.append((adjacent_node, time + 1, income))
            self.visited[source_node] = True
        return max_income

    def find_bob_path(self, source_node: int, time: int) -> bool:
        self.bob_path[source_node] = time
        self.visited[source_node] = True
        if source_node == 0: return True
        for adjacent_node in self.tree[source_node]:
            if not self.visited[adjacent_node]:
                if self.find_bob_path(adjacent_node, time + 1):
                    return True
        self.bob_path.pop(source_node, None)
        return False