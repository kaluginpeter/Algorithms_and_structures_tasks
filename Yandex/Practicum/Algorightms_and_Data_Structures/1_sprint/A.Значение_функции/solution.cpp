#include <iostream>
#include <cmath>


int main() {
    /*
    Time Complexity O(1)
    Memory Complexity O(1)
    */
    int a, x, b, c;
    std::cin >> a >> x >> b >> c;
    int result = a * std::pow(x, 2) + b * x + c;
    std::cout << result << std::endl;
}