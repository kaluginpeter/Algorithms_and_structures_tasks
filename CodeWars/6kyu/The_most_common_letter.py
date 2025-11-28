# Find the most common letter (not a space) in the given string (comprised of at least 3 lowercase words) and replace it with the given letter.
#
# If such letters are two or more, choose the one that appears earliest in the string.
#
# For example:
#
# ('my mom loves me as never did', 't') => 'ty tot loves te as never did'
# ('real talk bro', 'n') => 'neal talk bno'
# ('great job go ahead', 'k') => 'grekt job go khekd'
# FundamentalsStringsArrays
# Solution
from collections import defaultdict

def replace_common(st, letter):
    bound: int = -1
    target: str = ''
    seen: dict[str, int] = defaultdict(int)
    first: dict[str, int] = dict()
    for i in range(len(st)):
        char = st[i]
        if char not in first: first[char] = i
        if char == ' ': continue
        seen[char] += 1
        if seen[char] > bound:
            bound = seen[char]
            target = char
        elif seen[char] == bound and first[char] < first[target]:
            bound = seen[char]
            target = char
    return st.replace(target, letter)