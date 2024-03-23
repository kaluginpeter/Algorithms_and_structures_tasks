reader = open('input.txt', 'r')
mtrx: list = [list(map(int, i[:-1].split())) for i in reader.readlines() if i.endswith('\n')]
reader.close()
n, m = mtrx.pop(0)[:]
first_max_on_rows_rows, first_max_on_rows_columns = 0, 0
for i in range(n):
    for j in range(m):
        if mtrx[i][j] > mtrx[first_max_on_rows_rows][first_max_on_rows_columns]:
            first_max_on_rows_rows, first_max_on_rows_columns = i, j
second_max_on_rows_rows, second_max_on_rows_columns = None, None
for i in range(n):
    if i == first_max_on_rows_rows:
        continue
    for j in range(m):
        if second_max_on_rows_rows is None:
            second_max_on_rows_rows, second_max_on_rows_columns = i, j
        elif mtrx[i][j] > mtrx[second_max_on_rows_rows][second_max_on_rows_columns]:
            second_max_on_rows_rows, second_max_on_rows_columns = i, j
least_max_for_first_max_rows, least_max_for_first_max_columns = None, None
for i in range(n):
    if i == first_max_on_rows_rows:
        continue
    for j in range(m):
        if j == second_max_on_rows_columns:
            continue
        elif least_max_for_first_max_rows is None:
            least_max_for_first_max_rows, least_max_for_first_max_columns = i, j
        elif mtrx[i][j] > mtrx[least_max_for_first_max_rows][least_max_for_first_max_columns]:
            least_max_for_first_max_rows, least_max_for_first_max_columns = i, j

first_max_on_columns_rows, first_max_on_columns_columns = 0, 0
for i in range(n):
    for j in range(m):
        if mtrx[i][j] > mtrx[first_max_on_columns_rows][first_max_on_columns_columns]:
            first_max_on_columns_rows, first_max_on_columns_columns = i, j
second_max_on_columns_rows, second_max_on_columns_columns = None, None
for i in range(n):
    for j in range(m):
        if j == first_max_on_columns_columns:
            continue
        elif second_max_on_columns_rows is None:
            second_max_on_columns_rows, second_max_on_columns_columns = i, j
        elif mtrx[i][j] > mtrx[second_max_on_columns_rows][second_max_on_columns_columns]:
            second_max_on_columns_rows, second_max_on_columns_columns = i, j
least_max_for_second_max_rows, least_max_for_second_max_columns = None, None
for i in range(n):
    if i == second_max_on_columns_rows:
        continue
    for j in range(m):
        if j == first_max_on_columns_columns:
            continue
        elif least_max_for_second_max_rows is None:
            least_max_for_second_max_rows, least_max_for_second_max_columns = i, j
        elif mtrx[i][j] > mtrx[least_max_for_second_max_rows][least_max_for_second_max_columns]:
            least_max_for_second_max_rows, least_max_for_second_max_columns = i, j
if mtrx[least_max_for_first_max_rows][least_max_for_first_max_columns] <= mtrx[least_max_for_second_max_rows][least_max_for_second_max_columns]:
    print(first_max_on_rows_rows + 1, second_max_on_rows_columns + 1)
else:
    print(second_max_on_columns_rows + 1, first_max_on_columns_columns + 1)