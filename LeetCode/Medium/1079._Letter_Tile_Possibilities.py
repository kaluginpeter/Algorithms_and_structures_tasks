# You have n  tiles, where each tile has one letter tiles[i] printed on it.
#
# Return the number of possible non-empty sequences of letters you can make using the letters printed on those tiles.
#
#
#
# Example 1:
#
# Input: tiles = "AAB"
# Output: 8
# Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB", "ABA", "BAA".
# Example 2:
#
# Input: tiles = "AAABBC"
# Output: 188
# Example 3:
#
# Input: tiles = "V"
# Output: 1
#
#
# Constraints:
#
# 1 <= tiles.length <= 7
# tiles consists of uppercase English letters.
# Solution
# Python O(2**N) O(N) Backtracking
class Solution:
    def backtrack(self, chunks: list[int]) -> int:
        permutations: int = 0
        for chunk in range(26):
            if not chunks[chunk]: continue
            permutations += 1
            chunks[chunk] -= 1
            permutations += self.backtrack(chunks)
            chunks[chunk] += 1
        return permutations

    def numTilePossibilities(self, tiles: str) -> int:
        chunks: list[int] = [0] * 26
        for letter in tiles:
            chunks[ord(letter) - 65] += 1
        return self.backtrack(chunks)

# C++ O(2**N) O(N) Backtracking
class Solution {
public:
    void backtrack(std::string& substr, std::string& tiles, std::unordered_set<std::string>& seen, std::vector<bool>& used) {
        if (substr.size() == tiles.size()) return;
        for (int idx = 0; idx < tiles.size(); ++idx) {
            if (used[idx]) continue;
            used[idx] = true;
            substr.push_back(tiles[idx]);
            seen.insert(substr);
            backtrack(substr, tiles, seen, used);
            used[idx] = false;
            substr.pop_back();
        }
    }

    int numTilePossibilities(string tiles) {
        std::string substr = "";
        int curIdx = 0;
        std::vector<bool> used (7, false);
        std::unordered_set<std::string> seen;
        backtrack(substr, tiles, seen, used);
        return seen.size();
    }
};