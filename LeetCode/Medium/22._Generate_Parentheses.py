# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
#
#
# Example 1:
#
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
#
# Input: n = 1
# Output: ["()"]
#
#
# Constraints:
#
# 1 <= n <= 8
# Solution Backtracking Recursive O(4**N) O(4**N)
class Solution:
    def backtrack(self, n: int, left: int, right: int, output: list[str], result: list[str]) -> None:
        if left >= n and right >= n:
            result.append(''.join(output))

        if left < n:
            output.append('(')
            self.backtrack(n, left + 1, right, output, result)
            output.pop()
        if right < left:
            output.append(')')
            self.backtrack(n, left, right + 1, output, result)
            output.pop()

    def generateParenthesis(self, n: int) -> List[str]:
        result: list[str] = []
        output: list[str] = []
        self.backtrack(n, 0, 0, output, result)
        return result


# Go O(2^N) O(2^N) Backtracking
func dfs(open, closed int, output *[]string, seq string, bound int) {
    if open == closed && open == bound {
        *output = append(*output, seq)
        return
    }
    if open < bound {
        dfs(open + 1, closed, output, seq + "(", bound)
    }
    if closed < bound && closed < open {
        dfs(open, closed + 1, output, seq + ")", bound)
    }
}
func generateParenthesis(n int) []string {
    var output []string = []string{}
    dfs(0, 0, &output, "", n)
    return output
}

# C++ O(2^N) O(2^N) Backtracking
class Solution {
public:
    void dfs(int& open, int& closed, const int& n, std::string& seq, std::vector<std::string>& output) {
        if (open == closed && open == n) {
            output.emplace_back(std::string(seq));
            return;
        }
        if (open < n) {
            seq.push_back('(');
            ++open;
            dfs(open, closed, n, seq, output);
            --open;
            seq.pop_back();
        }
        if (closed < n && closed < open) {
            seq.push_back(')');
            ++closed;
            dfs(open, closed, n, seq, output);
            --closed;
            seq.pop_back();
        }
    }
    vector<string> generateParenthesis(int n) {
        int open = 0, closed = 0;
        std::string seq = "";
        std::vector<std::string> output;
        dfs(open, closed, n, seq, output);
        return output;
    }
};