#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;


vector<long long> dijkstra(int start, const vector<vector<pair<int, int>>> &adj, int n) {
    vector<long long> dist(n + 1, LLONG_MAX);
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
    dist[start] = 0;
    pq.push({0, start});

    while (!pq.empty()) {
        long long current_dist = pq.top().first;
        int u = pq.top().second;
        pq.pop();

        if (current_dist > dist[u]) continue;

        for (const auto &edge : adj[u]) {
            int v = edge.first;
            int w = edge.second;
            if (dist[v] > dist[u] + w) {
                dist[v] = dist[u] + w;
                pq.push({dist[v], v});
            }
        }
    }
    return dist;
}

void solution() {
    /*
    Time Complexity O(VlogE)
    Memory Complexity O(V + E)
    */
    int n, m;
    scanf("%d %d", &n, &m);
    vector<vector<pair<int, int>>> adj(n + 1);

    for (int i = 0; i < m; ++i) {
        int u, v, w;
        scanf("%d %d %d", &u, &v, &w);
        adj[u].emplace_back(v, w);
        adj[v].emplace_back(u, w);
    }

    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    vector<long long> dist_a = dijkstra(a, adj, n);
    vector<long long> dist_b = dijkstra(b, adj, n);
    vector<long long> dist_c = dijkstra(c, adj, n);

    if (dist_a[b] == LLONG_MAX || dist_a[c] == LLONG_MAX || 
        dist_b[c] == LLONG_MAX) {
        printf("-1\n");
        return;
    }

    long long min_time = LLONG_MAX;
    
    if (dist_a[b] != LLONG_MAX && dist_b[c] != LLONG_MAX)
        min_time = min(min_time, dist_a[b] + dist_b[c]);
    
    if (dist_a[c] != LLONG_MAX && dist_c[b] != LLONG_MAX)
        min_time = min(min_time, dist_a[c] + dist_c[b]);
    
    if (dist_b[a] != LLONG_MAX && dist_a[c] != LLONG_MAX)
        min_time = min(min_time, dist_b[a] + dist_a[c]);
    
    if (dist_b[c] != LLONG_MAX && dist_c[a] != LLONG_MAX)
        min_time = min(min_time, dist_b[c] + dist_c[a]);
    
    if (dist_c[a] != LLONG_MAX && dist_a[b] != LLONG_MAX)
        min_time = min(min_time, dist_c[a] + dist_a[b]);
    
    if (dist_c[b] != LLONG_MAX && dist_b[a] != LLONG_MAX)
        min_time = min(min_time, dist_c[b] + dist_b[a]);

    if (min_time == LLONG_MAX) printf("-1\n");
    else printf("%lld\n", min_time);
}

int main() {
    solution();
    return 0;
}