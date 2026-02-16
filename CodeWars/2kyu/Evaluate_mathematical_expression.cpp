/*
Instructions
Given a mathematical expression as a string you must return the result as a number.

Numbers
Number may be both whole numbers and/or decimal numbers. The same goes for the returned result.

Operators
You need to support the following mathematical operators:

Multiplication *
Division / (as floating point division)
Addition +
Subtraction -
Operators are always evaluated from left-to-right, and * and / must be evaluated before + and -.

Parentheses
You need to support multiple levels of nested parentheses, ex. (2 / (2 + 3.33) * 4) - -6

Whitespace
There may or may not be whitespace between numbers and operators.

An addition to this rule is that the minus sign (-) used for negating numbers and parentheses will never be separated by whitespace. I.e all of the following are valid expressions.

1-1    // 0
1 -1   // 0
1- 1   // 0
1 - 1  // 0
1- -1  // 2
1 - -1 // 2
1--1   // 2

6 + -(4)   // 2
6 + -( -4) // 10
And the following are invalid expressions

1 - - 1    // Invalid
1- - 1     // Invalid
6 + - (4)  // Invalid
6 + -(- 4) // Invalid
Validation
You do not need to worry about validation - you will only receive valid mathematical expressions following the above rules.

Restricted APIs
MathematicsParsingAlgorithms
*/
// Solution
#include <string>
#include <cctype>

class Parser {
public:
    Parser(const std::string& s) : str(s), pos(0) {}
    double parse() {
        return expression();
    }

private:
    std::string str;
    size_t pos;
    void skipSpaces() {
        while (pos < str.size() && std::isspace(str[pos])) ++pos;
    }
    double expression() {
        double value = term();
        while (true) {
            skipSpaces();
            if (pos >= str.size()) break;
            if (str[pos] == '+') {
                ++pos;
                value += term();
            } else if (str[pos] == '-') {
                ++pos;
                value -= term();
            } else break;
        }
        return value;
    }
    double term() {
        double value = factor();
        while (true) {
            skipSpaces();
            if (pos >= str.size()) break;
            if (str[pos] == '*') {
                ++pos;
                value *= factor();
            } else if (str[pos] == '/') {
                ++pos;
                value /= factor();
            } else break;
        }
        return value;
    }
    double factor() {
        skipSpaces();
        if (str[pos] == '+') {
            ++pos;
            return factor();
        }
        if (str[pos] == '-') {
            ++pos;
            return -factor();
        }
        if (str[pos] == '(') {
            ++pos;
            double value = expression();
            skipSpaces();
            ++pos;
            return value;
        }
        return number();
    }
    double number() {
        skipSpaces();
        double value = 0;
        bool hasDecimal = false;
        double decimalPlace = 0.1;
        while (pos < str.size() && (std::isdigit(str[pos]) || str[pos] == '.')) {
            if (str[pos] == '.') hasDecimal = true;
            else if (!hasDecimal) value = value * 10 + (str[pos] - '0');
            else {
                value += (str[pos] - '0') * decimalPlace;
                decimalPlace *= 0.1;
            }
            ++pos;
        }
        return value;
    }
};

double calc(const std::string& expression) {
    Parser parser(expression);
    return parser.parse();
}