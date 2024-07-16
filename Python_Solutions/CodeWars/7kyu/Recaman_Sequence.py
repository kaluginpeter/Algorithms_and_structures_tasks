# Return the nth term of the Recamán's sequence.
#
# a(0) = 0;
#
#         a(n-1) - n, if this value is positive and not yet in the sequence
#       /
# a(n) <
#       \
#         a(n-1) + n, otherwise
# input range: 0 – 30 000
#
# Numberphile video about Recamán's sequence
#
# ALGORITHMSPERFORMANCE
# Solution
def recaman(n):
    sequence = [0]
    seen = {0}

    for i in range(1, n + 1):
        previous = sequence[-1]
        potential = previous - i

        if potential > 0 and potential not in seen:
            sequence.append(potential)
            seen.add(potential)
        else:
            sequence.append(previous + i)
            seen.add(previous + i)

    return sequence[n]