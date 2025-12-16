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