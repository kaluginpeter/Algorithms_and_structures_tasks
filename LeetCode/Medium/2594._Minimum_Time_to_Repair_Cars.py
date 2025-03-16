# You are given an integer array ranks representing the ranks of some mechanics. ranksi is the rank of the ith mechanic. A mechanic with a rank r can repair n cars in r * n2 minutes.
#
# You are also given an integer cars representing the total number of cars waiting in the garage to be repaired.
#
# Return the minimum time taken to repair all the cars.
#
# Note: All the mechanics can repair the cars simultaneously.
#
#
#
# Example 1:
#
# Input: ranks = [4,2,3,1], cars = 10
# Output: 16
# Explanation:
# - The first mechanic will repair two cars. The time required is 4 * 2 * 2 = 16 minutes.
# - The second mechanic will repair two cars. The time required is 2 * 2 * 2 = 8 minutes.
# - The third mechanic will repair two cars. The time required is 3 * 2 * 2 = 12 minutes.
# - The fourth mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
# Example 2:
#
# Input: ranks = [5,1,8], cars = 6
# Output: 16
# Explanation:
# - The first mechanic will repair one car. The time required is 5 * 1 * 1 = 5 minutes.
# - The second mechanic will repair four cars. The time required is 1 * 4 * 4 = 16 minutes.
# - The third mechanic will repair one car. The time required is 8 * 1 * 1 = 8 minutes.
# It can be proved that the cars cannot be repaired in less than 16 minutes.​​​​​
#
#
# Constraints:
#
# 1 <= ranks.length <= 105
# 1 <= ranks[i] <= 100
# 1 <= cars <= 106
# Solution
# Python O(NlogM) O(1) BinarySearch
class Solution:
    def check(self, ranks: list[int], cars: int, middle: int) -> bool:
        for rank in ranks:
            can_make: int = int((middle // rank)**.5)
            cars -= can_make
        return cars <= 0

    def repairCars(self, ranks: List[int], cars: int) -> int:
        answer: int = 0
        left: int = 0
        right: int = 10**14
        while left <= right:
            middle: int = left + ((right - left) >> 1)
            if self.check(ranks, cars, middle):
                answer = middle
                right = middle - 1
            else: left = middle + 1
        return answer

# C++ O(NlogM) O(1) BinarySearch
class Solution {
public:
    bool check(vector<int>& ranks, int& cars, long long middle) {
        long long maked = static_cast<long long>(cars);
        for (int& rank : ranks) {
            long long canMake = (long long)sqrt((double)(middle / rank));
            maked -= canMake;
        }
        return maked <= 0;
    }

    long long repairCars(vector<int>& ranks, int cars) {
        long long left = 0;
        long long right = 100000000000000; // 10^14
        long long answer = 0;
        while (left <= right) {
            long long middle = left + ((right - left) >> 1);
            if (check(ranks, cars, middle)) {
                answer = middle;
                right = middle - 1;
            } else left = middle + 1;
        }
        return answer;
    }
};