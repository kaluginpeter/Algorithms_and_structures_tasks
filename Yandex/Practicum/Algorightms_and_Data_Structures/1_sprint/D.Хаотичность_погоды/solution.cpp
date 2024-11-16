#include <iostream>
#include <vector>


void solution(int n, std::vector<int>& nums) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int output = 0;
    for (int index = 0; index < n; ++index) {
        if (
        (!index || nums[index - 1] < nums[index])
        && (index + 1 == n || nums[index] > nums[index + 1])
        ) {
            ++output;
        }
    }
    std::cout << output << "\n";
};


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