hs: set = set(input().split())
lst: list = input().split()
ans: list = list()
for i in lst:
    for j in range(len(i)):
        if i[:j] in hs:
            ans.append(i[:j])
            break
    else:
        ans.append(i)
print(' '.join(ans))