/*
You are climbing a staircase with n + 1 steps, numbered from 0 to n.

You are also given a 1-indexed integer array costs of length n, where costs[i] is the cost of step i.

From step i, you can jump only to step i + 1, i + 2, or i + 3. The cost of jumping from step i to step j is defined as: costs[j] + (j - i)2

You start from step 0 with cost = 0.

Return the minimum total cost to reach step n.

 

Example 1:

Input: n = 4, costs = [1,2,3,4]

Output: 13

Explanation:

One optimal path is 0 → 1 → 2 → 4

Jump	Cost Calculation	Cost
0 → 1	costs[1] + (1 - 0)2 = 1 + 1	2
1 → 2	costs[2] + (2 - 1)2 = 2 + 1	3
2 → 4	costs[4] + (4 - 2)2 = 4 + 4	8
Thus, the minimum total cost is 2 + 3 + 8 = 13

Example 2:

Input: n = 4, costs = [5,1,6,2]

Output: 11

Explanation:

One optimal path is 0 → 2 → 4

Jump	Cost Calculation	Cost
0 → 2	costs[2] + (2 - 0)2 = 1 + 4	5
2 → 4	costs[4] + (4 - 2)2 = 2 + 4	6
Thus, the minimum total cost is 5 + 6 = 11

Example 3:

Input: n = 3, costs = [9,8,3]

Output: 12

Explanation:

The optimal path is 0 → 3 with total cost = costs[3] + (3 - 0)2 = 3 + 9 = 12

 

Constraints:

1 <= n == costs.length <= 105​​​​​​​
1 <= costs[i] <= 104
 

*/
// Solution
// C++ O(N) O(1) DP
class Solution {
public:
    int climbStairs(int n, vector<int>& costs) {
        int first = 0, second = 0, third = 0;
        for (int i = 1; i <= n; ++i) {
            int curStair = first + costs[i - 1] + 1;
            if (i >= 2) curStair = std::min(curStair, second + costs[i - 1] + 4);
            if (i >= 3) curStair = std::min(curStair, third + costs[i - 1] + 9);
            std::swap(third, second);
            std::swap(second, first);
            std::swap(first, curStair);
        }
        return first;
    }
};

// Go O(N) O(1) DP
func climbStairs(n int, costs []int) int {
    var first, second, third int = 0, 0, 0
    for i := 1; i <= n; i++ {
        var curStair int = first + costs[i - 1] + 1
        if i >= 2 {
            curStair = min(curStair, second + costs[i - 1] + 4)
        }
        if i >= 3 {
            curStair = min(curStair, third + costs[i - 1] + 9)
        }
        third = second
        second = first
        first = curStair
    }
    return first
}

// Python O(N) O(1) DP
class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        first = second = third = 0
        for i in range(1, n + 1):
            cur_stair: int = first + costs[i - 1] + 1
            if i >= 2: cur_stair = min(cur_stair, second + costs[i - 1] + 4)
            if i >= 3: cur_stair = min(cur_stair, third + costs[i - 1] + 9)
            third, second, first = second, first, cur_stair
        return first