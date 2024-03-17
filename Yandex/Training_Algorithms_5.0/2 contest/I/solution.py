n: int = int(input())
moves: set = set()
lst: list = list()
dop_moves: int = 0
pos: list = list([0] * n)
for i in range(n):
    x, y = map(int, input().split())
    pos[x - 1] += 1
    lst.append([x, y])
for i in range(n):
    while pos[i] > 1:
        x: int = pos.index(0)
        dop_moves += abs(i - x)
        pos[x], pos[i] = 1, pos[i] - 1
mn: int = float('inf')
for i in range(1, n + 1):
    top: int = 0
    for j in lst:
        top += abs(i - j[1])
    mn = min(mn, top)
print(mn + dop_moves)