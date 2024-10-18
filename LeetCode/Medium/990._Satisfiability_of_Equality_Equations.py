# You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.
#
# Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.
#
#
#
# Example 1:
#
# Input: equations = ["a==b","b!=a"]
# Output: false
# Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
# There is no way to assign the variables to satisfy both equations.
# Example 2:
#
# Input: equations = ["b==a","a==b"]
# Output: true
# Explanation: We could assign a = 1 and b = 1 to satisfy both equations.
#
#
# Constraints:
#
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] is a lowercase letter.
# equations[i][1] is either '=' or '!'.
# equations[i][2] is '='.
# equations[i][3] is a lowercase letter.
# Solution
# Python O(N) O(N) Union Find
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parents: list[int] = list(range(n))
        self.ranks: list[int] = [1] * n

    def find(self, x: int) -> int:
        while x != self.parents[x]:
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x

    def unionFind(self, x: int, y: int) -> None:
        root_x: bool = self.find(x)
        root_y: bool = self.find(y)
        if root_x == root_y:
            return
        if self.ranks[root_x] >= self.ranks[root_y]:
            self.parents[root_y] = root_x
            self.ranks[root_x] += self.ranks[root_y]
        else:
            self.parents[root_x] = root_y
            self.ranks[root_y] += self.ranks[root_x]


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        variables: dict[str, int] = dict()
        idx: int = 0
        for equation in equations:
            x: str = equation[0]
            y: str = equation[-1]
            if x not in variables:
                variables[x] = idx
                idx += 1
            if y not in variables:
                variables[y] = idx
                idx += 1
        UF: UnionFind = UnionFind(len(variables))
        for equation in equations:
            x: int = variables[equation[0]]
            y: int = variables[equation[-1]]
            operation_is_equal: bool = equation[1] == '='
            if operation_is_equal:
                UF.unionFind(x, y)
        for equation in equations:
            x: int = variables[equation[0]]
            y: int = variables[equation[-1]]
            operation_not_equal: bool = equation[1] == '!'
            if operation_not_equal and UF.find(x) == UF.find(y):
                return False
        return True

# C++ O(N) O(N) UnionFind
class UnionFind {
public:
    std::vector<int> parents;
    std::vector<int> ranks;
    UnionFind(int n) {
        parents.resize(n);
        std::iota(parents.begin(), parents.end(), 0);
        ranks.resize(n, 1);
    };

    int find(int x) {
        while (x != parents[x]) {
            parents[x] = parents[parents[x]];
            x = parents[x];
        }
        return x;
    };

    bool unionFind(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) {
            return true;
        }
        if (ranks[rootX] >= ranks[rootY]) {
            parents[rootY] = rootX;
            ranks[rootX] += ranks[rootY];
        } else {
            parents[rootX] = rootY;
            ranks[rootY] += ranks[rootX];
        }
        return true;
    };
};

class Solution {
public:
    bool equationsPossible(vector<string>& equations) {
        std::unordered_map<char, int> variables;
        int index = 0;
        for (const std::string& equation : equations) {
            if (variables.find(equation[0]) == variables.end()) {
                variables[equation[0]] = index++;
            }
            if (variables.find(equation[3]) == variables.end()) {
                variables[equation[3]] = index++;
            }
        }
        UnionFind* UF = new UnionFind(static_cast<int>(variables.size()));
        for (std::string pair : equations) {
            int x = variables[pair[0]];
            int y = variables[pair[pair.size() - 1]];
            int operator_is_equal = pair[1] == '=';
            if (operator_is_equal) {
                UF->unionFind(x, y);
            }
        }
        for (std::string pair : equations) {
            int x = variables[pair[0]];
            int y = variables[pair[pair.size() - 1]];
            int operator_not_equal = pair[1] == '!';
            if (operator_not_equal && UF->find(x) == UF->find(y)) {
                return false;
            }
        }
        return true;
    }
};