# There is a directed weighted graph that consists of n nodes numbered from 0 to n - 1. The edges of the graph are initially represented by the given array edges where edges[i] = [fromi, toi, edgeCosti] meaning that there is an edge from fromi to toi with the cost edgeCosti.
#
# Implement the Graph class:
#
# Graph(int n, int[][] edges) initializes the object with n nodes and the given edges.
# addEdge(int[] edge) adds an edge to the list of edges where edge = [from, to, edgeCost]. It is guaranteed that there is no edge between the two nodes before adding this one.
# int shortestPath(int node1, int node2) returns the minimum cost of a path from node1 to node2. If no path exists, return -1. The cost of a path is the sum of the costs of the edges in the path.
#
#
# Example 1:
#
#
# Input
# ["Graph", "shortestPath", "shortestPath", "addEdge", "shortestPath"]
# [[4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]], [3, 2], [0, 3], [[1, 3, 4]], [0, 3]]
# Output
# [null, 6, -1, null, 6]
#
# Explanation
# Graph g = new Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]]);
# g.shortestPath(3, 2); // return 6. The shortest path from 3 to 2 in the first diagram above is 3 -> 0 -> 1 -> 2 with a total cost of 3 + 2 + 1 = 6.
# g.shortestPath(0, 3); // return -1. There is no path from 0 to 3.
# g.addEdge([1, 3, 4]); // We add an edge from node 1 to node 3, and we get the second diagram above.
# g.shortestPath(0, 3); // return 6. The shortest path from 0 to 3 now is 0 -> 1 -> 3 with a total cost of 2 + 4 = 6.
#
#
# Constraints:
#
# 1 <= n <= 100
# 0 <= edges.length <= n * (n - 1)
# edges[i].length == edge.length == 3
# 0 <= fromi, toi, from, to, node1, node2 <= n - 1
# 1 <= edgeCosti, edgeCost <= 106
# There are no repeated edges and no self-loops in the graph at any point.
# At most 100 calls will be made for addEdge.
# At most 100 calls will be made for shortestPath.
# Solution
# Python O(N + M + (ElogV)) O(ElogV) Dijkstra Shortest Path Design
class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.adj_list: dict[int, list[tuple[int, int]]] = dict()
        for edge in edges:
            start, end, weight = edge
            if start not in self.adj_list:
                self.adj_list[start] = list()
            self.adj_list[start].append((weight, end))
        self.n: int = n

    def addEdge(self, edge: List[int]) -> None:
        start, end, weight = edge
        if start not in self.adj_list:
            self.adj_list[start] = list()
        self.adj_list[start].append((weight, end))

    def shortestPath(self, node1: int, node2: int) -> int:
        return self.dijkstra(node1, node2)

    def dijkstra(self, source: int, target: int) -> int:
        min_heap: list[tuple[int, int]] = []
        visited: set[int] = set()
        heapq.heappush(min_heap, (0, source))
        while min_heap:
            cur_score, cur_vertex = heapq.heappop(min_heap)
            if cur_vertex == target:
                return cur_score
            if cur_vertex in visited:
                continue
            visited.add(cur_vertex)
            for edge in self.adj_list.get(cur_vertex, []):
                weight, neighbor = edge
                if edge not in visited:
                    heapq.heappush(min_heap, (cur_score + weight, neighbor))
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)

# C++ O(N + M + (ElogV)) O(ElogN) Dijkstra Shortest Path Design
class Graph {
private:
    std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
    int n = 0;
public:
    Graph(int n, vector<vector<int>>& edges) {
        this->n = n;
        for (std::vector<int>& edge : edges) {
            int start = edge[0];
            int end = edge[1];
            int weight = edge[2];
            adjList[start].push_back({weight, end});
        }
    };

    void addEdge(vector<int> edge) {
        int start = edge[0];
        int end = edge[1];
        int weight = edge[2];
        adjList[start].push_back({weight, end});
    }

    int shortestPath(int node1, int node2) {
        return dijkstra(node1, node2);
    }

    int dijkstra(int source, int target) {
        std::unordered_set<int> visited;
        std::priority_queue<std::pair<int, int>, std::vector<std::pair<int, int>>, std::greater<std::pair<int, int>>> minHeap;
        minHeap.push({0, source});
        while (minHeap.size()) {
            int curScore = minHeap.top().first;
            int curVertex = minHeap.top().second;
            minHeap.pop();
            if (curVertex == target) {
                return curScore;
            }
            if (visited.count(curVertex)) {
                continue;
            }
            visited.insert(curVertex);
            for (std::pair<int, int> edge : adjList[curVertex]) {
                int weight = edge.first;
                int neighbor = edge.second;
                if (!visited.count(neighbor)) {
                    minHeap.push({curScore + weight, neighbor});
                }
            }
        }
        return -1;
    }
};

/**
 * Your Graph object will be instantiated and called as such:
 * Graph* obj = new Graph(n, edges);
 * obj->addEdge(edge);
 * int param_2 = obj->shortestPath(node1,node2);
 */
