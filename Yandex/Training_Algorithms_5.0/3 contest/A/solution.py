n: int = int(input())
ht: dict = dict()
for i in range(n):
    k: int = int(input())
    lst: list = input().split()
    for j in range(k):
        ht[lst[j]] = ht.get(lst[j], 0) + 1
for i in ht.copy():
    if ht[i] != n:
        del ht[i]
print(len(ht))
print(' '.join(sorted(ht.keys())))