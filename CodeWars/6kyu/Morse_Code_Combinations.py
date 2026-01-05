# Terminology
# Morse code is a telecommunications method which encodes text characters as standardized sequences of two different signal durations, called dots and dashes.
# For this task, we will consider a term "word" as any sequence of symbols.
# Task
# You are given a specific amount of dashes and dots allowed your message could have. Implement a function morse_code_combinations(dashes: int, dots: int) which outputs all words which have the same number of dashed and dots as given in the input.
#
# Examples
# 1 dash, 1 dot
# →
# {
# A, N, ET, TE
# }
# 1 dash, 1 dot→{A, N, ET, TE}
# 1 dash, 2 dot
# →
# {
# R, U, D, TI, IT, NE, EN, EA, AE, ETE, EET, TEE
# }
# 1 dash, 2 dot→{R, U, D, TI, IT, NE, EN, EA, AE, ETE, EET, TEE}
# 2 dash, 1 dot
# →
# {
# G, K, W, TA, EM, NT, ME, TN, AT, TET, TTE, ETT
# }
# 2 dash, 1 dot→{G, K, W, TA, EM, NT, ME, TN, AT, TET, TTE, ETT}
# 2 dash, 2 dot
# →
# {
# P, X, Z, C, IM, MI, RT, TR, KE, ER, TU, UT, GE, EG, DT, TD, ...
# }
# 2 dash, 2 dot→{P, X, Z, C, IM, MI, RT, TR, KE, ER, TU, UT, GE, EG, DT, TD, ...}
#
# Notes
# In order to prevent hardcoded solutions, your code's limit size needs to be less than 5000 characters.
# MORSE_CODE preloaded dictionary (Morse code characters -> uppercase English letters) is given to you, for a more convenient debugging and implementation.
# Constraints
# 1
# ≤
# dashes
# ≤
# 5
# ;
#
# 1
# ≤
# dots
# ≤
# 5
# 1≤dashes≤5; 1≤dots≤5.
#
# This is the part 3 of ? Morse Code kata series:
#
# 1st kata (6 kyu) - Alternating Morse Code
# 2nd kata (6 kyu) - Recognize The Word
# 3rd kata (6 kyu) - this one.
# StringsAlgorithms
# Solution
from preloaded import MORSE_CODE

def morse_code_combinations(dashes: int, dots: int) -> set[str]:
    output: set[str] = set()
    cur_nodes: list[tuple(int, int, list[str])] = [(0, 0, [])]
    while cur_nodes:
        i, j, path = cur_nodes.pop()
        if i == dots and j == dashes:
            output.add(''.join(path))
            continue
        for code, char in MORSE_CODE.items():
            x, y = code.count('.'), code.count('-')
            if i + x > dots or j + y > dashes: continue
            path.append(char)
            cur_nodes.append((i + x, j + y, path.copy()))
            path.pop()
    return output