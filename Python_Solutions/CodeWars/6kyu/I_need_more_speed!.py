# Write a function that will take in any array and reverse it.
#
# Sounds simple doesn't it?
#
# NOTES:
#
# Array should be reversed in place! (no need to return it)
# Usual builtins have been deactivated. Don't count on them.
# You'll have to do it fast enough, so think about performances
# ARRAYSALGORITHMS
# Solution
def reverse(seq):
    l = list()
    for _ in range(len(seq)): l.append(seq.pop())
    seq.extend(l)