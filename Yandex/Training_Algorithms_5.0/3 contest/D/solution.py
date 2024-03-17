n, k = map(int, input().split())
lst: list = list(map(int, input().split()))
ht: dict = dict()
for i in range(n):
    if lst[i] in ht and i - ht[lst[i]] <= k:
        print('YES')
        break
    else:
        ht[lst[i]] = i
else:
    print('NO')