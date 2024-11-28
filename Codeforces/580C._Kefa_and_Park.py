# C. Kefa and Park
# time limit per test2 seconds
# memory limit per test256 megabytes
# Kefa decided to celebrate his first big salary by going to the restaurant.
#
# He lives by an unusual park. The park is a rooted tree consisting of n vertices with the root at vertex 1. Vertex 1 also contains Kefa's house. Unfortunaely for our hero, the park also contains cats. Kefa has already found out what are the vertices with cats in them.
#
# The leaf vertices of the park contain restaurants. Kefa wants to choose a restaurant where he will go, but unfortunately he is very afraid of cats, so there is no way he will go to the restaurant if the path from the restaurant to his house contains more than m consecutive vertices with cats.
#
# Your task is to help Kefa count the number of restaurants where he can go.
#
# Input
# The first line contains two integers, n and m (2 ≤ n ≤ 105, 1 ≤ m ≤ n) — the number of vertices of the tree and the maximum number of consecutive vertices with cats that is still ok for Kefa.
#
# The second line contains n integers a1, a2, ..., an, where each ai either equals to 0 (then vertex i has no cat), or equals to 1 (then vertex i has a cat).
#
# Next n - 1 lines contains the edges of the tree in the format "xi yi" (without the quotes) (1 ≤ xi, yi ≤ n, xi ≠ yi), where xi and yi are the vertices of the tree, connected by an edge.
#
# It is guaranteed that the given set of edges specifies a tree.
#
# Output
# A single integer — the number of distinct leaves of a tree the path to which from Kefa's home contains at most m consecutive vertices with cats.
#
# Examples
# InputCopy
# 4 1
# 1 1 0 0
# 1 2
# 1 3
# 1 4
# OutputCopy
# 2
# InputCopy
# 7 1
# 1 0 1 1 0 0 0
# 1 2
# 1 3
# 2 4
# 2 5
# 3 6
# 3 7
# OutputCopy
# 2
# Note
# Let us remind you that a tree is a connected graph on n vertices and n - 1 edge. A rooted tree is a tree with a special vertex called root. In a rooted tree among any two vertices connected by an edge, one vertex is a parent (the one closer to the root), and the other one is a child. A vertex is called a leaf, if it has no children.
#
# Note to the first sample test:The vertices containing cats are marked red. The restaurants are at vertices 2, 3, 4. Kefa can't go only to the restaurant located at vertex 2.
#
# Note to the second sample test:The restaurants are located at vertices 4, 5, 6, 7. Kefa can't go to restaurants 6, 7.
# Solution
# C++ O(N) O(N) DFS
#include <iostream>
#include <unordered_map>
#include <vector>

using namespace std;

void dfs(int node, int consecutiveCats, int m, const vector<int>& cats, const unordered_map<int, vector<int>>& adjList, int& count, vector<bool>& visited) {
    visited[node] = true;
    if (cats[node] == 1) {
        consecutiveCats++;
    } else {
        consecutiveCats = 0;
    }
    if (consecutiveCats > m) {
        return;
    }

    bool isLeaf = true;
    for (int neighbor : adjList.at(node)) {
        if (!visited[neighbor]) {
            isLeaf = false;
            dfs(neighbor, consecutiveCats, m, cats, adjList, count, visited);
        }
    }
    if (isLeaf) {
        count++;
    }
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> cats(n + 1);
    for (int i = 1; i <= n; ++i) {
        cin >> cats[i];
    }

    unordered_map<int, vector<int>> adjList;
    for (int i = 0; i < n - 1; ++i) {
        int x, y;
        cin >> x >> y;
        adjList[x].push_back(y);
        adjList[y].push_back(x);
    }

    int count = 0;
    vector<bool> visited(n + 1, false);

    dfs(1, 0, m, cats, adjList, count, visited);

    cout << count << "\n";
    return 0;
}

# Python O(N) O(N) DFS
import sys


def solution(n: int, m: int) -> None:
    cats = list(map(int, sys.stdin.readline().rstrip().split()))
    cats = [0] + cats
    adj_list = {i: [] for i in range(1, n + 1)}

    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        adj_list[x].append(y)
        adj_list[y].append(x)

    visited = [False] * (n + 1)
    count = 0
    stack = [(1, 0)]
    while stack:
        root, cat = stack.pop()
        if visited[root]:
            continue
        visited[root] = True

        if cats[root]:
            cat += 1
        else:
            cat = 0

        if cat > m:
            continue

        is_leaf = True
        for neighbor in adj_list[root]:
            if not visited[neighbor]:
                is_leaf = False
                stack.append((neighbor, cat))

        if is_leaf:
            count += 1

    sys.stdout.write(str(count) + '\n')


if __name__ == '__main__':
    n, m = map(int, sys.stdin.readline().rstrip().split())
    solution(n, m)

