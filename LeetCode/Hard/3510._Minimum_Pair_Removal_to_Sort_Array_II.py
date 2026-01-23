# Given an array nums, you can perform the following operation any number of times:
#
# Select the adjacent pair with the minimum sum in nums. If multiple such pairs exist, choose the leftmost one.
# Replace the pair with their sum.
# Return the minimum number of operations needed to make the array non-decreasing.
#
# An array is said to be non-decreasing if each element is greater than or equal to its previous element (if it exists).
#
#
#
# Example 1:
#
# Input: nums = [5,2,3,1]
#
# Output: 2
#
# Explanation:
#
# The pair (3,1) has the minimum sum of 4. After replacement, nums = [5,2,4].
# The pair (2,4) has the minimum sum of 6. After replacement, nums = [5,6].
# The array nums became non-decreasing in two operations.
#
# Example 2:
#
# Input: nums = [1,2,2]
#
# Output: 0
#
# Explanation:
#
# The array nums is already sorted.
#
#
#
# Constraints:
#
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# Solution
# C++ O(NlogN) O(N) PriorityQueue
class Solution {
public:
    int n;
    vector<bool> removed;
    vector<int>  _next;
    vector<int>  _prev;
    vector<long long> cval;
    priority_queue<
            pair<long long, int>,
            vector<pair<long long, int>>,
            greater<pair<long long, int>>
        > Q;
    int inversions;

    void init(vector<int> &v){
        n = (int)v.size();
        removed = vector<bool>(n, false);
        _prev.resize(n);
        _next.resize(n);
        cval.resize(n);
        inversions = 0;
        for(int i = 0; i < n; ++i){
            _prev[i] = i - 1;
            _next[i] = i + 1;
            cval[i]  = v[i];
        }

        for(int i = 0; i < n - 1; ++i){
            if(cval[i] > cval[i + 1]) ++inversions;
            Q.push({cval[i] + cval[i + 1], i});
        }
    }

    bool isSorted(){
        return inversions == 0;
    }

    int topElement(){
        while(!Q.empty()){
            int pos = Q.top().second;
            long long asum = Q.top().first;
            if(removed[pos] || _next[pos] == n ||
                cval[pos] + cval[_next[pos]] != asum){
                Q.pop();
            }
            else break;
        }
        if (Q.empty()) return -1;
        return Q.top().second;
    }
    void merge(int i){
        int j = _next[i];
        if(j == n) return;
        int x = _prev[i], y = _next[j];
        if(cval[i] > cval[j]) inversions --;
        if(x != -1 && cval[x] > cval[i]) inversions --;
        if(y !=  n && cval[j] > cval[y]) inversions --;
        if(x != -1 && cval[x] > cval[i] + cval[j]) inversions ++;
        if(y !=  n && cval[i] + cval[j] > cval[y]) inversions ++;
        cval[i] += cval[j];
        removed[j] = true;
        _next[i] = y;
        if (y !=  n) {
            _prev[y] = i;
            Q.push({cval[i] + cval[y], i});
        }
        if(x != -1) Q.push({cval[x] + cval[i], x});
    }
    int minimumPairRemoval(vector<int>& nums) {
        init(nums);
        int output = 0;
        while(!isSorted()){
            int i = topElement();
            merge(i);
            ++output;
        }
        return output;
    }
};