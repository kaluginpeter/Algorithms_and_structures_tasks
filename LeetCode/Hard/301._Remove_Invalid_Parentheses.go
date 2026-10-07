/*
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

Return a list of unique strings that are valid with the minimum number of removals. You may return the answer in any order.

 

Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]
Example 2:

Input: s = "(a)())()"
Output: ["(a())()","(a)()()"]
Example 3:

Input: s = ")("
Output: [""]
 

Constraints:

1 <= s.length <= 25
s consists of lowercase English letters and parentheses '(' and ')'.
There will be at most 20 parentheses in s.
*/
// Solution
// Go O(2^N) O(N) Backtracking String
func getNumberOfMinDeletions(s *string) int {
    var output, cur int = 0, 0
    for _, ch := range *s {
        if ch == '(' {
            cur++
        } else if ch == ')' {
            cur--
            if cur < 0 {
                cur++
                output++
            }
        }
    }
    return output + cur
}

func backtrack(i, n, bound, acc int, curSeq *[]byte, s *string, output *[]string) {
    if i == n {
        if acc != 0 { return } // not all open brackets are closed
        *output = append(*output, string(*curSeq))
        return
    }
    var ch rune = rune((*s)[i])
    if ch == '(' {
        if bound > 0 {
            backtrack(i + 1, n, bound - 1, acc, curSeq, s, output)
        }
        *curSeq = append(*curSeq, byte(ch))
        backtrack(i + 1, n, bound, acc + 1, curSeq, s, output)
        *curSeq = (*curSeq)[:len(*curSeq) - 1]
    } else if ch == ')' {
        if bound > 0 {
            backtrack(i + 1, n, bound - 1, acc, curSeq, s, output)
        }
        if acc - 1 >= 0 {
            *curSeq = append(*curSeq, byte(ch))
            backtrack(i + 1, n, bound, acc - 1, curSeq, s, output)
            *curSeq = (*curSeq)[:len(*curSeq) - 1]
        }
    } else {
        *curSeq = append(*curSeq, byte(ch))
        backtrack(i + 1, n, bound, acc, curSeq, s, output)
        *curSeq = (*curSeq)[:len(*curSeq) - 1]
    }
}

func eraseDuplicates(output *[]string) {
    var hashmap map[string]bool = map[string]bool{}
    var sieved []string = []string{}
    for _, seq := range *output {
        _, was := hashmap[seq]; if !was {
            sieved = append(sieved, seq)
            hashmap[seq] = true
        }
    }
    *output = sieved
}

func removeInvalidParentheses(s string) []string {
    var bound int = getNumberOfMinDeletions(&s)
    var output []string = []string{}
    var curSeq []byte = []byte{}
    var n int = len(s)
    backtrack(0, n, bound, 0, &curSeq, &s, &output)
    eraseDuplicates(&output)
    return output
}

// C++ O(2^N) O(N) String Backtracking
int getNumberOfMinDeletions(std::string& s) {
    int output = 0, cur = 0;
    for (char& ch : s) {
        if (ch == '(') ++cur;
        else if (ch == ')') {
            --cur;
            if (cur < 0) {
                ++output; ++cur;
            }
        }
    }
    return output + cur;
}

void backtrack(int i, int n, int bound, int acc, std::string& curSeq, std::string& s, std::vector<std::string>& output, std::unordered_set<std::string>& seen) {
    if (i == n) {
        if (acc || seen.count(curSeq)) return;
        seen.insert(curSeq);
        output.push_back(curSeq);
        return;
    }
    if (s[i] == '(') {
        if (bound) backtrack(i + 1, n, bound - 1, acc, curSeq, s, output, seen);
        curSeq.push_back(s[i]);
        backtrack(i + 1, n, bound, acc + 1, curSeq, s, output, seen);
        curSeq.pop_back();
    } else if (s[i] == ')') {
        if (bound) backtrack(i + 1, n, bound - 1, acc, curSeq, s, output, seen);
        if (acc) {
            curSeq.push_back(s[i]);
            backtrack(i + 1, n, bound, acc - 1, curSeq, s, output, seen);
            curSeq.pop_back();
        }
    } else {
        curSeq.push_back(s[i]);
        backtrack(i + 1, n, bound, acc, curSeq, s, output, seen);
        curSeq.pop_back();
    }
}

class Solution {
public:
    vector<string> removeInvalidParentheses(string s) {
        int bound = getNumberOfMinDeletions(s), n = s.size();
        std::vector<std::string> output;
        std::string curSeq = "";
        std::unordered_set<std::string> seen;
        backtrack(0, n, bound, 0, curSeq, s, output, seen);
        return output;
    }
};