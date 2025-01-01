#include <iostream>
#include <vector>
#include <cstdint>
#include <algorithm>

void solution() {
    /*
    Time Complexity O(log(min(A, B)))
    Memory Complexity O(1)
    */
    int n, m;
    std::cin >> n >> m;

    std::vector<int> A(n);
    std::vector<int> B(m);

    for (int i = 0; i < n; ++i) {
        std::cin >> A[i];
    }
    for (int i = 0; i < m; ++i) {
        std::cin >> B[i];
    }
    if (n > m) {
        std::swap(A, B);
        std::swap(n, m);
    }

    int left = 0, right = n, half = (n + m + 1) / 2;

    while (left <= right) {
        int middle = left + (right - left) / 2;
        int second_middle = half - middle;

        int Aleft = (middle > 0) ? A[middle - 1] : INT32_MIN;
        int Aright = (middle < n) ? A[middle] : INT32_MAX;

        int Bleft = (second_middle > 0) ? B[second_middle - 1] : INT32_MIN;
        int Bright = (second_middle < m) ? B[second_middle] : INT32_MAX;

        if (Aleft <= Bright && Bleft <= Aright) {
            if ((n + m) % 2 == 0) {
                std::cout << (std::max(Aleft, Bleft) + std::min(Aright, Bright)) / 2.0 << "\n";
            } else {
                std::cout << std::max(Aleft, Bleft) << "\n";
            }
            return;
        } else if (Aleft > Bright) {
            right = middle - 1;
        } else {
            left = middle + 1;
        }
    }
}

int main() {
    solution();
}