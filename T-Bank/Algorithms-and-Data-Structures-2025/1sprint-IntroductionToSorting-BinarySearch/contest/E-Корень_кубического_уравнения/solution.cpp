#include <iostream>
#include <cmath>
#include <iomanip>


double f(double& x, int& a, int& b, int&c, int& d) {
    return a  * std::pow(x, 3) + b * std::pow(x, 2) + c * x + d;
}


void solution() {
    /*
    Time Complexity O(log(10^8))
    Memory Complexity O(1)
    */
    int a, b, c, d;
    std::scanf("%d %d %d %d", &a, &b, &c, &d);
    double left = -100000000;
    double right = 100000000;
    double eplison = 0.00001;
    while (right - left > eplison) {
        double middle = left + (right - left) / 2.0;
        if (f(middle, a, b, c, d) == 0) {
            left = middle;
            right = middle;
            break;
        } else if (f(left, a, b, c, d) * f(middle, a, b, c, d) < 0) right = middle;
        else left = middle;
    }
    std::setprecision(5);
    std::cout << left + (right - left) / 2.0 << "\n";
}


int main() {
    solution();
}