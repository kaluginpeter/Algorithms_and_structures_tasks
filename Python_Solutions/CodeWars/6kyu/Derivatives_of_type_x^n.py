# You are provided with a function of the form f(x) = axⁿ,
# that consists of a single term only and 'a' and 'n' are integers, e.g f(x) = 3x², f(x) = 5 etc.
#
# Your task is to create a function that takes f(x) as the argument and returns
# the result of differentiating the function, that is, the derivative.
#
# If
# �
# (
# �
# )
# =
# �
# �
# �
# f(x)=ax
# n
#  , then
# �
# ′
# (
# �
# )
# =
# �
# �
# �
# �
# −
# 1
# f
# ′
#  (x)=nax
# n−1
#
#
# Input is a string, for example "5x^4". The function f(x) consists of a single term only. Variable is denoted by x.
# Output should be a string, for example "20x^3".
#
# Examples
# "3x^2"  => "6x"
# "-5x^3" => "-15x^2"
# "6x^-2" => "-12x^-3"
# "5x"    => "5"
# "-x"    => "-1"
# "42"    => "0"
# MATHEMATICS
# Solution
def differentiate(x):
    if 'x' not in x: return '0'
    a, n = x.split('x', 2)
    a = 1 if a == '' else -1 if a == '-' else int(a)
    return f"{a}" if n == '' else f"{2*a}x" if n == "^2" else f"{a*int(n[1:])}x^{int(n[1:])-1}"