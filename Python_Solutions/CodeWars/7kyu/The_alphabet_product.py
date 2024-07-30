# I have four positive integers, A, B, C and D, where A < B < C < D. The input is a list of the integers A, B, C, D, AxB, BxC, CxD, DxA in some order. Your task is to return the value of D.
#
# LOGIC
# Solution
def alphabet(ns):
    ns.sort()
    a, b = ns[:2]
    ans: list[int] = []
    first: bool = False
    second: bool = False
    for idx in range(2, len(ns)):
        if not first and  a * b == ns[idx]:
            first = True
            continue
        if not second and ns[idx] % b == 0 and ns[idx] // b > b:
            second = True
            continue
        else: ans.append(ns[idx])
        if len(ans) == 2: break
    return ans[-1]