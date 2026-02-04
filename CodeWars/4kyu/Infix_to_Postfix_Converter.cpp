/*
Construct a function that, when given a string containing an expression in infix notation, will return an identical expression in postfix notation.

The operators used will be +, -, *, /, and ^ with left-associativity of all operators but ^.

The precedence of the operators (most important to least) are : 1) parentheses, 2) exponentiation, 3) times/divide, 4) plus/minus.

The operands will be single-digit integers between 0 and 9, inclusive.

Parentheses may be included in the input, and are guaranteed to be in correct pairs.

to_postfix("2+7*5") # Should return "275*+"
to_postfix("3*3/(7+1)") # Should return "33*71+/"
to_postfix("5+(6-2)*9+3^(7-1)") # Should return "562-9*+371-^+"
to_postfix("1^2^3") # Should return "123^^"
You may read more about postfix notation, also called Reverse Polish notation, here: http://en.wikipedia.org/wiki/Reverse_Polish_notation

MathematicsAlgorithms
*/
// Solution
#include <string>
#include <stack>
#include <unordered_map>

int precedence(char op) {
    switch (op) {
        case '^': return 3;
        case '*':
        case '/': return 2;
        case '+':
        case '-': return 1;
    }
    return 0;
}

bool is_right_associative(char op) {
    return op == '^';
}

bool is_operator(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/' || c == '^';
}

std::string to_postfix(std::string infix) {
    std::string output;
    std::stack<char> ops;
    for (char c : infix) {
        if (c >= '0' && c <= '9') output += c;
        else if (c == '(') ops.push(c);
        else if (c == ')') {
            while (!ops.empty() && ops.top() != '(') {
                output += ops.top();
                ops.pop();
            }
            ops.pop();
        }
        else if (is_operator(c)) {
            while (!ops.empty() && is_operator(ops.top())) {
                char top = ops.top();
                if (
                    precedence(top) > precedence(c) ||
                    (precedence(top) == precedence(c) && !is_right_associative(c))
                ) {
                    output += top;
                    ops.pop();
                } else break;
            }
            ops.push(c);
        }
    }
    while (!ops.empty()) {
        output += ops.top();
        ops.pop();
    }
    return output;
}