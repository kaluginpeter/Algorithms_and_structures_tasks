# You are writing a three-pass compiler for a simple programming language into a small assembly language.
#
# The programming language has this syntax:
#
#     function   ::= '[' arg-list ']' expression
#
#     arg-list   ::= /* nothing */
#                  | variable arg-list
#
#     expression ::= term
#                  | expression '+' term
#                  | expression '-' term
#
#     term       ::= factor
#                  | term '*' factor
#                  | term '/' factor
#
#     factor     ::= number
#                  | variable
#                  | '(' expression ')'
# Variables are strings of alphabetic characters. Numbers are strings of decimal digits representing integers. So, for example, a function which computes a2 + b2 might look like:
#
#     [ a b ] a*a + b*b
# A function which computes the average of two numbers might look like:
#
#     [ first second ] (first + second) / 2
# You need write a three-pass compiler. All test cases will be valid programs, so you needn't concentrate on error-handling.
#
# The first pass will be the method pass1 which takes a string representing a function in the original programming language and will return a (JSON) object that represents that Abstract Syntax Tree. The Abstract Syntax Tree must use the following representations:
#
#   // Each node is of type 'AST' and has the following fields:
#   // 'string op', 'AST* a', 'AST* b', and 'int n'
#   AST ("+", a, b)       // add subtree a to subtree b
#   AST ("-", a, b)       // subtract subtree b from subtree a
#   AST ("*", a, b)       // multiply subtree a by subtree b
#   AST ("/", a, b)       // divide subtree a from subtree b
#   AST ("arg", n)        // reference to n-th argument, n integer
#   AST ("imm", n)        // immediate value n, n integer
# Note: arguments are indexed from zero. So, for example, the function
#
# [ x y ] ( x + y ) / 2 would look like:
#
#   new AST ("/", new AST ("+", new AST ("arg", 0), new AST ("arg", 1)), new AST ("imm", 2))
# The second pass of the compiler will be called pass2. This pass will take the output from pass1 and return a new Abstract Syntax Tree (with the same format) with all constant expressions reduced as much as possible. So, if for example, the function is [ x ] x + 2*5, the result of pass1 would be:
#
# new AST ("+", new AST ("arg", 0), new AST ("*", new AST ("imm", 2), new AST ("imm", 5)))
# This would be passed into pass2 which would return:
#
# new AST ("+", new AST ("arg", 0), new AST ("imm", 10))
# The third pass of the compiler is pass3. The pass3 method takes in an Abstract Syntax Tree and returns an array of strings. Each string is an assembly directive. You are working on a small processor with two registers (R0 and R1), a stack, and an array of input arguments. The result of a function is expected to be in R0. The processor supports the following instructions:
#
#     "IM n"     // load the constant value n into R0
#     "AR n"     // load the n-th input argument into R0
#     "SW"       // swap R0 and R1
#     "PU"       // push R0 onto the stack
#     "PO"       // pop the top value off of the stack into R0
#     "AD"       // add R1 to R0 and put the result in R0
#     "SU"       // subtract R1 from R0 and put the result in R0
#     "MU"       // multiply R0 by R1 and put the result in R0
#     "DI"       // divide R0 by R1 and put the result in R0
# So, one possible return value from pass3 given the Abstract Syntax Tree shown above from pass2 is:
#
#     [ "IM 10", "SW", "AR 0", "AD" ]
# Here is a simulator for the target machine. It takes an array of assembly instructions and an array of arguments and returns the result.
#
# #include <vector>
# #include <stack>
# #include <string>
# #include <utility>
#
# using namespace std;
#
# int simulate (const vector <string> &assembly, const vector <int> &argv) {
#   int r0 = 0, r1 = 0;
#   stack <int> istack;
#   for (auto &ins : assembly) {
#     string code = ins.substr (0, 2);
#          if (code == "IM") { r0 = stoi (ins.substr (3)); }
#     else if (code == "AR") { r0 = argv.at (stoi (ins.substr (3))); }
#     else if (code == "SW") { swap (r0, r1); }
#     else if (code == "PU") { istack.push (r0); }
#     else if (code == "PO") { r0 = istack.top (); istack.pop (); }
#     else if (code == "AD") { r0 += r1; }
#     else if (code == "SU") { r0 -= r1; }
#     else if (code == "MU") { r0 *= r1; }
#     else if (code == "DI") { r0 /= r1; }
#   }
#   return r0;
# }
# CompilersAlgorithms
# Solution
import re


class Compiler(object):

    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))

    def tokenize(self, program):
        token_iter = (
            m.group(0)
            for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program)
        )
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def pass1(self, program):
        tokens = self.tokenize(program)
        args, idx = self.parse_arguments(tokens)
        return self.tokens_to_ast(args, tokens[idx + 1:])

    def parse_arguments(self, tokens):
        if not tokens or tokens[0] != '[': raise ValueError("Invalid argument list")

        args = {}
        arg_index = 0

        for i in range(1, len(tokens)):
            if tokens[i] == ']': return args, i
            args[tokens[i]] = arg_index
            arg_index += 1

        raise ValueError("Invalid argument list")

    def equal_order(self, op1, op2):
        return (
            op1 == op2
            or (op1 in "*/" and op2 in "*/")
            or (op1 in "+-" and op2 in "+-")
        )

    def greater_order(self, op1, op2):
        return op1 in "*/" and op2 in "+-"

    def greater_or_equal(self, op1, op2):
        return self.equal_order(op1, op2) or self.greater_order(op1, op2)

    def tokens_to_ast(self, args, tokens):
        out_stack = []
        op_stack = []
        def apply_op():
            op = op_stack.pop(0)
            b = out_stack.pop()
            a = out_stack.pop()
            out_stack.append({"op": op, "a": a, "b": b})
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators and token not in ("(", ")"):
                if isinstance(token, int): out_stack.append({"op": "imm", "n": token})
                else: out_stack.append({"op": "arg", "n": args[token]})
            elif token in operators:
                while op_stack and self.greater_or_equal(op_stack[0], token): apply_op()
                op_stack.insert(0, token)
            elif token == "(": op_stack.insert(0, token)
            elif token == ")":
                while op_stack and op_stack[0] != "(": apply_op()
                op_stack.pop(0)
        while op_stack: apply_op()
        return out_stack.pop()
    def pass2(self, ast):

        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x // y,
        }

        def fold(node):
            if node["op"] in operations:
                node["a"] = fold(node["a"])
                node["b"] = fold(node["b"])

                if node["a"]["op"] == "imm" and node["b"]["op"] == "imm":
                    return {
                        "op": "imm",
                        "n": operations[node["op"]](
                            node["a"]["n"],
                            node["b"]["n"]
                        )
                    }
            return node
        return fold(ast)

    def pass3(self, ast):

        op_instr = {
            "+": "AD",
            "-": "SU",
            "*": "MU",
            "/": "DI",
        }

        def generate(node):
            if node["op"] in op_instr:
                return (
                    generate(node["a"])
                    + ["PU"]
                    + generate(node["b"])
                    + ["SW", "PO", op_instr[node["op"]]]
                )
            if node["op"] == "imm": return [f"IM {node['n']}"]
            if node["op"] == "arg": return [f"AR {node['n']}"]
            return []
        return generate(ast)