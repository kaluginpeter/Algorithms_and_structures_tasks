#include <iostream>
#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>


void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N)
    */
    int n;
    std::cin >> n;
    std::vector<std::string> words(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> words[i];
    }
    std::unordered_map<std::string, std::vector<int>> hashmap;
    for (int idx = 0; idx < n; ++idx) {
        std::sort(words[idx].begin(), words[idx].end());
        hashmap[words[idx]].push_back(idx);
    }
    std::vector<std::vector<int>> groups;
    for (auto& pair : hashmap) {
        groups.push_back(pair.second);
    }
    std::sort(groups.begin(), groups.end());
    for (int rowIdx = 0; rowIdx < groups.size(); ++rowIdx) {
        if (rowIdx) {
            std::cout << "\n";
        }
        for (int colIdx = 0; colIdx < groups[rowIdx].size(); ++colIdx) {
            if (colIdx) {
                std::cout << " ";
            }
            std::cout << groups[rowIdx][colIdx];
        }
    }
}

int main() {
    solution();
}