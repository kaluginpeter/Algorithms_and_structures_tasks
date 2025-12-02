# You are given a positive natural number n (which is n > 0) and you should create a regular expression pattern which only matches the decimal representation of all positive natural numbers strictly less than n without leading zeros. The empty string, numbers with leading zeros, negative numbers and non-numbers should not match the regular expression compiled from your returned pattern.
#
# Input
# n > 0 natural number, n can be from the full possible positive range
# Output
# regular expression pattern as string which will be used to compile a regular expression to do the matches
# Tests
# The compiled regular expression will be tested against decimal representations of random numbers with and without leading zeros, strings including letters and the empty string and should only match for decimal representations of numbers k with 0 < k < n.
#
# Tests use re.match() to do the matches.
#
# Regular Expressions
# Solution
def regex_below(n):
    s = str(n)
    L = len(s)

    parts = []
    for l in range(1, L):
        if l == 1:
            parts.append(r"[1-9]")
        else:
            parts.append(r"[1-9][0-9]{%d}" % (l - 1))

    prefix_parts = []
    for i, ch in enumerate(s):
        d = int(ch)
        if d > 1:
            if i == 0:
                prefix_parts.append(f"[1-{d-1}][0-9]{{{L-i-1}}}")
            else:
                prefix_parts.append(s[:i] + f"[0-{d-1}]" + f"[0-9]{{{L-i-1}}}")
        elif d == 1:
            if i == 0:
                continue
            else:
                prefix_parts.append(s[:i] + f"[0-0]" + f"[0-9]{{{L-i-1}}}")

    parts.extend(prefix_parts)

    if not parts:
        return r"^(?!.*)^$"

    return r"^(?:%s)$" % "|".join(parts)