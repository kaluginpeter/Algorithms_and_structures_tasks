# Wikipedia: The Baum–Sweet sequence is an infinite automatic sequence of 0s and 1s defined by the rule:
#
# bn = 1 if the binary representation of n contains no block of consecutive 0s of odd length;
# bn = 0 otherwise;
#
# for n ≥ 0.
#
# Define a generator function baum_sweet that sequentially generates the values of this sequence.
#
# It will be tested for up to 1 000 000 values.
#
# Note that the binary representation of 0 used here is not 0 but the empty string ( which does not contain any blocks of consecutive 0s ).
#
# Algorithms
# Solution
def check(i: int) -> bool:
    if not i: return True
    left: int = 0
    b_i: str = bin(i)[2:]
    for right in range(len(b_i)):
        if b_i[right] == '1':
            if right - left & 1: return False
            left = right + 1
    if len(b_i) - left & 1: return False
    return True

def baum_sweet():
    i: int = 0
    while True:
        yield (1 if check(i) else 0)
        i += 1