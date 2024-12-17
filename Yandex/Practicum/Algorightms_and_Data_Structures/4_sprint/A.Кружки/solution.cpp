#include <iostream>
#include <unordered_set>
#include <string>


void solution(int& t) {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    std::unordered_set<std::string> hashset;
    for (int i = 0; i < t; ++i) {
        std::string activity;
        std::getline(std::cin, activity);
        if (!hashset.count(activity)) {
            std::cout << activity << "\n";
            hashset.insert(activity);
        }
    }
}


int main() {
    int t;
    std::cin >> t;
    std::cin.ignore();
    solution(t);
}