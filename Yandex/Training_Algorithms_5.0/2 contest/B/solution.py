n, k = map(int, input().split())
lst: list = list(map(int, input().split()))
ans: int = 0
for i in range(n):
    for j in range(i+1, min(n, i + k + 1)):
        ans = max(ans, lst[j] - lst[i])
print(ans)