#include <iostream>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <vector>
#include <queue>

using namespace std;

void solution() {
    /*
    Time Complexity O(|V| + |E|)
    Memory Complexity O(|V|)
    */
    int m;
    scanf("%d", &m);
    cin.ignore();
    unordered_map<string, vector<string>> adjList;
    for (int i = 0; i < m; ++i) {
        string convertation;
        getline(cin, convertation);
        int x = convertation.find(" -> ");
        string source = convertation.substr(0, x);
        string destination = convertation.substr(x + 4);
        adjList[destination].push_back(source);
    }
    string start, target;
    cin >> start >> target;
    unordered_set<string> seen;
    seen.insert(target);
    queue<pair<string, int>> q;
    q.push({target, 0});
    while (!q.empty()) {
        string vertex = q.front().first;
        int path = q.front().second;
        q.pop();
        if (vertex == start) {
            printf("%d\n", path);
            return;
        }
        for (string& neighbor : adjList[vertex]) {
            if (!seen.count(neighbor)) {
                seen.insert(neighbor);
                q.push({neighbor, path + 1});
            }
        }
    }
    printf("-1\n");
    
}


int main() {
    solution();
}