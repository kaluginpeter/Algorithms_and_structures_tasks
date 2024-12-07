#include <iostream>
#include <vector>


void solution(int n, std::vector<int>& nums) {
    /*
    Time Complexity O(N)
    Memory Complexity O(1)
    */
    int zerosIdx = 0;
    int onesIdx = 0;
    int twosIdx = n - 1;
    while (onesIdx <= twosIdx) {
        if (nums[onesIdx] == 0) {
            int zerosValue = nums[zerosIdx];
            nums[zerosIdx] = nums[onesIdx];
            nums[onesIdx] = zerosValue;
            if (zerosIdx == onesIdx) {
                ++onesIdx;
            }
            ++zerosIdx;
        } else if (nums[onesIdx] == 2) {
            int twosValue = nums[twosIdx];
            nums[twosIdx] = nums[onesIdx];
            nums[onesIdx] = twosValue;
            --twosIdx;
        } else {
            ++onesIdx;
        }
    }

    for (int idx = 0; idx < n; ++idx) {
        if (idx) {
            std::cout << " ";
        }
        std::cout << nums[idx];
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