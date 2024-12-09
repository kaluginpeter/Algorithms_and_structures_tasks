#include <iostream>
#include <vector>


void solution(int& n, std::vector<int>& nums) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int blocks = 0;
    int start = 0;
    int threshold = 0;
    for (int idx = 0; idx < n; ++idx) {
        if (nums[idx] > idx) {
            threshold = std::max(threshold, nums[idx]);
        }
        if (idx >= threshold) {
            ++blocks;
            threshold = 0;
        }
    }
    std::cout << blocks << "\n";
}


int main() {
    int n;
    std::cin >> n;
    std::vector<int> nums;
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        nums.push_back(num);
    }
    solution(n, nums);
}
