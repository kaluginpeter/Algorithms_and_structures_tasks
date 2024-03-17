lst: list = input().split()
def func(n, k, d):
    ans, top = '', int(n)
    k = int(k)
    d = int(d)
    while d > 0:
        flag = False
        if top % k == 0:
            return n + ans + '0' * d
        for i in range(10):
            if (top * 10 + i) % k == 0:
                ans += str(i)
                top = top * 10 + i
                d -= 1
                flag = True
                break
        if not flag:
            return '-1'
    return n + ans
print(func(*lst))