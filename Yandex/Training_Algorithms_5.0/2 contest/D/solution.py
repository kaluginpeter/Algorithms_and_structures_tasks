n: int = int(input())
lst: list = [input().split() for i in range(n)]
mtrx: list = list()
for i in range(8):
    mtrx.append([False] * 8)
for i in lst:
    mtrx[int(i[0])-1][int(i[1])-1] = True
count: int = 0
for i in range(8):
    for j in range(8):
        if mtrx[i][j]:
            if i - 1 < 0 or not mtrx[i-1][j]:
                count += 1
            if i + 1 >= 8 or not mtrx[i+1][j]:
                count += 1
            if j - 1 < 0 or not mtrx[i][j-1]:
                count += 1
            if j + 1 >= 8 or not mtrx[i][j+1]:
                count += 1
print(count)