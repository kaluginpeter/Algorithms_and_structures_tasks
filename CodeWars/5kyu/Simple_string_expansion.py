# Consider the following expansion:
#
# "3(ab)"     expands to "ababab"    -- because "ab" repeats 3 times
# "2(a3(b))"  expands to "abbbabbb"  -- "a3(b)" expands to "abbb" and that repeats twice
# Given a string, return the expansion of that string.
#
# Rules:
#
# The input is guaranteed to be well-formed and balanced.
# Multipliers are single digits in the range 1–9, and are optional.
# Every multiplier is immediately followed by a parenthesised group.
# After a group is fully expanded, nothing appears beyond the final closing parenthesis.
# Lowercase letters and digits are the only characters that appear.
#
# Algorithms