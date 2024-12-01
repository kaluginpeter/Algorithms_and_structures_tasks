#include <iostream>
#include <string>
#include <vector>
#include <algorithm>


bool comparator(const std::string &x, const std::string &y) {
    return (x + y) > (y + x);
}


void solution(int &n, std::vector<std::string>& nums) {
    /*
    Time Complexity O(NlogN)
    Memory Complexity O(1)
    */
    std::sort(nums.begin(), nums.end(), comparator);
    for (std::string& num : nums) {
        std::cout << num;
    }
    std::cout << "\n";
}

int main() {
    int n;
    std::cin >> n;
    std::vector<std::string> nums;
    for (int i = 0; i < n; ++i) {
        std::string num;
        std::cin >> num;
        nums.push_back(num);
    }
    solution(n, nums);
}