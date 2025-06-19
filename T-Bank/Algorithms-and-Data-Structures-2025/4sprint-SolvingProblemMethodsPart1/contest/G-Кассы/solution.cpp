#include <iostream>
#include <vector>


void solution() {
    /*
    Time Complexity O(N + M)
    Memory Complexity O(M)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> seconds (24 * 60 * 60, 0);
    for (int i = 0; i < n; ++i) {
        int sH, sM, sS, eH, eM, eS;
        std::scanf("%d %d %d %d %d %d", &sH, &sM, &sS, &eH, &eM, &eS);
        int start = 3600 * sH + 60 * sM + sS;
        int end = 3600 * eH + 60 * eM + eS;
        if (start == end) ++seconds[0];
        else if (start < end) {
            ++seconds[start];
            --seconds[end];
        } else {
            ++seconds[0];
            --seconds[end]; 
            ++seconds[start];
        }
    }
    int output = 0;
    int workers = 0;
    for (int second = 0; second < seconds.size(); ++second) {
        workers += seconds[second];
        if (workers == n) ++output;
    }
    std::printf("%d\n", output);
}


int main() {
    solution();
}