#include <iostream>
#include <string>
#include <algorithm>


void solution(std::string& x, std::string& y) {
    /*
    Time Complexity O(XlogX + YlogY)
    Memory Complexity O(1)
    */
    std::sort(x.begin(), x.end());
    std::sort(y.begin(), y.end());
    int xLength = x.size(), yLength = y.size();
    int xIdx = 0, yIdx = 0;
    while (xIdx < xLength && yIdx < yLength) {
        if (x[xIdx] != y[yIdx]) {
            std::cout << y[yIdx] << "\n";
            return;
        }
        ++xIdx;
        ++yIdx;
    }
    std::cout << y[yIdx] << "\n";
}


int main() {
    std::string x, y;
    std::cin >> x >> y;
    solution(x, y);
}



#include <iostream>
#include <string>
#include <unordered_map>


void solution(std::string& x, std::string& y) {
    /*
    Time Complexity O(X + Y)
    Memory Complexity O({X} + {Y})
    */
    std::unordered_map<char, int> xHashmap, yHashmap;
    for (char letter : x) {
        ++xHashmap[letter];
    }
    for (char letter : y) {
        ++yHashmap[letter];
    }
    for (auto& pair : yHashmap) {
        if (pair.second != xHashmap[pair.first]) {
            std::cout << pair.first << "\n";
        }
    }
}


int main() {
    std::string x, y;
    std::cin >> x >> y;
    solution(x, y);
}