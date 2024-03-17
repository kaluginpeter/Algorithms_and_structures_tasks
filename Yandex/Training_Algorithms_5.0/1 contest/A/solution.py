lst1: list = list(map(int, input().split()))
lst2: list = list(map(int, input().split()))

x = lst1 if lst1[0] - abs(lst1[1]) <= lst2[0] - abs(lst2[1]) else lst2
y = lst1 if x == lst2 else lst2
if x[0] + abs(x[1]) >= y[0] - abs(y[1]):
    if x[0] + abs(x[1]) <= y[0] + abs(y[1]):
        print(abs(x[0] - abs(x[1])) + abs(y[0] + abs(y[1])) + 1)
    elif x[0] + abs(x[1]) > y[0] + abs(y[1]):
        print(abs(x[1]) * 2 + 1)
else:
    print(abs(x[1]) * 2 + abs(y[1]) * 2 + 2)