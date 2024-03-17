n: int = int(input())
lst: list = list(map(int, input().split()))
ht: dict = dict()
for i in lst:
    ht[i] = ht.get(i, 0) + 1
mx: int = 0
for i in ht:
    mx = max(mx, ht[i] + ht.get(i + 1, 0))
print(n - mx)