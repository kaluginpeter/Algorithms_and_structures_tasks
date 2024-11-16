#include <iostream>
#include <vector>

void solution(int num) {
    /*
    Time Complexity O(N), where N is length of place values
    Memory Complexity O(N), where N is length of place values
    */
    if (!num) {
        std::cout << "0\n";
        return;
    }
    int base = 2;
    std::vector<int> digits;
    while (num) {
        digits.push_back(num % base);
        num /= base;
    }
    int n = digits.size();
    for (int index = n - 1; index >= 0; --index) {
        std::cout << digits[index];
    }
    std::cout << "\n";
};


int main() {
    int num;
    std::cin >> num;
    solution(num);
}