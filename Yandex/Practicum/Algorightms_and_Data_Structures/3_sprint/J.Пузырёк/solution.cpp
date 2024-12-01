#include <iostream>
#include <vector>


void solution(int& n, std::vector<int>& nums) {
    /*
    Time Complexity O(N**2)
    Memory Complexity O(1)
    */
    bool alreadySorted = true;
    bool hasChange = false;
    for (int i = n - 1; i >= 0; --i) {
        hasChange = false;
        for (int j = 0; j < i; ++j) {
            if (nums[j] > nums[j + 1]) {
                alreadySorted = false;
                hasChange = true;
                int prevJ = nums[j];
                nums[j] = nums[j + 1];
                nums[j + 1] = prevJ;
            }
        }
        if (hasChange) {
            for (int k = 0; k < n; ++k) {
                if (k) {
                    std::cout << " ";
                }
                std::cout << nums[k];
            }
            std::cout << "\n";
        }
    }
    if (alreadySorted) {
        for (int i = 0; i < n; ++i) {
            if (i) {
                std::cout << " ";
            }
            std::cout << nums[i];
        }
        std::cout << "\n";
    }
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