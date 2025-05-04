# Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.
#
# Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].
#
#
#
# Example 1:
#
# Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
# Output: 1
# Example 2:
#
# Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
# Output: 3
#
#
# Constraints:
#
# 1 <= dominoes.length <= 4 * 104
# dominoes[i].length == 2
# 1 <= dominoes[i][j] <= 9
# Solution
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        d = {}
        count = 0  
        for i in dominoes:
            t = (min(i), max(i))
            if t in d:
                count += d[t]
                d[t] += 1
            else:
                d[t] = 1
        return count


# Python O(N) O(N) HashMap Counting
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        output: int = 0
        hashmap: dict[tuple[int, int], int] = dict()
        for domino in dominoes:
            x: int = hashmap.get((domino[0], domino[1]), 0)
            y: int = hashmap.get((domino[1], domino[0]), 0)
            if domino[0] == domino[1]: y = 0
            output += x + y
            hashmap[(domino[0], domino[1])] = hashmap.get((domino[0], domino[1]), 0) + 1
        return output

# C++ O(N) O(N) HashMap Counting
#include <unordered_map>
#include <functional>

struct PairHash {
    size_t operator()(const std::pair<int, int>& p) const {
        auto hash1 = std::hash<int>{}(p.first);
        auto hash2 = std::hash<int>{}(p.second);
        return hash1 ^ (hash2 << 1);
    }
};

class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<pair<int, int>, int, PairHash> hashmap;
        int output = 0;
        for (vector<int>& domino : dominoes) {
            int x = hashmap[{domino[0], domino[1]}];
            int y = hashmap[{domino[1], domino[0]}];
            if (domino[0] == domino[1]) y = 0;
            output += x + y;
            ++hashmap[{domino[0], domino[1]}];
        }
        return output;
    }
};