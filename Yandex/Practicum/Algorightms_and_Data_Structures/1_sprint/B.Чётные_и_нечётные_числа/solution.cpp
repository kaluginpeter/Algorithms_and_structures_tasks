#include <iostream>
#include <cmath>

int main() {
    /*
    Time Complexity O(1)
    Memory Complexity O(1)
    */
    int a, b, c;
    std::cin >> a >> b >> c;
    int diff = std::abs(a % 2) + std::abs(b % 2) + std::abs(c % 2);
    std::cout << (diff == 0 || diff == 3? "WIN" : "FAIL") << std::endl;
}