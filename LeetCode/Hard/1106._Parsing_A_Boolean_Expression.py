# A boolean expression is an expression that evaluates to either true or false. It can be in one of the following shapes:
#
# 't' that evaluates to true.
# 'f' that evaluates to false.
# '!(subExpr)' that evaluates to the logical NOT of the inner expression subExpr.
# '&(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical AND of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# '|(subExpr1, subExpr2, ..., subExprn)' that evaluates to the logical OR of the inner expressions subExpr1, subExpr2, ..., subExprn where n >= 1.
# Given a string expression that represents a boolean expression, return the evaluation of that expression.
#
# It is guaranteed that the given expression is valid and follows the given rules.
#
#
#
# Example 1:
#
# Input: expression = "&(|(f))"
# Output: false
# Explanation:
# First, evaluate |(f) --> f. The expression is now "&(f)".
# Then, evaluate &(f) --> f. The expression is now "f".
# Finally, return false.
# Example 2:
#
# Input: expression = "|(f,f,f,t)"
# Output: true
# Explanation: The evaluation of (false OR false OR false OR true) is true.
# Example 3:
#
# Input: expression = "!(&(f,t))"
# Output: true
# Explanation:
# First, evaluate &(f,t) --> (false AND true) --> false --> f. The expression is now "!(f)".
# Then, evaluate !(f) --> NOT false --> true. We return true.
#
#
# Constraints:
#
# 1 <= expression.length <= 2 * 104
# expression[i] is one following characters: '(', ')', '&', '|', '!', 't', 'f', and ','.
# Solution
# Python O(N) O(N) Stack String
class Solution:
    def boolean_calc(self, left: bool, right: bool, comparison_method: str) -> bool:
        if comparison_method == '&':
            left = left and right
        elif comparison_method == '|':
            left = left or right
        return left

    def parseBoolExpr(self, expression: str) -> bool:
        stack: list[tuple[str, bool]] = []
        comparison_method: str = ''
        answer: bool = None
        for idx in range(len(expression)):
            if expression[idx] == 't':
                if answer is None:
                    answer = True
                else:
                    answer = self.boolean_calc(answer, True, comparison_method)

            elif expression[idx] == 'f':
                if answer is None:
                    answer = False
                else:
                    answer = self.boolean_calc(answer, False, comparison_method)

            elif expression[idx] in '!&|':
                stack.append((comparison_method, answer))
                comparison_method = expression[idx]
                answer = None

            elif expression[idx] == ')':
                if comparison_method == '!':
                    answer = not answer
                prev_comparison_method, prev_answer = stack.pop()
                comparison_method = prev_comparison_method
                if prev_answer is not None:
                    answer = self.boolean_calc(prev_answer, answer, comparison_method)

            elif expression[idx] in ',(':
                continue

        return answer

# C++ O(N) O(N) Stack String
class Solution {
public:
    bool booleanCalc(bool left, bool right, char comparisonMethod) {
        if (comparisonMethod == '&') {
            left = left && right;
        } else if (comparisonMethod == '|') {
            left = left | right;
        }
        return left;
    }

    bool parseBoolExpr(string expression) {
        std::vector<std::tuple<char, bool, bool>> stack;
        char comparisonMethod = 'None';
        bool answer = false;
        bool seenFirst = true;
        std::string operators = "!&|";
        std::string canSkip = "(,";
        for (int index = 0; index < expression.size(); ++index) {
            if (expression[index] == 't') {
                if (seenFirst) {
                    seenFirst = false;
                    answer = true;
                } else {
                    answer = booleanCalc(answer, true, comparisonMethod);
                }
            } else if (expression[index] == 'f') {
                if (seenFirst) {
                    seenFirst = false;
                    answer = false;
                } else {
                    answer = booleanCalc(answer, false, comparisonMethod);
                }
            } else if (operators.find(expression[index]) != std::string::npos) {
                stack.push_back(std::make_tuple(comparisonMethod, answer, seenFirst));
                seenFirst = true;
                comparisonMethod = expression[index];
            } else if (expression[index] == ')') {
                auto [prevComparisonMethod, prevSeen, prevAnswer] = stack[stack.size() - 1];
                stack.pop_back();
                if (comparisonMethod == '!') {
                    answer = !answer;
                }
                comparisonMethod = prevComparisonMethod;
                if (!prevSeen) {
                    answer = booleanCalc(answer, prevAnswer, comparisonMethod);
                }
            } else if (canSkip.find(expression[index]) != std::string::npos) {
                continue;
            }
        }
        return answer;
    }
};