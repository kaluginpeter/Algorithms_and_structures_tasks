#include <iostream>
#include <vector>


void solution(int xLength, std::vector<int>& x, int k) {
    /*
    Time Complexity O(N), where N is the length of the largest number
    Memory Complexity O(N), where N is the length of the largest number
    */
    std::vector<int> output;
    int addition = 0;
    for (int index = xLength - 1; index >= 0; --index) {
        int sumDigits = x[index] + k % 10 + addition;
        addition = sumDigits / 10;
        k /= 10;
        output.push_back(sumDigits % 10);
    }
    while (k) {
        int sumDigits = k % 10 + addition;
        k /= 10;
        addition = sumDigits / 10;
        output.push_back(sumDigits % 10);
    }
    if (addition) {
        output.push_back(addition);
    }
    int n = output.size();
    for (int index = n - 1; index >= 0; --index) {
        std::cout << output[index];
        if (index) {
            std::cout << " ";
        }
    }
    std::cout << "\n";
}


int main() {
    int xLength;
    std::cin >> xLength;
    std::vector<int> x;
    for (int i = 0; i < xLength; ++i) {
        int digit;
        std::cin >> digit;
        x.push_back(digit);
    }
    int k;
    std::cin >> k;
    solution(xLength, x, k);
}