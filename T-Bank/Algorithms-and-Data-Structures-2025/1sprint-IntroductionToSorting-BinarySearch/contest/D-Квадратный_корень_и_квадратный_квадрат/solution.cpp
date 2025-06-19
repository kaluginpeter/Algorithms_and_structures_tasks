#include <iostream>
#include <cmath>
#include <iomanip>


void solution() {
    /*
    Time Complexity O(logN)
    Memory Complexity O(1)
    */
    double PRECISE = 0.000001;
    double c;
    std::cin >> c;
    double left = 0;
    double right = c;
    while (std::abs(left - right) > 0.0) {
        double middle = left + (right - left) / 2.0;
        double cPrime = std::pow(middle, 2) + std::sqrt(middle + 1.0);
        if (std::abs(cPrime - c) <= PRECISE) {
            std::cout << std::fixed << std::setprecision(6) << middle << "\n";
            return;
        } else if (cPrime > c) right = middle;
        else left = middle;
    }
}


int main() {
    solution();
}