//# Consider the following expansion:
//#
//# "3(ab)"     expands to "ababab"    -- because "ab" repeats 3 times
//# "2(a3(b))"  expands to "abbbabbb"  -- "a3(b)" expands to "abbb" and that repeats twice
//# Given a string, return the expansion of that string.
//#
//# Rules:
//#
//# The input is guaranteed to be well-formed and balanced.
//# Multipliers are single digits in the range 1–9, and are optional.
//# Every multiplier is immediately followed by a parenthesised group.
//# After a group is fully expanded, nothing appears beyond the final closing parenthesis.
//# Lowercase letters and digits are the only characters that appear.
//#
//# Algorithms
//# Solution
#include <string>
#include <stack>

std::string solve(const std::string& s) {
    std::stack<int> counts;
    std::stack<std::string> strs;
    std::string current = "";
    int repeat = 1;
    for (char c : s) {
        if (isdigit(c)) repeat = c - '0';
        else if (c == '(') {
            counts.push(repeat);
            strs.push(current);
            current = "";
            repeat = 1;
        }
        else if (c == ')') {
            int times = counts.top();
            counts.pop();
            std::string prev = strs.top();
            strs.pop();
            std::string expanded = "";
            for (int i = 0; i < times; ++i) expanded += current;

            current = prev + expanded;
        }
        else current += c;
    }
    return current;
}