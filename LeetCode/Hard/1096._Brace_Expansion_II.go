/*
Under the grammar given below, strings can represent a set of lowercase words. Let R(expr) denote the set of words the expression represents.

The grammar can best be understood through simple examples:

Single letters represent a singleton set containing that word.
R("a") = {"a"}
R("w") = {"w"}
When we take a comma-delimited list of two or more expressions, we take the union of possibilities.
R("{a,b,c}") = {"a","b","c"}
R("{{a,b},{b,c}}") = {"a","b","c"} (notice the final set only contains each word at most once)
When we concatenate two expressions, we take the set of possible concatenations between two words where the first word comes from the first expression and the second word comes from the second expression.
R("{a,b}{c,d}") = {"ac","ad","bc","bd"}
R("a{b,c}{d,e}f{g,h}") = {"abdfg", "abdfh", "abefg", "abefh", "acdfg", "acdfh", "acefg", "acefh"}
Formally, the three rules for our grammar:

For every lowercase letter x, we have R(x) = {x}.
For expressions e1, e2, ... , ek with k >= 2, we have R({e1, e2, ...}) = R(e1) ∪ R(e2) ∪ ...
For expressions e1 and e2, we have R(e1 + e2) = {a + b for (a, b) in R(e1) × R(e2)}, where + denotes concatenation, and × denotes the cartesian product.
Given an expression representing a set of words under the given grammar, return the sorted list of words that the expression represents.

 

Example 1:

Input: expression = "{a,b}{c,{d,e}}"
Output: ["ac","ad","ae","bc","bd","be"]
Example 2:

Input: expression = "{{a,z},a{b,c},{ab,z}}"
Output: ["a","ab","ac","z"]
Explanation: Each distinct word is written only once in the final answer.
 

Constraints:

1 <= expression.length <= 60
expression[i] consists of '{', '}', ','or lowercase English letters.
The given expression represents a set of words based on the grammar given in the description.
*/
// Solution
// Go O(NM) O(NM) Stack String
func braceExpansionII(expression string) []string {
    op := []byte{}
    stk := []map[string]bool{}
    ope := func() {
        l, r := len(stk)-2, len(stk)-1
        if op[len(op)-1] == '+' {
            for k := range stk[r] {
                stk[l][k] = true
            }
        } else {
            tmp := make(map[string]bool)
            for left := range stk[l] {
                for right := range stk[r] {
                    tmp[left+right] = true
                }
            }
            stk[l] = tmp
        }
        op = op[:len(op)-1]
        stk = stk[:len(stk)-1]
    }

    for i := 0; i < len(expression); i++ {
        if expression[i] == ',' {
            for len(op) > 0 && op[len(op)-1] == '*' {
                ope()
            }
            op = append(op, '+')
        } else if expression[i] == '{' {
            if i > 0 && (expression[i-1] == '}' || (expression[i-1] >= 'a' && expression[i-1] <= 'z')) {
                op = append(op, '*')
            }
            op = append(op, '{')
        } else if expression[i] == '}' {
            for len(op) > 0 && op[len(op)-1] != '{' {
                ope()
            }
            op = op[:len(op)-1]
        } else {
            if i > 0 && (expression[i-1] == '}' || (expression[i-1] >= 'a' && expression[i-1] <= 'z')) {
                op = append(op, '*')
            }
            set := map[string]bool{string(expression[i]): true}
            stk = append(stk, set)
        }
    }
    for len(op) > 0 { ope() }
    result := make([]string, 0, len(stk[0]))
    for k := range stk[0] { result = append(result, k) }
    sort.Strings(result)
    return result
}