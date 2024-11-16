#include <iostream>
#include <vector>


void solution(long long num) {
    /*
    Time Complexity O(sqrt(N)log(sqrt(N)))
    Memory Complexity O(sqrt(N))
    */
    std::vector<long long> output;
    while (num % 2 == 0) {
        output.push_back(2);
        num /= 2;
    }
    for (long long mod = 3; mod * mod <= num; mod += 2) {
        while (num % mod == 0) {
            output.push_back(mod);
            num /= mod;
        }
    }
    if (num > 2) {
        output.push_back(num);
    }
    int n = output.size();
    for (int index = 0; index < n; ++index) {
        if (index) {
            std::cout << " ";
        }
        std::cout << output[index];
    }
    std::cout << "\n";
}


int main() {
    long long num;
    std::cin >> num;
    solution(num);
}