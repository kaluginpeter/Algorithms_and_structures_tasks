#include <iostream>

void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int n;
    std::scanf("%d", &n);
    if (n == 0 || n == 1) {
        std::printf("1\n");
        return;
    }
    int count2 = 0, count5 = 0;
    int output = 1;
    for (int i = 2; i <= n; ++i) {
        int num = i;
        while (num % 2 == 0) {
            num /= 2;
            ++count2;
        }
        while (num % 5 == 0) {
            num /= 5;
            ++count5;
        }
        output = (output * num) % 10;
    }
    int extra2s = count2 - count5;
    for (int i = 0; i < extra2s; ++i) output = (output * 2) % 10;
    std::printf("%d\n", output);
}

int main() {
    solution();
}