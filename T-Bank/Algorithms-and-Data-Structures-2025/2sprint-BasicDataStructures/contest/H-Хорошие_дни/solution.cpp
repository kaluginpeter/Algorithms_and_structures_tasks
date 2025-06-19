#include <iostream>
#include <vector>
#include <stack>

using namespace std;


void solution() {
    /*
    Time Complexity O(N)
    Memory Complexity O(N)
    */
    int n;
    scanf("%d", &n);
    vector<long long> prefixSum = {0};
    vector<int> nums;
    for (int i = 0; i < n; ++i) {
        int num;
        scanf("%d", &num);
        prefixSum.push_back(prefixSum.back() + num);
        nums.push_back(num);
    }
    stack<int> st;
    vector<pair<int, int>> segments;
    for (int idx = 0; idx < n; ++idx) {
        while (!st.empty() && nums[st.top()] >= nums[idx]) {
            segments[st.top()].second = idx;
            st.pop();
        }
        if (st.empty()) segments.push_back({-1, n});
        else segments.push_back({st.top(), n});
        st.push(idx);
    }
    long long answer = 0;
    for (int i = 0; i < n; ++i) {
        int left = segments[i].first + 1;
        int right = segments[i].second;
        long long part = (prefixSum[right] - prefixSum[left]) * nums[i];
        answer = max(answer, part);
    }
    printf("%lld\n", answer);
}


int main() {
    solution();
}