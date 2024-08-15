# ##The Brief Microsoft Excel provides a number of useful functions for counting, summing, and averaging values if they meet a certain criteria. Your task is to write three functions that work similarly to Excel's COUNTIF, SUMIF and AVERAGEIF functions.
#
# ##Specifications Each function will take the same two arguments:
#
# A list object containing values to be counted, summed, or averaged.
# A criteria in either an integer, float, or string
# Integer or float indicates equality
# Strings can indicate >, >=, <, <= or <> (use the Excel-style "Not equal to" operator) to a number (ex. ">=3"). In the count_if function, a string without an operater indicates equality to this string.
# The tests will all include properly formatted inputs. The test cases all avoid rounding issues associated with floats.
#
# ##Examples
#
# count_if([1,3,5,7,9], 3)
# 1
#
# count_if(["John","Steve","John"], "John")
# 2
#
# sum_if([2,4,6,-1,3,1.5],">0")
# 16.5
#
# average_if([99,95.5,0,83],"<>0")
# 92.5
# ##Excel Function Documentation:
#
# COUNTIF
# SUMIF
# AVERAGEIF
# ALGORITHMS
# Solution
from typing import Callable

funcs: dict[str, Callable] = {
    '<>': lambda item, key: item != key,
    '<=': lambda item, key: item <= key,
    '>=': lambda item, key: item >= key,
    '<': lambda item, key: item < key,
    '>': lambda item, key: item > key,
}


def is_number_regex(s: str) -> bool:
    return s.lstrip('-').replace('.', '', 1).replace('e-', '', 1).replace('e', '', 1).isdigit()


def parse(expression: str) -> tuple[Callable, str]:
    if isinstance(expression, (float, int)) or '>' not in expression and '<' not in expression:
        key = expression
        if isinstance(key, str):
            key = float(key) if is_number_regex(key) else key
        return lambda item, key: item == key, key

    for module in funcs:
        if expression.startswith(module):
            key = expression[len(module):]
            key = float(key) if is_number_regex(key) else key
            return funcs[module], key


def count_if(values, criteria):
    func, key = parse(criteria)
    return len([item for item in values if func(item, key)])


def sum_if(values, criteria):
    func, key = parse(criteria)
    return sum([item for item in values if func(item, key)])


def average_if(values, criteria):
    func, key = parse(criteria)
    objs: iter = [item for item in values if func(item, key)]
    return sum(objs) / len(objs)