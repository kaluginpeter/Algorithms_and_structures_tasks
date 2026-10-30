/*
You are given an integer n representing the number of nodes in a directed weighted graph, numbered from 0 to n - 1. This is represented by a 2D integer array edges, where edges[i] = [ui, vi, wi] represents a directed edge from node ui to node vi with weight wi.

You are also given a string labels of length n, where labels[i] is the character assigned to node i, and an integer k.

Return the minimum total edge weight of a path from node 0 to node n - 1 such that the concatenation of the labels of the nodes along the path contains at most k consecutive identical characters. If no valid path exists, return -1.

 

Example 1:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 1

Output: 3

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

Use edges[2] = [0, 2, 3] to reach node 2 with a weight wi = 3.
The corresponding concatenation of labels is "ab", which satisfies at most k = 1 consecutive identical characters. Thus, the answer is 3.
Example 2:

Input: n = 3, edges = [[0,1,1],[1,2,1],[0,2,3]], labels = "aab", k = 2

Output: 2

Explanation:

The optimal valid path from node 0 to node 2 is as follows:

Use edges[0] = [0, 1, 1] to reach node 1 with weight wi = 1.
Use edges[1] = [1, 2, 1] to reach node 2 with weight wi = 1.
The corresponding concatenation of labels is "aab", which satisfies at most k = 2 consecutive identical characters. Thus, the answer is 2.
Example 3:

Input: n = 3, edges = [[0,1,1],[1,2,1]], labels = "aaa", k = 2

Output: -1

Explanation:

There is no valid path from node 0 to node 2 that satisfies at most k = 2 consecutive identical characters. Thus, the answer is -1.

 

Constraints:

1 <= n == labels.length <= 5 * 104
0 <= edges.length <= 5 * 104
edges[i] == [ui, vi, wi]
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 104
labels consists of lowercase English letters
1 <= k <= 50
*/
// Solution
// C++ O(VlogE) O(E) Dijkstra Graph
class Solution {
public:
    int shortestPath(int n, vector<vector<int>>& edges, string labels, int k) {
        std::unordered_map<int, std::vector<std::pair<int, int>>> adjList;
        for (std::vector<int>& edge : edges) {
            adjList[edge[0]].push_back({edge[1], edge[2]});
        }
        std::vector<std::vector<int>> costs(n, std::vector<int>(k + 1, INT32_MAX));
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> minHeap;
        minHeap.push({0, 0, 1}); // <cost, node, length>
        costs[0][1] = 0;
        while (!minHeap.empty()) {
            std::vector<int> state = minHeap.top();
            minHeap.pop();
            int cost = state[0], node = state[1],length = state[2];
            if (cost != costs[node][length]) continue;
            if (node == n - 1) return cost;
            for (auto [neighbor, weight] : adjList[node]) {
                int nextChar = labels[neighbor] - 'a';
                int newLength = labels[node] - 'a' == nextChar ? length + 1 : 1;
                if (newLength > k) continue;
                else if (cost + weight >= costs[neighbor][newLength]) continue;
                costs[neighbor][newLength] = cost + weight;
                minHeap.push({cost + weight, neighbor, newLength});
            }
        }
        return -1;
    }
};

// Go O(VlogE) O(E) Graph Dijkstra
import "container/heap"

type PQ [][3]int

func (pq PQ) Len() int { return len(pq) }
func (pq PQ) Less(i, j int) bool {
    if pq[i][0] != pq[j][0] { return pq[i][0] < pq[j][0] }
    return pq[i][1] < pq[j][1]
}
func (pq PQ) Swap(i, j int) { pq[i], pq[j] = pq[j], pq[i] }
func (pq *PQ) Push(x interface{}) {
    *pq = append(*pq, x.([3]int))
}
func (pq *PQ) Pop() interface{} {
    output := (*pq)[len(*pq) - 1]
    *pq = (*pq)[:len(*pq) - 1]
    return output
}


func shortestPath(n int, edges [][]int, labels string, k int) int {
    var adjList map[int][][2]int = map[int][][2]int{}
    for _, edge := range edges {
        var u, v, w int = edge[0], edge[1], edge[2]
        _, ok := adjList[u]; if !ok { adjList[u] = [][2]int{} }
        adjList[u] = append(adjList[u], [2]int{v, w})
    }
    var seen [][]int = make([][]int, n)
    for i := 0; i < n; i++ {
        seen[i] = make([]int, k + 1)
        for j := 0; j < k + 1; j++ { seen[i][j] = 1e9 }
    }
    seen[0][0] = 0
    var pq *PQ = &PQ{[3]int{0, 0, 1}} // {cost, node, length}
    heap.Init(pq)
    for pq.Len() > 0 {
        var tmp interface{} = heap.Pop(pq)
        var vertex [3]int = tmp.([3]int)
        if vertex[1] == n - 1 { return vertex[0] }
        if vertex[0] > seen[vertex[1]][vertex[2]] { continue }
        for _, edge := range adjList[vertex[1]] {
            var newLength int = vertex[2] + 1
            if labels[vertex[1]] != labels[edge[0]] { newLength = 1 }
            if newLength > k { continue }
            if vertex[0] + edge[1] >= seen[edge[0]][newLength] { continue }
            seen[edge[0]][newLength] = vertex[0] + edge[1]
            heap.Push(pq, [3]int{vertex[0] + edge[1], edge[0], newLength})
        }
    }
    return -1
}