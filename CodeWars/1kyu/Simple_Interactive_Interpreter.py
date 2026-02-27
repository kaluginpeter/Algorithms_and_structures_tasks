# Task
# You will create an interpreter which takes inputs described below and produces outputs, storing state in between each input.
#
# If you're not sure where to start with this kata, check out my Simpler Interactive Interpreter kata, which greatly simplifies the interpreter by removing functions.
#
# Note that the eval command has been disabled.
#
# Concepts
# The interpreter will take inputs in the language described under the language header below. This section will give an overview of the language constructs.
#
# Variables
# Any identifier which is not a keyword or a function name will be treated as a variable. If the identifier is on the left hand side of an assignment operator, the result of the right hand side will be stored in the variable. If a variable occurs as part of an expression, the value held in the variable will be substituted when the expression is evaluated.
#
# Variables are implicitly declared the first time they are assigned to.
#
# Example: Initializing a variable to a constant value and using the variable in another expression (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)
#
# >x = 7
#     7
# >x + 6
#     13
# Referencing a non-existent variable will cause the interpreter to throw an error. The interpreter should be able to continue accepting input even after throwing.
#
# Example: Referencing a non-existent variable
#
# >y + 7
#     ERROR: Invalid identifier. No variable with name 'y' was found."
# Assignments
# An assignment is an expression that has an identifier on left side of an = operator, and any expression on the right. Such expressions should store the value of the right hand side in the specified variable and return the result.
#
# Example: Assigning a constant to a variable
#
# x = 7
#     7
# You should also be able to chain and nest assignments. Note that the assignment operator is one of the few that is right associative.
#
# Example: Chained assignments. The statement below should set both x and y to 7.
#
# x = y = 7
#     7
# Example: Nested assignments. The statement below should set y to 3, but it only outputs the final result.
#
# x = 13 + (y = 3)
#     16
# Operator Precedence
# Operator precedence will follow the common order. There is a table in the Language section below that explicitly states the operators and their relative precedence.
#
# Functions
# Functions are declared by the fn keyword followed by a name, an optional arguments list, the => operator, and finally an expression. All function variables are local to the function. That is, the only variable names allowed in the function body are those declared by the arguments list. If a function has an argument called 'x', and there is also a global variable called 'x', the function should use the value of the supplied argument, not the value of the global variable, when evaluating the expression. References to variables not found in the argument list should result in an error when the function is defined.
#
# Example: declare a function to calculate the average of two variables and call it. (Each line starting with a '>' indicates a separate call to the input method of the interpreter, other lines represent output)
#
# >fn avg => (x + y) / 2
#     ERROR: Unknown identifier 'x'
# >fn avg x y => (x + y) / 2
# >a = 2
#     2
# >b = 4
#     4
# >avg a b
#     3
# Example: declare a function with an invalid variable name in the function body
#
# >fn add x y => x + z
#     ERROR: Invalid identifier 'z' in function body.
# Example: chain method calls (hint: function calls are right associative!)
#
# >fn echo x => x
# >fn add x y => x + y
# >add echo 4 echo 3
#     7
# Name conflicts
# Because variable and function names share the same grammar, conflicts are possible. Precedence will be given to the first object declared. That is, if a variable is declared, then subsequent declaration of a function with the same name should result in an error. Likewise, declaration of a function followed by the initialization of a variable with the same name should result in an error.
#
# Declaration of function with the same name as an existing function should overwrite the old function with the new one.
#
# Example: Overwriting a function
#
# >fn inc x => x + 1
# >a = 0
#     0
# >a = inc a
#     1
# >fn inc x => x + 2
# >a = inc a
#     3
# Input
# Input will conform to either the function production or the expression production in the grammar below.
#
# Output
# Output for a valid function declaration will be an empty string (null in Java).
# Output for a valid expression will be the result of the expression.
# Output for input consisting entirely of whitespace will be an empty string (null in Java).
# All other cases will throw an error.
# -- In Haskell that is:
# Right (Nothing, Interpreter)
# Right (Just Double, Interpreter)
# Right (Nothing, Interpreter)
# Left String
# Language
# Grammar
# This section specifies the grammar for the interpreter language in EBNF syntax
#
# function        ::= fn-keyword fn-name { identifier } fn-operator expression
# fn-name         ::= identifier
# fn-operator     ::= '=>'
# fn-keyword      ::= 'fn'
#
# expression      ::= factor | expression operator expression
# factor          ::= number | identifier | assignment | '(' expression ')' | function-call
# assignment      ::= identifier '=' expression
# function-call   ::= fn-name { expression }
#
# operator        ::= '+' | '-' | '*' | '/' | '%'
#
# identifier      ::= letter | '_' { identifier-char }
# identifier-char ::= '_' | letter | digit
#
# number          ::= { digit } [ '.' digit { digit } ]
#
# letter          ::= 'a' | 'b' | ... | 'y' | 'z' | 'A' | 'B' | ... | 'Y' | 'Z'
# digit           ::= '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
# Operator Precedence
# The following table lists the language's operators grouped in order of precedence. Operators within each group have equal precedence.
#
# Category	Operators
# Multiplicative	*, /, %
# Additive	+, -
# Assignment	=
# Function	=>
# Division
# You should use float division instead of integer division.
#
# InterpretersAlgorithms
# Solution
import re
from numbers import Number
import operator as op


def tokenize(expression):
    if expression == "": return []
    regex = re.compile(r"\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


def is_number(candidate):
    regular_expression = re.compile(r"\A[-]?\d+(?:\.\d+)?\Z")
    answer = regular_expression.search(candidate)
    return bool(answer)


class Interpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.operations = {
            '+': op.add,
            '-': op.sub,
            '*': op.mul,
            '/': op.truediv,
            '%': op.mod,
            '=': self._assign_var
        }
        self.keywords = ['fn']

    def _assign_var(self, name, value):
        if name in self.functions: raise Exception('Cannot overwrite varible with function')
        self.variables[name] = value
        return value

    def input(self, expression):
        tokens = tokenize(expression)
        if not tokens: return ''
        if tokens[0] in self.keywords:
            if tokens[0] == 'fn':
                func_name = tokens[1]
                if func_name in self.variables: raise Exception('Cannot overwrite varible with function')
                assign_index = tokens.index('=>')
                params = tokens[2:assign_index]
                if len(params) != len(set(params)): raise Exception('Duplicate of parameters')
                expression = tokens[assign_index + 1:]
                for token in expression:
                    if token.isalpha() and token not in params:
                        raise Exception('Variable "{}" not declared in the function body '.format(token))
                declared_func = Function(params, expression, self)
                self.functions[func_name] = declared_func
                return ''
        else:
            value = self.evaluate_expression(tokens)
        return value

    def evaluate_expression(self, tokens):
        return self.evaluate_function(self.calculate(tokens))

    def calculate(self, expression, interpreter=None):
        if interpreter is None: interpreter = self
        output = []
        operators = []
        for token in expression:
            if is_number(token):
                try:
                    output.append(int(token))
                except ValueError:
                    output.append(float(token))
            elif token in interpreter.functions:
                operators.append(token)
            elif token in interpreter.variables:
                output.append(token)
            elif token in interpreter.operations:
                if operators and operators[-1] in interpreter.operations:
                    op1 = token
                    op2 = operators[-1]
                    while operators and op2 in interpreter.operations and (
                            (left_association(op1) and precedence(op1) <= precedence(op2)) or
                            (not left_association(op1) and precedence(op1) < precedence(op2))):
                        output.append(interpreter.operations[operators.pop()])
                        try:
                            op2 = operators[-1]
                        except IndexError:
                            break
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(' and operators[-1] in interpreter.operations:
                    output.append(interpreter.operations[operators.pop()])
                try:
                    parentesis = operators.pop()
                except IndexError:
                    raise Exception('ERROR: Mismatched parentesis')
                if operators and operators[-1] in interpreter.functions: output.append(
                    interpreter.functions[operators.pop()])
            else:
                output.append(token)
        while operators:
            if operators[-1] in interpreter.operations:
                output.append(interpreter.operations[operators.pop()])
            elif operators[-1] in interpreter.functions:
                output.append(interpreter.functions[operators.pop()])
            else:
                raise Exception('Invalid function')
        return output

    def evaluate_function(self, tokens, interpreter=None):
        if interpreter is None: interpreter = self
        if tokens is None: return ''
        output = []
        for _, token in enumerate(tokens):
            if isinstance(token, Number):
                output.append(token)
            elif isinstance(token, Function):
                try:
                    args = [interpreter.variables[output.pop()] if output[-1] in interpreter.variables else output.pop()
                            for _ in range(token.count_params)]
                except IndexError:
                    raise Exception('Error: Incorrect number of arguments in the function')
                result = token(*args)
                output.append(result)
            elif callable(token):
                right = output.pop()
                left = output.pop()
                if right in interpreter.variables: right = interpreter.variables[right]
                if isinstance(right, str): raise Exception('Error: Variable referenced before assignment')
                if left in interpreter.variables and token != interpreter.operations['=']: left = interpreter.variables[
                    left]
                result = token(left, right)
                output.append(result)
            elif isinstance(token, str):
                output.append(token)
        if len(output) > 1: raise Exception('Error: Invalid sintax')
        try:
            if output[0] in interpreter.variables:
                return interpreter.variables[output[0]]
            elif isinstance(output[0], str):
                raise Exception('Undeclared Variable')
            return output[0]
        except IndexError:
            return ''


def precedence(op):
    if op == '=':
        return 1
    elif op == '+' or op == '-':
        return 2
    elif op == '*' or op == '/' or op == '%':
        return 3
    raise Exception('{} is not a valid operator'.format(op))


def left_association(op):
    return not (op == '=')


class Function:
    def __init__(self, params, expr, interp):
        self.parameters = params
        self.expression = expr
        self.interpreter = interp
        self.count_params = len(params)

    def __call__(self, *args):
        self.interpreter.variables.update(zip(self.parameters, args))
        return self.interpreter.evaluate_function(self.interpreter.calculate(self.expression, self.interpreter),
                                                  self.interpreter)