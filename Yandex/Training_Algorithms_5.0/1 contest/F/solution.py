n: int = int(input())
arr: list = list(map(int, input().split()))
ans: list = list()
odd: bool = arr[0] % 2 != 0
for i in range(1, n):
    if arr[i] % 2 != 0:
        if odd:
            ans.append('x')
        else:
            odd = True
            ans.append('+')
    else:
        ans.append('+')
print(''.join(ans))