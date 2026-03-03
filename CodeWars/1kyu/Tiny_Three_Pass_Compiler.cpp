/*
You are writing a three-pass compiler for a simple programming language into a small assembly language.

The programming language has this syntax:

    function   ::= '[' arg-list ']' expression

    arg-list   ::= /* nothing */
                 | variable arg-list

    expression ::= term
                 | expression '+' term
                 | expression '-' term

    term       ::= factor
                 | term '*' factor
                 | term '/' factor

    factor     ::= number
                 | variable
                 | '(' expression ')'
Variables are strings of alphabetic characters. Numbers are strings of decimal digits representing integers. So, for example, a function which computes a2 + b2 might look like:

    [ a b ] a*a + b*b
A function which computes the average of two numbers might look like:

    [ first second ] (first + second) / 2
You need write a three-pass compiler. All test cases will be valid programs, so you needn't concentrate on error-handling.

The first pass will be the method pass1 which takes a string representing a function in the original programming language and will return a (JSON) object that represents that Abstract Syntax Tree. The Abstract Syntax Tree must use the following representations:

    { 'op': '+', 'a': a, 'b': b }    // add subtree a to subtree b
    { 'op': '-', 'a': a, 'b': b }    // subtract subtree b from subtree a
    { 'op': '*', 'a': a, 'b': b }    // multiply subtree a by subtree b
    { 'op': '/', 'a': a, 'b': b }    // divide subtree a from subtree b
    { 'op': 'arg', 'n': n }          // reference to n-th argument, n integer
    { 'op': 'imm', 'n': n }          // immediate value n, n integer
Note: arguments are indexed from zero. So, for example, the function

[ x y ] ( x + y ) / 2 would look like:

    { 'op': '/', 'a': { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                                   'b': { 'op': 'arg', 'n': 1 } },
                 'b': { 'op': 'imm', 'n': 2 } }
The second pass of the compiler will be called pass2. This pass will take the output from pass1 and return a new Abstract Syntax Tree (with the same format) with all constant expressions reduced as much as possible. So, if for example, the function is [ x ] x + 2*5, the result of pass1 would be:

    { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                 'b': { 'op': '*', 'a': { 'op': 'imm', 'n': 2 },
                                   'b': { 'op': 'imm', 'n': 5 } } }
This would be passed into pass2 which would return:

    { 'op': '+', 'a': { 'op': 'arg', 'n': 0 },
                 'b': { 'op': 'imm', 'n': 10 } }
The third pass of the compiler is pass3. The pass3 method takes in an Abstract Syntax Tree and returns an array of strings. Each string is an assembly directive. You are working on a small processor with two registers (R0 and R1), a stack, and an array of input arguments. The result of a function is expected to be in R0. The processor supports the following instructions:

    "IM n"     // load the constant value n into R0
    "AR n"     // load the n-th input argument into R0
    "SW"       // swap R0 and R1
    "PU"       // push R0 onto the stack
    "PO"       // pop the top value off of the stack into R0
    "AD"       // add R1 to R0 and put the result in R0
    "SU"       // subtract R1 from R0 and put the result in R0
    "MU"       // multiply R0 by R1 and put the result in R0
    "DI"       // divide R0 by R1 and put the result in R0
So, one possible return value from pass3 given the Abstract Syntax Tree shown above from pass2 is:

    [ "IM 10", "SW", "AR 0", "AD" ]
Here is a simulator for the target machine. It takes an array of assembly instructions and an array of arguments and returns the result.

def simulate(asm, argv):
    r0, r1 = None, None
    stack = []
    for ins in asm:
        if ins[:2] == 'IM' or ins[:2] == 'AR':
            ins, n = ins[:2], int(ins[2:])
        if ins == 'IM':   r0 = n
        elif ins == 'AR': r0 = argv[n]
        elif ins == 'SW': r0, r1 = r1, r0
        elif ins == 'PU': stack.append(r0)
        elif ins == 'PO': r0 = stack.pop()
        elif ins == 'AD': r0 += r1
        elif ins == 'SU': r0 -= r1
        elif ins == 'MU': r0 *= r1
        elif ins == 'DI': r0 /= r1
    return r0
CompilersAlgorithms
*/
// Solution
#include <vector>
#include <string>
#include <regex>
#include <unordered_map>
#include <stack>
#include <cctype>
#include <memory>

using namespace std;

struct AST {
    string op;
    AST* a = nullptr;
    AST* b = nullptr;
    int n = 0;

    AST(string op) : op(op) {}
    AST(string op, int n) : op(op), n(n) {}
    AST(string op, AST* a, AST* b) : op(op), a(a), b(b) {}
};

struct Compiler {

    vector<string> compile(string program) {
        return pass3(pass2(pass1(program)));
    }

    vector<string> tokenize(string program) {
        static regex re("[-+*/()[\\]]|[A-Za-z]+|\\d+");
        sregex_token_iterator it(program.begin(), program.end(), re);
        return vector<string>(it, sregex_token_iterator());
    }

    AST* pass1(string program) {
        auto tokens = tokenize(program);

        unordered_map<string,int> args;
        int idx = parseArguments(tokens, args);

        vector<string> exprTokens(tokens.begin() + idx + 1, tokens.end());
        return tokensToAST(args, exprTokens);
    }

    int parseArguments(const vector<string>& tokens,
                       unordered_map<string,int>& args) {

        if (tokens.empty() || tokens[0] != "[")
            throw runtime_error("Invalid argument list");

        int argIndex = 0;
        for (int i = 1; i < tokens.size(); i++) {
            if (tokens[i] == "]")
                return i;
            args[tokens[i]] = argIndex++;
        }

        throw runtime_error("Invalid argument list");
    }

    bool equalOrder(string op1, string op2) {
        return op1 == op2 ||
               ((op1=="*"||op1=="/") && (op2=="*"||op2=="/")) ||
               ((op1=="+"||op1=="-") && (op2=="+"||op2=="-"));
    }

    bool greaterOrder(string op1, string op2) {
        return (op1=="*"||op1=="/") &&
               (op2=="+"||op2=="-");
    }

    bool greaterOrEqual(string op1, string op2) {
        return equalOrder(op1, op2) || greaterOrder(op1, op2);
    }

    AST* tokensToAST(unordered_map<string,int>& args,
                     vector<string>& tokens) {

        vector<AST*> outStack;
        vector<string> opStack;

        auto applyOp = [&]() {
            string op = opStack.front();
            opStack.erase(opStack.begin());

            AST* b = outStack.back(); outStack.pop_back();
            AST* a = outStack.back(); outStack.pop_back();

            outStack.push_back(new AST(op, a, b));
        };

        for (auto& token : tokens) {

            if (token != "+" && token != "-" &&
                token != "*" && token != "/" &&
                token != "(" && token != ")") {

                if (isdigit(token[0])) {
                    outStack.push_back(new AST("imm", stoi(token)));
                } else {
                    outStack.push_back(new AST("arg", args[token]));
                }

            } else if (token == "+" || token == "-" ||
                       token == "*" || token == "/") {

                while (!opStack.empty() &&
                       greaterOrEqual(opStack.front(), token)) {
                    applyOp();
                }
                opStack.insert(opStack.begin(), token);

            } else if (token == "(") {
                opStack.insert(opStack.begin(), token);

            } else if (token == ")") {
                while (!opStack.empty() && opStack.front() != "(") {
                    applyOp();
                }
                opStack.erase(opStack.begin());
            }
        }

        while (!opStack.empty())
            applyOp();

        return outStack.back();
    }

    AST* pass2(AST* ast) {

        if (!ast) return ast;

        if (ast->op == "+" || ast->op == "-" ||
            ast->op == "*" || ast->op == "/") {

            ast->a = pass2(ast->a);
            ast->b = pass2(ast->b);

            if (ast->a->op == "imm" && ast->b->op == "imm") {
                int x = ast->a->n;
                int y = ast->b->n;
                int result = 0;

                if (ast->op == "+") result = x + y;
                if (ast->op == "-") result = x - y;
                if (ast->op == "*") result = x * y;
                if (ast->op == "/") result = x / y;

                return new AST("imm", result);
            }
        }

        return ast;
    }

    vector<string> pass3(AST* ast) {

        vector<string> result;

        if (!ast) return result;

        if (ast->op == "+" || ast->op == "-" ||
            ast->op == "*" || ast->op == "/") {

            auto left = pass3(ast->a);
            auto right = pass3(ast->b);

            result.insert(result.end(), left.begin(), left.end());
            result.push_back("PU");
            result.insert(result.end(), right.begin(), right.end());
            result.push_back("SW");
            result.push_back("PO");

            if (ast->op == "+") result.push_back("AD");
            if (ast->op == "-") result.push_back("SU");
            if (ast->op == "*") result.push_back("MU");
            if (ast->op == "/") result.push_back("DI");

            return result;
        }

        if (ast->op == "imm") {
            result.push_back("IM " + to_string(ast->n));
        }

        if (ast->op == "arg") {
            result.push_back("AR " + to_string(ast->n));
        }

        return result;
    }
};