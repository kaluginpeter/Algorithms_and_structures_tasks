t: int = int(input())
for i in range(t):
    n: int = int(input())
    lst: list = list(map(int, input().split()))
    ans: list = list()
    ln = 1
    min_in_ln = lst[0]
    for i in range(1, n):
        if lst[i] < ln + 1:
            ans.append(ln)
            ln, min_in_ln = 1, lst[i]
        elif min_in_ln < ln + 1:
            ans.append(ln)
            ln, min_in_ln = 1, lst[i]
        else:
            ln += 1
        min_in_ln = min(min_in_ln, lst[i])
    ans.append(ln)
    print(len(ans))
    print(' '.join(str(k) for k in ans))