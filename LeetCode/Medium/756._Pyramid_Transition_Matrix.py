# You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.
#
# To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.
#
# For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
# You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.
#
# Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.
#
#
#
# Example 1:
#
#
# Input: bottom = "BCD", allowed = ["BCC","CDE","CEA","FFF"]
# Output: true
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 3), we can build "CE" on level 2 and then build "A" on level 1.
# There are three triangular patterns in the pyramid, which are "BCC", "CDE", and "CEA". All are allowed.
# Example 2:
#
#
# Input: bottom = "AAAA", allowed = ["AAB","AAC","BCD","BBE","DEF"]
# Output: false
# Explanation: The allowed triangular patterns are shown on the right.
# Starting from the bottom (level 4), there are multiple ways to build level 3, but trying all the possibilites, you will get always stuck before building level 1.
#
#
# Constraints:
#
# 2 <= bottom.length <= 6
# 0 <= allowed.length <= 216
# allowed[i].length == 3
# The letters in all input strings are from the set {'A', 'B', 'C', 'D', 'E', 'F'}.
# All the values of allowed are unique.
# Solution
# Python O(M^N) O(M^N * N) Backtracking Memoization
class Solution:
    def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
        bricks: dict[str, list[str]] = dict()
        memo: dict[str, bool] = dict()
        for brick in allowed:
            if brick[:2] not in bricks: bricks[brick[:2]] = []
            bricks[brick[:2]].append(brick[-1])
        def dfs(bottom: str) -> bool:
            if len(bottom) == 1: return True
            elif memo.get(bottom): return memo.get(bottom)
            next_rows: list[str] = []
            reconstruct(bottom, 0, [], next_rows)
            for row in next_rows:
                if dfs(row):
                    memo[bottom] = True
                    return True
            memo[bottom] = False
            return False
        def reconstruct(bottom: str, i: int, cur: list[str], next_rows: list[str]) -> None:
            if i + 1 == len(bottom):
                next_rows.append(''.join(cur))
                return
            if bottom[i:i + 2] not in bricks: return
            for brick in bricks[bottom[i:i + 2]]:
                cur.append(brick)
                reconstruct(bottom, i + 1, cur, next_rows)
                cur.pop()
        return dfs(bottom)

# C++ O(M^N) O(M^N * N) Memoization Backtracking
class Solution {
public:
    unordered_map<string, vector<char>> bricks;
    unordered_map<string, bool> memo;
    bool dfs(const string& bottom) {
        if (bottom.size() == 1) return true;
        if (memo.count(bottom)) return memo[bottom];
        vector<string> nextRows;
        reconstruct(bottom, 0, "", nextRows);
        for (const string& next : nextRows) {
            if (dfs(next)) return memo[bottom] = true;
        }
        return memo[bottom] = false;
    }

    void reconstruct(const string& bottom, int idx, string cur, vector<string>& res) {
        if (idx == bottom.size() - 1) {
            res.push_back(cur);
            return;
        }
        string key = bottom.substr(idx, 2);
        if (!bricks.count(key)) return;
        for (char c : bricks[key]) reconstruct(bottom, idx + 1, cur + c, res);
    }

    bool pyramidTransition(string bottom, vector<string>& allowed) {
        for (const string& s : allowed) bricks[s.substr(0, 2)].push_back(s[2]);
        return dfs(bottom);
    }
};