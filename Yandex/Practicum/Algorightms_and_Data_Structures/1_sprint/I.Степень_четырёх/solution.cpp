#include <iostream>


void solution(int n) {
    /*
    Time Complexity O(log4 N)
    Memory Complexity O(1)
    */
    int mod = 4;
    int curN = 1;
    int upperBound = 10001;
    bool isValid = false;
    while (curN < upperBound) {
        if (curN == n) {
            isValid = true;
            break;
        }
        curN *= 4;
    }
    std::cout << (isValid? "True" : "False") << "\n";
};


int main() {
    int n;
    std::cin >> n;
    solution(n);
}