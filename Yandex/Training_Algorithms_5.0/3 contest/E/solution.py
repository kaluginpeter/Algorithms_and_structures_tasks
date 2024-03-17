ht: dict = dict()
for k in range(3):
    n: int = int(input())
    lst: list = list(map(int, input().split()))
    for i in lst:
        if i not in ht:
            ht[i] = set()
        ht[i].add(k)
ans: list = list()
for i in ht:
    if len(ht[i]) > 1:
        ans.append(i)
ans.sort()
print(' '.join(str(i) for i in ans))