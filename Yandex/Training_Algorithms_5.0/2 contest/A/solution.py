k: int = int(input())
lst: list = [input().split() for i in range(k)]
x_min = y_min = float('inf')
x_max = y_max = float('-inf')
for i in range(k):
    if x_min > int(lst[i][0]):
        x_min = int(lst[i][0])
    if x_max < int(lst[i][0]):
        x_max = int(lst[i][0])
    if y_min > int(lst[i][1]):
        y_min = int(lst[i][1])
    if y_max < int(lst[i][1]):
        y_max = int(lst[i][1])
print(x_min, y_min, x_max, y_max)