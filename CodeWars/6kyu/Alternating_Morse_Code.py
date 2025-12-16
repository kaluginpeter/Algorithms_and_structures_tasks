# Terminology
# Morse code is a telecommunications method which encodes text characters as standardized sequences of two different signal durations, called dots and dashes.
# For this task, we will consider a term "word" as any sequence of symbols.
# Heterogram is a word, where each letter occurs only once.
# Task
# Implement a function alternating_morse_code(letter), which takes as an input an English uppercase letter and outputs a set of all heterograms starting with letter, such that, in their Morse code encoding, the dots and dashes alternate (
# −
# ⋅
# −
# ⋅
# −
# ⋅
# …
#  or
# ⋅
# −
# ⋅
# −
# ⋅
# −
# …
# −⋅−⋅−⋅… or ⋅−⋅−⋅−…), if you ignore the spaces between letters. All words should be in the uppercase.
#
# Few examples of such words
# ART
# ⇒
# ⋅
# −
#
# ⋅
# −
# ⋅
#
# −
# ART            ⇒⋅−  ⋅−⋅  −
# TEN
# ⇒
# −
#
# ⋅
#
# −
#
# ⋅
# TEN            ⇒−  ⋅  − ⋅
# KARTECN
# ⇒
# −
# ⋅
# −
#
# ⋅
# −
#
# ⋅
# −
# ⋅
#
# −
#
# ⋅
#
# −
# ⋅
# −
# ⋅
#
# −
#
# ⋅
# KARTECN⇒−⋅−  ⋅−  ⋅−⋅  −  ⋅  −⋅−⋅  − ⋅
# ⋱
# ⋱
#
# Notes
# In order to prevent hardcoded solutions, your code's limit size needs to be less than 5000 characters.
# MORSE_CODE preloaded dictionary is given to you, for a more convenient debugging.
# AlgorithmsRecursion
# Solution
from preloaded import MORSE_CODE

def alternating_morse_code(letter: str) -> set[str]:
    output: set[str] = set()
    if '--' in MORSE_CODE[letter] or '..' in MORSE_CODE[letter]: return output
    cur_nodes: list[tuple[str, str]] = [(letter, MORSE_CODE[letter])]
    next_nodes: list[tuple[str, str]] = []
    while cur_nodes:
        for node, path in cur_nodes:
            output.add(node)
            for ch, seq in MORSE_CODE.items():
                if path[-1] != seq[0] and '--' not in seq and '..' not in seq and ch not in node:
                    next_nodes.append((node + ch, path + seq))
        cur_nodes = next_nodes
        next_nodes = []
    return output