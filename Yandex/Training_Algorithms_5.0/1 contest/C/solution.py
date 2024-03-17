n: int = int(input())
lst: list = [int(input()) for i in range(n)]
count: int = 0
for i in range(n):
    x: int = lst[i]
    count += x // 4
    x %= 4
    if x == 3:
        count += 2
        continue
    elif x > 0:
        count += x
print(count)