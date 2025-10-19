# Change every letter in a given string to the next letter in the alphabet. The function takes a single parameter s (string).
#
# Notes:
#
# Spaces and special characters should remain the same.
# Capital letters should transfer in the same way but remain capitilized.
# Examples
# "Hello"               -->  "Ifmmp"
# "What is your name?"  -->  "Xibu jt zpvs obnf?"
# "zoo"                 -->  "app"
# "zzZAaa"              -->  "aaABbb"
# StringsRegular ExpressionsFundamentals
# Solution
def next_letter(s):
    output: list[str] = []
    for ch in s:
        if not ch.isalpha(): output.append(ch)
        elif ch.islower(): output.append(chr((ord(ch) - 97 + 1) % 26 + 97))
        else: output.append(chr((ord(ch) - 65 + 1) % 26 + 65))
    return ''.join(output)