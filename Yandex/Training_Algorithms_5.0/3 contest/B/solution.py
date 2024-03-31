st1, st2 = input(), input()
ht1: dict = dict()
ht2: dict = dict()
for i in st1:
    ht1[i] = ht1.get(i, 0) + 1
for i in st2:
    ht2[i] = ht2.get(i, 0) + 1
print('YES' if ht1 == ht2 else 'NO')