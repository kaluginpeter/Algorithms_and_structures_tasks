n: int = int(input())
lst: list = [list(map(int, input().split())) for i in range(n)]
ans: list = list()
positive_mx_b = None
positive_mn_b = None
negative_mx_a = None
total: int = 0
bad: list = list()
if len(lst) == 1:
    print(lst[0][0])
    print(1)
else:
    for i in range(n):
        if lst[i][0] - lst[i][1] >= 0:
            if positive_mx_b is None or lst[positive_mx_b][1] < lst[i][1]:
                if positive_mx_b is not None and (not positive_mn_b or lst[positive_mn_b][1] > lst[positive_mx_b][1]):
                    if positive_mn_b is not None:
                        ans.append(positive_mn_b + 1)
                        total += lst[positive_mn_b][0] - lst[positive_mn_b][1]
                    positive_mn_b = positive_mx_b
                elif positive_mx_b is not None:
                    total += lst[positive_mx_b][0] - lst[positive_mx_b][1]
                    ans.append(positive_mx_b + 1)
                positive_mx_b = i
            elif positive_mn_b is None or lst[positive_mn_b][1] > lst[i][1]:
                if positive_mn_b is not None:
                    total += lst[positive_mn_b][0] - lst[positive_mn_b][1]
                    ans.append(positive_mn_b + 1)
                positive_mn_b = i
            else:
                total += lst[i][0] - lst[i][1]
                ans.append(i + 1)
        else:
            if negative_mx_a is None or lst[negative_mx_a][0] < lst[i][0]:
                if negative_mx_a is not None:
                    bad.append(negative_mx_a + 1)
                negative_mx_a = i
            else:
                bad.append(i + 1)
    if negative_mx_a is None:
        total += lst[positive_mn_b][0] - lst[positive_mn_b][1] + lst[positive_mx_b][0]
        print(total)
        print(' '.join(str(i) for i in ans + [positive_mn_b + 1, positive_mx_b + 1]))
    elif positive_mx_b is None:
        print(total + lst[negative_mx_a][0])
        print(' '.join(str(i) for i in ans + [negative_mx_a + 1] + bad))
    elif positive_mn_b is None:
        if lst[positive_mx_b][0] > lst[positive_mx_b][0] - lst[positive_mx_b][1] + lst[negative_mx_a][0]:
            total += lst[positive_mx_b][0]
        else:
            total += lst[positive_mx_b][0] - lst[positive_mx_b][1] + lst[negative_mx_a][0]
        print(total)
        print(' '.join(str(i) for i in ans + [positive_mx_b + 1, + negative_mx_a + 1] + bad))
    else:
        if lst[positive_mx_b][1] > lst[positive_mx_b][0] - lst[positive_mx_b][1] + lst[negative_mx_a][0]:
            total += lst[positive_mn_b][0] - lst[positive_mn_b][1] + lst[positive_mx_b][0]
            print(total)
            print(' '.join(str(i) for i in ans + [positive_mn_b + 1, positive_mx_b + 1, negative_mx_a + 1] + bad))
        else:
            if lst[negative_mx_a][0] > lst[positive_mx_b][1]:
                total += lst[positive_mn_b][0] - lst[positive_mn_b][1]
                total += lst[positive_mx_b][0] - lst[positive_mx_b][1]
                total += lst[negative_mx_a][0]
                print(total)
            else:
                total += lst[positive_mn_b][0] - lst[positive_mn_b][1] + lst[positive_mx_b][0]
                print(total)
            print(' '.join(str(i) for i in ans + [positive_mn_b + 1, positive_mx_b + 1, negative_mx_a + 1] + bad))