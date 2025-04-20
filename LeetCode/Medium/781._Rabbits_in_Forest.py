# There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.
#
# Given the array answers, return the minimum number of rabbits that could be in the forest.
#
#
#
# Example 1:
#
# Input: answers = [1,1,2]
# Output: 5
# Explanation:
# The two rabbits that answered "1" could both be the same color, say red.
# The rabbit that answered "2" can't be red or the answers would be inconsistent.
# Say the rabbit that answered "2" was blue.
# Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
# The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
# Example 2:
#
# Input: answers = [10,10,10]
# Output: 11
#
#
# Constraints:
#
# 1 <= answers.length <= 1000
# 0 <= answers[i] < 1000
# Solution
# Python O(N) O(D) HashMap Greedy Math
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        seen: dict[int, int] = dict()
        for same in answers:
            seen[same + 1] = seen.get(same + 1, 0) + 1
        rabbits: int = 0
        for same, members in seen.items():
            whole: int = members // same
            rabbits += whole * same
            if same * whole != members: rabbits += same
        return rabbits

# C++ O(N) O(D) HashMap Greedy Math
class Solution {
public:
    int numRabbits(vector<int>& answers) {
        unordered_map<int, int> seen;
        for (int &same : answers) ++seen[same + 1];
        int rabbits = 0;
        for (auto &p : seen) {
            int whole = p.second / p.first;
            rabbits += whole * p.first;
            if (p.first * whole != p.second) rabbits += p.first;
        }
        return rabbits;
    }
};