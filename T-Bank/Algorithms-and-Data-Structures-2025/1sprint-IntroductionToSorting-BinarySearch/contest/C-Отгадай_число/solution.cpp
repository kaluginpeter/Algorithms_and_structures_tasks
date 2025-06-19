#include <iostream>
#include <string>


void solution() {
    /*
    Time Complexity O(logN)
    Memory Complexity O(1)
    */
    int n;
    std::cin >> n;
    int left = 1;
    int right = n;
    while (left <= right) {
        int middle = left + (right - left) / 2;
        std::cout << middle << "\n";
        std::fflush(stdout);
        std::string sign;
        std::cin >> sign;
        if (sign == ">=") left = middle + 1;
        else right = middle - 1;
    }
    std::printf("! %d\n", right);
}


int main() {
    solution();
}