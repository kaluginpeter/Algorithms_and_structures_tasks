# Terminology
# Morse code is a telecommunications method which encodes text characters as standardized sequences of two different signal durations, called dots and dashes.
# For this task, we will consider a term "word" as any sequence of symbols.
# Task
# You work on an emergency services organization. Whenever, there is a new task, you ask dispatcher for the instructions in Morse code. However, your dispatcher doesn't even know about the intervals between letters! Probably used ChatGPT to graduate... So his message is all compressed together and it's really hard to identify what is he saying. Implement a function possible_words(morse_str) that takes as an input a Morse code string (dots are . and dashes are -) and output a set of all possible words, the dispatcher was trying to say. All words should be in uppercase.
#
# Examples
# −
# −
# −
#
# −
# ⇒
# {
# TO, OT, MM, TTM, TMT, MTT, TTTT
# }
# −−− −⇒{TO, OT, MM, TTM, TMT, MTT, TTTT}
# ⋯
# ⋅
#
# ⇒
# {
# H, II, ES, SE, EEI, EIE, IEE, EEEE
# }
# ⋯⋅         ⇒{H, II, ES, SE, EEI, EIE, IEE, EEEE}
# −
# −
# ⋅
#
# ⋅
#
# ⇒
# {
# Z, MI, GE, TD, TTI, TNE, MEE, TTEE
# }
# −−⋅ ⋅    ⇒{Z, MI, GE, TD, TTI, TNE, MEE, TTEE}
# ⋅
# ⋅
# −
#
# −
#
# ⇒
# {
# IM, UT, EW, EAT, ITT, EEM, EETT
# }
# ⋅⋅− −    ⇒{IM, UT, EW, EAT, ITT, EEM, EETT}
# ⋱
# ⋱
#
# Notes
# MORSE_CODE preloaded dictionary (Morse code characters -> uppercase English letters) is given to you, for a more convenient debugging and implementation.
# Algorithms
# Solution
from preloaded import MORSE_CODE

def possible_words(morse_str: str) -> set[str]:
    cur_nodes: list[tuple[str, str]] = [(morse_str, "")]
    next_nodes: list[tuple[str, str]] = []
    output: set[str] = set()
    while cur_nodes:
        for node, path in cur_nodes:
            if not node:
                output.add(path)
                continue
            for p in MORSE_CODE:
                if node.startswith(p):
                    next_nodes.append((node[len(p):], path + MORSE_CODE[p]))
        cur_nodes = next_nodes
        next_nodes = []
    return output