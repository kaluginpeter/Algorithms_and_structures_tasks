# Maxie is the largest number that can be obtained by swapping two digits of an integer, Minnie is the smallest number. Create a function that takes an integer and returns Maxie and Minnie. Leading zeroes are not permitted. All test cases are positive integers of three digits or more. Sometimes no swaps are needed.
#
# Examples:
# swap(12340) → (42310,10342)
# swap(98761) → (98761,18769)>>No swap needed for Maxie.
# swap(9000) → (9000,9000)>>No swaps allowed.
# swap(90888) → (98880,80889)
# PuzzlesMathematics
# Solution
def get_max(x: int) -> int:
    s: list[str] = list(str(x))
    last: list[int] = [-1] * 10
    for i, c in enumerate(s): last[int(c)] = i
    for i, c in enumerate(s):
        cur: int = int(c)
        for d in range(9, cur, -1):
            if last[d] > i:
                j: int = last[d]
                s[i], s[j] = s[j], s[i]
                return int(''.join(s))
    return x

def get_min(x: int) -> int:
    s: list[str] = list(str(x))
    last: list[int] = [-1] * 10
    for i, c in enumerate(s): last[int(c)] = i
    for i, c in enumerate(s):
        cur: int = int(c)
        start: int = 1 if i == 0 else 0
        for d in range(start, cur):
            if last[d] > i:
                j: int = last[d]
                s[i], s[j] = s[j], s[i]
                return int(''.join(s))
    return x

def swap(number):
    return (get_max(number), get_min(number))
