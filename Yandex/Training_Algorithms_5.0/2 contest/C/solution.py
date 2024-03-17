n: int = int(input())
lst: list = list(map(int, input().split()))
mx: int = max(lst)
total: int = sum(lst)
if mx - (total - mx) > 0:
    print(mx - (total - mx))
else:
    print(total)