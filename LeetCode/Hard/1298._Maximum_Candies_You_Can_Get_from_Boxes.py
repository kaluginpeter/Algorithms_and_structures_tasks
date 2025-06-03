# You have n boxes labeled from 0 to n - 1. You are given four arrays: status, candies, keys, and containedBoxes where:
#
# status[i] is 1 if the ith box is open and 0 if the ith box is closed,
# candies[i] is the number of candies in the ith box,
# keys[i] is a list of the labels of the boxes you can open after opening the ith box.
# containedBoxes[i] is a list of the boxes you found inside the ith box.
# You are given an integer array initialBoxes that contains the labels of the boxes you initially have. You can take all the candies in any open box and you can use the keys in it to open new boxes and you also can use the boxes you find in it.
#
# Return the maximum number of candies you can get following the rules above.
#
#
#
# Example 1:
#
# Input: status = [1,0,1,0], candies = [7,5,4,100], keys = [[],[],[1],[]], containedBoxes = [[1,2],[3],[],[]], initialBoxes = [0]
# Output: 16
# Explanation: You will be initially given box 0. You will find 7 candies in it and boxes 1 and 2.
# Box 1 is closed and you do not have a key for it so you will open box 2. You will find 4 candies and a key to box 1 in box 2.
# In box 1, you will find 5 candies and box 3 but you will not find a key to box 3 so box 3 will remain closed.
# Total number of candies collected = 7 + 4 + 5 = 16 candy.
# Example 2:
#
# Input: status = [1,0,0,0,0,0], candies = [1,1,1,1,1,1], keys = [[1,2,3,4,5],[],[],[],[],[]], containedBoxes = [[1,2,3,4,5],[],[],[],[],[]], initialBoxes = [0]
# Output: 6
# Explanation: You have initially box 0. Opening it you can find boxes 1,2,3,4 and 5 and their keys.
# The total number of candies will be 6.
#
#
# Constraints:
#
# n == status.length == candies.length == keys.length == containedBoxes.length
# 1 <= n <= 1000
# status[i] is either 0 or 1.
# 1 <= candies[i] <= 1000
# 0 <= keys[i].length <= n
# 0 <= keys[i][j] < n
# All values of keys[i] are unique.
# 0 <= containedBoxes[i].length <= n
# 0 <= containedBoxes[i][j] < n
# All values of containedBoxes[i] are unique.
# Each box is contained in one box at most.
# 0 <= initialBoxes.length <= n
# 0 <= initialBoxes[i] < n
# Solution
# Python O(N^2) O(N) Breadth-First-Search Greedy
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        n: int = len(candies)
        output: int = 0
        in_stock: list[int] = [0] * n
        have_key: list[int] = [0] * n
        candidates: list[int] = []
        for init_box in initialBoxes:
            in_stock[init_box] = 1
            candidates.append(init_box)
        for _ in range(n):
            discover_something: bool = False
            new_opens: list[int] = []
            i: int = 0
            while i < len(candidates):
                box: int = candidates[i]
                if in_stock[box] and (status[box] or have_key[box]):
                    discover_something = True
                    output += candies[box]
                    for new_box in containedBoxes[box]:
                        in_stock[new_box] = 1
                        new_opens.append(new_box)
                    for new_key in keys[box]: have_key[new_key] = 1
                    candidates[i], candidates[-1] = candidates[-1], candidates[i]
                    candidates.pop()
                else: i += 1
            if not discover_something: break
            for new_box in new_opens: candidates.append(new_box)
        return output

# C++ O(N^2) O(N) Breadth-First-Search Greedy
class Solution {
public:
    int maxCandies(vector<int>& status, vector<int>& candies, vector<vector<int>>& keys, vector<vector<int>>& containedBoxes, vector<int>& initialBoxes) {
        int n = candies.size(), output = 0;
        vector<int> inStock(n, 0), haveKey(n, 0), candidates;
        for (int &initBox : initialBoxes) {
            inStock[initBox] = 1;
            candidates.push_back(initBox);
        }
        for (int t = 0; t < n; ++t) {
            bool discoverSomething = false;
            int i = 0;
            vector<int> newOpens;
            while (i < candidates.size()) {
                int box = candidates[i];
                if (inStock[box] && (status[box] || haveKey[box])) {
                    discoverSomething = true;
                    output += candies[box];
                    for (int &newBox : containedBoxes[box]) {
                        newOpens.push_back(newBox);
                        inStock[newBox] = 1;
                    }
                    for (int &newKey : keys[box]) haveKey[newKey] = 1;
                    swap(candidates[i], candidates[candidates.size() - 1]);
                    candidates.pop_back();
                } else ++i;
            }
            if (!discoverSomething) break;
            for (int &box : newOpens) candidates.push_back(box);
        }
        return output;
    }
};
