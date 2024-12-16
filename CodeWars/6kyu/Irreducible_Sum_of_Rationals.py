# You will have a list of rationals in the form
#
# lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]
# or
#
# lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]
# where all numbers are positive integers. You have to produce their sum N / D in an irreducible form: this means that N and D have only 1 as a common divisor.
#
# Return the result in the form:
#
# [N, D] in Ruby, Crystal, Python, Clojure, JS, CS, PHP, Julia, Pascal
# Just "N D" in Haskell, PureScript
# "[N, D]" in Java, CSharp, TS, Scala, PowerShell, Kotlin
# "N/D" in Go, Nim
# {N, D} in C, C++, Elixir, Lua
# Some((N, D)) in Rust
# Some "N D" in F#, Ocaml
# c(N, D) in R
# (N, D) in Swift
# '(N D) in Racket
# If the result is an integer (D evenly divides N) return:
#
# an integer in Ruby, Crystal, Elixir, Clojure, Python, JS, CS, PHP, R, Julia
# Just "n" (Haskell, PureScript)
# "n" Java, CSharp, TS, Scala, PowerShell, Go, Nim, Kotlin
# {n, 1} in C, C++, Lua
# Some((n, 1)) in Rust
# Some "n" in F#, Ocaml,
# (n, 1) in Swift
# n in Racket
# (n, 1) in Swift, Pascal, Perl
# If the input list is empty, return
#
# nil/None/null/Nothing
# {0, 1} in C, C++, Lua
# "0" in Scala, PowerShell, Go, Nim
# O in Racket
# "" in Kotlin
# [0, 1] in C++, "[0, 1]" in Pascal
# [0, 1] in Perl
# Example:
# [ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]
# 1/2  +  1/3  +  1/4     =      13/12
# Note
# See sample tests for more examples and form of results.
# Fundamentals
# Solution
import math
def simplify(x: int, y: int) -> list[int, int]:
    has_move: bool = True
    while has_move:
        has_move = False
        for mod in range(2, 103):
            if x % mod == 0 and y % mod == 0:
                x //= mod
                y //= mod
                has_move = True
                break
    return [x, y] if y != 1 else x
def sum_fractions(fractions: list[list[int, int]]) -> tuple[int, int]:
    lcm: int = math.lcm(*[denom for numer, denom in fractions])
    numerator: int = 0
    for num, denom in fractions:
        numerator += num * (lcm // denom)
    return (numerator, lcm)
def sum_fracts(lst):
    if not lst: return None
    numerator, denominator = sum_fractions(lst)
    return simplify(numerator, denominator)