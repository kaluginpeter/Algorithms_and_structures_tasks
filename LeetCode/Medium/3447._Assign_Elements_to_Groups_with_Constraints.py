# You are given an integer array groups, where groups[i] represents the size of the ith group. You are also given an integer array elements.
#
# Your task is to assign one element to each group based on the following rules:
#
# An element j can be assigned to a group i if groups[i] is divisible by elements[j].
# If there are multiple elements that can be assigned, assign the element with the smallest index j.
# If no element satisfies the condition for a group, assign -1 to that group.
# Return an integer array assigned, where assigned[i] is the index of the element chosen for group i, or -1 if no suitable element exists.
#
# Note: An element may be assigned to more than one group.
#
#
#
# Example 1:
#
# Input: groups = [8,4,3,2,4], elements = [4,2]
#
# Output: [0,0,-1,1,0]
#
# Explanation:
#
# elements[0] = 4 is assigned to groups 0, 1, and 4.
# elements[1] = 2 is assigned to group 3.
# Group 2 cannot be assigned any element.
# Example 2:
#
# Input: groups = [2,3,5,7], elements = [5,3,3]
#
# Output: [-1,1,0,-1]
#
# Explanation:
#
# elements[1] = 3 is assigned to group 1.
# elements[0] = 5 is assigned to group 2.
# Groups 0 and 3 cannot be assigned any element.
# Example 3:
#
# Input: groups = [10,21,30,41], elements = [2,1]
#
# Output: [0,1,0,1]
#
# Explanation:
#
# elements[0] = 2 is assigned to the groups with even values, and elements[1] = 1 is assigned to the groups with odd values.
#
#
#
# Constraints:
#
# 1 <= groups.length <= 105
# 1 <= elements.length <= 105
# 1 <= groups[i] <= 105
# 1 <= elements[i] <= 105
# Solution
# Python O(N + MlogM) O(1) Math Number Theory
class Solution:
    def assignElements(self, groups: List[int], elements: List[int]) -> List[int]:
        bound: int = 100_001 # 10^5+1
        seen: set[int] = set()
        sieve: list[int] = [-1] * bound
        for idx in range(len(elements)):
            divisor: int = elements[idx]
            if divisor in seen: continue
            seen.add(divisor)
            for multiply in range(divisor, bound, divisor):
                if sieve[multiply] == -1: sieve[multiply] = idx
        output: list[int] = []
        for group in groups:
            output.append(sieve[group])
        return output

# C++ O(N + MlogM) O(1) Math Number Theory
class Solution {
public:
    vector<int> assignElements(vector<int>& groups, vector<int>& elements) {
        int bound = 100001; // 10^5+1
        std::unordered_set<int> seen;
        std::vector sieve (bound, -1);
        for (int idx = 0; idx < elements.size(); ++idx) {
            int divisor = elements[idx];
            if (seen.count(divisor)) continue;
            seen.insert(divisor);
            for (int multiply = divisor; multiply < bound; multiply += divisor) {
                if (sieve[multiply] == -1) sieve[multiply] = idx;
            }
        }
        std::vector<int> output;
        for (int& group : groups) {
            output.push_back(sieve[group]);
        }
        return output;
    }
};