#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(V^2)
    Memory Complexity O(V^2)
    */
    int v, e;
    std::cin >> v >> e;
    std::vector<std::vector<int>> adjMatrix (v + 1, std::vector<int>(v + 1, 0));
    for (int i = 0; i < e; ++i) {
        int source, destination;
        std::cin >> source >> destination;
        adjMatrix[source][destination] = 1;
    }
    for (int source = 1; source <= v; ++source) {
        for (int destination = 1; destination <= v; ++destination) {
            if (destination > 1) std::cout << " ";
            std::cout << adjMatrix[source][destination];
        }
        std::cout << "\n";
    }
}


int main() {
    solution();
}