#include <iostream>
#include <vector>



long long mergeAndCount(std::vector<int>& nums, std::vector<int>& tempArr, int& left, int& middle, int& right) {
    long long invCount = 0;
    int l = left;
    int r = middle + 1;
    int k = left;
    while (l <= middle && r <= right) {
        if (nums[l] < nums[r]) {
            tempArr[k] = nums[l];
            ++l;
        } else {
            tempArr[k] = nums[r];
            invCount += (middle - l + 1);
            ++r;
        }
        ++k;
    }
    while (l <= middle) {
        tempArr[k] = nums[l];
        ++l;
        ++k;
    }
    while (r <= right) {
        tempArr[k] = nums[r];
        ++r;
        ++k;
    }
    for (int i = left; i < right + 1; ++i) nums[i] = tempArr[i];
    return invCount;
}



long long mergeSortAndCount(std::vector<int>& nums, std::vector<int>& tempArr, int left, int right) {
    long long invCount = 0;
    if (left < right) {
        int middle = left + (right - left) / 2;
        invCount += mergeSortAndCount(nums, tempArr, left, middle);
        invCount += mergeSortAndCount(nums, tempArr, middle + 1, right);
        invCount += mergeAndCount(nums, tempArr, left, middle, right);
    }
    return invCount;
}



void solution() {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(N + logN)
    */
    int n;
    std::scanf("%d", &n);
    std::vector<int> nums (n, 0);
    for (int i = 0; i < n; ++i) std::cin >> nums[i];
    std::vector<int> tempArr (n, 0);
    long long invCount = mergeSortAndCount(nums, tempArr, 0, n - 1);
    std::cout << invCount << "\n";
    for (int i = 0; i < n; ++i) {
        if (i) std::cout << " ";
        std::cout << nums[i];
    }
    std::cout << "\n";
}


int main() {
    solution();
}