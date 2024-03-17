n = int(input())
lst = list(map(int, input().split()))
a, b, k = map(int, input().split())
top: int = None
mx: int = max(lst)
start = max(a // k - (1 if a % k == 0 else 0), 0)
end = b // k + (1 if b % k != 0 else 0)
for i in range(start, end):
    if top is None:
        top = max(lst[i % n], lst[-i % n])
    else:
        top = max(top, lst[i % n], lst[-i % n])
    if top == mx:
        break
print(top if top is not None else lst[0])