/*
You are given a 0-indexed integer array nums.

The distinct count of a subarray of nums is defined as:

Let nums[i..j] be a subarray of nums consisting of all the indices from i to j such that 0 <= i <= j < nums.length. Then the number of distinct values in nums[i..j] is called the distinct count of nums[i..j].
Return the sum of the squares of distinct counts of all subarrays of nums.

Since the answer may be very large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [1,2,1]
Output: 15
Explanation: Six possible subarrays are:
[1]: 1 distinct value
[2]: 1 distinct value
[1]: 1 distinct value
[1,2]: 2 distinct values
[2,1]: 2 distinct values
[1,2,1]: 2 distinct values
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 + 22 + 22 + 22 = 15.
Example 2:

Input: nums = [2,2]
Output: 3
Explanation: Three possible subarrays are:
[2]: 1 distinct value
[2]: 1 distinct value
[2,2]: 1 distinct value
The sum of the squares of the distinct counts in all subarrays is equal to 12 + 12 + 12 = 3.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
*/
// Solution
// C++ O(NlogN) O(N) BIT
class BIT {
public:
    int size;
    vector<long long> _tree1;
    vector<long long> _tree2;

    BIT(int n) {
        size = n;
        _tree1.assign(n + 2, 0);
        _tree2.assign(n + 2, 0);
    }

    int _lowbit(int index) { return index & -index; }

    void add(int left, int right, int delta) {
        _add(left, delta);
        _add(right + 1, -delta);
    }

    long long query(int left, int right) {
        return _query(right) - _query(left - 1);
    }

private:
    void _add(int index, int delta) {
        index += 1;
        long long rawIndex = index;
        while (index <= size) {
            _tree1[index] += delta;
            _tree2[index] += rawIndex * delta;
            index += _lowbit(index);
        }
    }

    long long _query(int index) {
        index += 1;
        long long rawIndex = index + 1;
        if (index > size) {
            index = size;
        }
        long long res = 0;
        while (index > 0) {
            res += rawIndex * _tree1[index] - _tree2[index];
            index -= _lowbit(index);
        }
        return res;
    }
};

class Solution {
public:
    int sumCounts(vector<int>& A) {
        int n = A.size();
        long long res = 0, cur = 0;
        BIT bit(n + 10);
        unordered_map<int, int> seen;
        long long mod = 1e9 + 7;
        for (int i = 0; i < n; i++) {
            int a = A[i];
            int j = (seen.count(a) ? seen[a] : -1) + 1;
            long long q = bit.query(j, i);
            cur = (cur + q * 2 + i - j + 1) % mod;
            res = (res + cur) % mod;
            bit.add(j, i, 1);
            seen[a] = i;
        }
        return res;
    }
};