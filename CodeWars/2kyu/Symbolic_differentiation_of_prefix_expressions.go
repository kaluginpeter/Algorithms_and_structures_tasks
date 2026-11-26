/*
In this kata your task is to differentiate a mathematical expression given as a string in prefix notation. The result should be the derivative of the expression returned in prefix notation.

To simplify things we will use a simple list format made up of parentesis and spaces.

The expression format is (func arg1) or (op arg1 arg2) where op means operator, func means function and arg1, arg2 are aguments to the operator or function. For example (+ x 1) or (cos x)

The expressions will always have balanced parentesis and with spaces between list items.

Expression operators, functions and arguments will all be lowercase.

Expressions are single variable expressions using x as the variable.

Expressions can have nested arguments at any depth for example (+ (* 1 x) (* 2 (+ x 1)))

Examples of prefix notation in this format:

(+ x 2)        // prefix notation version of x+2

(* (+ x 3) 5)  // same as 5 * (x + 3)

(cos (+ x 1))  // same as cos(x+1)

(^ x 2)        // same as x^2 meaning x raised to power of 2
The operators and functions you are required to implement are + - * / ^ cos sin tan exp ln where ^ means raised to power of. exp is the exponential function (same as e^x) and ln is the natural logarithm (base e).

Example of input values and their derivatives:

(* 1 x) => 1

(^ x 3) => (* 3 (^ x 2))

(cos x) => (* -1 (sin x))
In addition to returning the derivative your solution must also do some simplifications of the result but only what is specified below.

The returned expression should not have unecessary 0 or 1 factors. For example it should not return (* 1 (+ x 1)) but simply the term (+ x 1) similarly it should not return (* 0 (+ x 1)) instead it should return just 0

Results with two constant values such as for example (+ 2 2) should be evaluated and returned as a single value 4

Any argument raised to the zero power should return 1 and if raised to 1 should return the same value or variable. For example (^ x 0) should return 1 and (^ x 1) should return x

No simplifications are expected for functions like cos, sin, exp, ln... (but their arguments might require a simplification).

Think recursively and build your answer according to the rules of derivation and sample test cases.

If you need to diff any test expressions you can use Wolfram Alpha however remember we use prefix format in this kata.

Best of luck !

Algorithms
*/
// Solution
package kata

import (
	"math"
	"strconv"
	"strings"
)

type node struct {
	op   string 
	val  float64
	args []*node
}

func num(v float64) *node { return &node{op: "num", val: v} }

func (n *node) isNum() bool       { return n.op == "num" }
func (n *node) is(v float64) bool { return n.op == "num" && n.val == v }

func (n *node) String() string {
	switch n.op {
	case "num":
		v := n.val
		if v == 0 {
			v = 0
		}
		return strconv.FormatFloat(v, 'f', -1, 64)
	case "x":
		return "x"
	}
	parts := []string{n.op}
	for _, a := range n.args {
		parts = append(parts, a.String())
	}
	return "(" + strings.Join(parts, " ") + ")"
}


func tokenize(s string) []string {
	s = strings.ReplaceAll(s, "(", " ( ")
	s = strings.ReplaceAll(s, ")", " ) ")
	return strings.Fields(s)
}

func parse(tokens []string, pos *int) *node {
	t := tokens[*pos]
	*pos++
	if t != "(" {
		if t == "x" {
			return &node{op: "x"}
		}
		v, _ := strconv.ParseFloat(t, 64)
		return num(v)
	}
	op := tokens[*pos]
	*pos++
	n := &node{op: op}
	for tokens[*pos] != ")" {
		n.args = append(n.args, parse(tokens, pos))
	}
	*pos++ 
	return n
}

func add(a, b *node) *node {
	switch {
	case a.isNum() && b.isNum():
		return num(a.val + b.val)
	case a.is(0):
		return b
	case b.is(0):
		return a
	}
	return &node{op: "+", args: []*node{a, b}}
}

func sub(a, b *node) *node {
	switch {
	case a.isNum() && b.isNum():
		return num(a.val - b.val)
	case b.is(0):
		return a
	}
	return &node{op: "-", args: []*node{a, b}}
}

func mul(a, b *node) *node {
	switch {
	case a.isNum() && b.isNum():
		return num(a.val * b.val)
	case a.is(0) || b.is(0):
		return num(0)
	case a.is(1):
		return b
	case b.is(1):
		return a
	}
	return &node{op: "*", args: []*node{a, b}}
}

func div(a, b *node) *node {
	switch {
	case a.isNum() && b.isNum():
		return num(a.val / b.val)
	case a.is(0):
		return num(0)
	case b.is(1):
		return a
	}
	return &node{op: "/", args: []*node{a, b}}
}

func pow(a, b *node) *node {
	switch {
	case b.is(0):
		return num(1)
	case b.is(1):
		return a
	case a.isNum() && b.isNum():
		return num(math.Pow(a.val, b.val))
	}
	return &node{op: "^", args: []*node{a, b}}
}

func fn(name string, a *node) *node { return &node{op: name, args: []*node{a}} }

func diff(n *node) *node {
	switch n.op {
	case "num":
		return num(0)
	case "x":
		return num(1)
	}

	a := n.args[0]
	da := diff(a)

	switch n.op {
	case "+":
		return add(da, diff(n.args[1]))
	case "-":
		return sub(da, diff(n.args[1]))
	case "*": 
		b := n.args[1]
		return add(mul(da, b), mul(a, diff(b)))
	case "/": 
		b := n.args[1]
		return div(sub(mul(da, b), mul(a, diff(b))), pow(b, num(2)))
	case "^":
		b := n.args[1]
		if b.isNum() {
			return mul(mul(b, pow(a, num(b.val-1))), da)
		}
		db := diff(b)
		return mul(n, add(mul(db, fn("ln", a)), div(mul(b, da), a)))
	}

	var outer *node
	switch n.op {
	case "sin":
		outer = fn("cos", a)
	case "cos":
		outer = mul(num(-1), fn("sin", a))
	case "tan":
		outer = add(num(1), pow(fn("tan", a), num(2)))
	case "exp":
		outer = fn("exp", a)
	case "ln":
		outer = div(num(1), a)
	}
	return mul(da, outer)
}

func Diff(expression string) string {
	tokens := tokenize(expression)
	pos := 0
	return diff(parse(tokens, &pos)).String()
}