#include <iostream>
#include <vector>

using namespace std;


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    vector<pair<int, int>> stack;
    int deletions = 0;
    for (int i = 0; i < n; ++i) {
        int num;
        cin >> num;
        if (stack.empty() || stack.back().first != num) {
            if (!stack.empty() && stack.back().second > 2) {
                deletions += stack.back().second;
                stack.pop_back();
                if (!stack.empty() && stack.back().first == num) {
                    ++stack.back().second;
                } else stack.push_back({num, 1});
            } else stack.push_back({num, 1});
        } else ++stack.back().second;
    }
    if (!stack.empty() && stack.back().second > 2) {
        deletions += stack.back().second;
    }
    printf("%d\n", deletions);
}

 
int main() {
    solution();
}