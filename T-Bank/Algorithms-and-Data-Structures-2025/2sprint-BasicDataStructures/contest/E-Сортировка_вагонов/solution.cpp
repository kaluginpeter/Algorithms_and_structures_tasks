#include <iostream>
#include <vector>
#include <string>
#include <stack>

using namespace std;


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    vector<string> moves;
    stack<int> deadlock;
    int rightNumsIdx = 0;
    int leftNumsIdx = 0;
    int target = 1;
    while (target <= n) {
        while (rightNumsIdx < n && nums[rightNumsIdx] != target) ++rightNumsIdx;
        
        if (rightNumsIdx < n) {
            moves.push_back("1 " + to_string(rightNumsIdx - leftNumsIdx + 1));
            for (int idx = leftNumsIdx; idx <= rightNumsIdx; ++idx) {
                deadlock.push(nums[idx]);
            }
            ++rightNumsIdx;
            leftNumsIdx = rightNumsIdx;
        } else {
            printf("0\n");
            return;
        }
        
        int deadlockToSecondStation = 0;
        while (!deadlock.empty() && deadlock.top() == target) {
            ++deadlockToSecondStation;
            deadlock.pop();
            ++target;
        }
        if (deadlockToSecondStation) {
            moves.push_back("2 " + to_string(deadlockToSecondStation));
        }
    }
    printf("%d\n", moves.size());
    for (string& move : moves) printf("%s\n", move.c_str());
}


int main() {
    solution();
}