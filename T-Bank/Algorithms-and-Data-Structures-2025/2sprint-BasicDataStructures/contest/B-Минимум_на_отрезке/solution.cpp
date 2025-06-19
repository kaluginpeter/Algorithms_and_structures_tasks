#include <iostream>
#include <vector>
#include <deque>


using namespace std;


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(K)
    */
    int n, k;
    scanf("%d %d", &n, &k);
    vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) cin >> nums[i];
    deque<int> dq;
    vector<int> output;
    for (int idx = 0; idx < n; ++idx) {
        if (!dq.empty() && idx - dq.front() + 1 > k) dq.pop_front();
        while (!dq.empty() && nums[dq.back()] > nums[idx]) dq.pop_back();
        dq.push_back(idx);
        if (idx + 1 >= k) output.push_back(nums[dq.front()]);
    }
    for (size_t i = 0; i < output.size(); ++i) {
        if (i) cout << " ";
        cout << output[i];
    }
    if (!output.empty()) cout << "\n";
}

 
int main() {
    solution();
}