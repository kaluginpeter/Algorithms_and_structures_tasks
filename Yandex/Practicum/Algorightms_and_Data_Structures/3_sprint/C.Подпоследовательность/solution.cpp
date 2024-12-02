#include <iostream>
#include <string>


void solution(std::string& x, std::string& y) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int xIdx = 0;
    int yIdx = 0;
    while (xIdx < x.size() && yIdx < y.size()) {
        if (x[xIdx] == y[yIdx]) {
            ++xIdx;
        }
        ++yIdx;
    }
    std::cout << (xIdx == x.size()? "True" : "False") << "\n";
}


int main() {
    std::string x;
    std::cin >> x;
    std::string y;
    std::cin >> y;
    solution(x, y);
}