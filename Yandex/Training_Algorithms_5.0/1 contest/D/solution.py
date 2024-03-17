lst: list = [[i for i in input() if i in {'*', 'R', 'B'}] for j in range(8)]
mtrx: list = [[True if i == '*' else False for i in j] for j in lst]
b_rows, b_col = 0, 0
r_rows, r_col = 0, 0
for i in range(len(lst)):
    for j in range(len(lst[0])):
        if lst[i][j] == 'R':
            if i - 1 >= 0:
                 up = i - 1
                 while up >= 0:
                     if lst[up][j] != '*':
                         break
                     mtrx[up][j] = False
                     up -= 1
            if i + 1 <= 8:
                down = i + 1
                while down < 8:
                    if lst[down][j] != '*':
                        break
                    mtrx[down][j] = False
                    down += 1
            if j - 1 >= 0:
                left = j - 1
                while left >= 0:
                    if lst[i][left] != '*':
                        break
                    mtrx[i][left] = False
                    left -= 1
            if j + 1 <= 8:
                right = j + 1
                while right < 8:
                    if lst[i][right] != '*':
                        break
                    mtrx[i][right] = False
                    right += 1
        elif lst[i][j] == 'B':
            if i - 1 >= 0 and j - 1 >= 0:
                 up, left = i - 1, j - 1
                 while up >= 0 and left >= 0:
                     if lst[up][left] != '*':
                         break
                     mtrx[up][left] = False
                     up -= 1
                     left -= 1
            if i + 1 <= 8 and j + 1 <= 8:
                 up, left = i + 1, j + 1
                 while up < 8 and left < 8:
                     if lst[up][left] != '*':
                         break
                     mtrx[up][left] = False
                     up += 1
                     left += 1
            if i - 1 >= 0 and j + 1 <= 8:
                 up, left = i - 1, j + 1
                 while up >= 0 and left < 8:
                     if lst[up][left] != '*':
                         break
                     mtrx[up][left] = False
                     up -= 1
                     left += 1
            if i + 1 <= 8 and j - 1 >= 0:
                 up, left = i + 1, j - 1
                 while up < 8 and left >= 0:
                     if lst[up][left] != '*':
                         break
                     mtrx[up][left] = False
                     up += 1
                     left -= 1
count: int = 0
for i in mtrx:
    for j in i:
        count += j
print(count)