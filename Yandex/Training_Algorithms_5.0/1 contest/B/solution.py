lst1: list = list(map(int, input().split(':')))
lst2: list = list(map(int, input().split(':')))
start: int = int(input())
total_t1, total_t2 = lst1[0] + lst2[0], lst1[1] + lst2[1]
guest_t1 = lst1[0] if start == 2 else lst2[0]
guest_t2 = lst1[1] if start == 1 else lst2[1]
if total_t1 > total_t2:
    print(0)
elif start == 1:
    if guest_t1 > guest_t2:
        print(total_t2 - total_t1)
    elif guest_t1 <= guest_t2:
        if guest_t1 + (total_t2 - total_t1) > guest_t2:
            print(total_t2 - total_t1)
        else:
            print(total_t2 - total_t1 + 1)
else:
    if guest_t1 > guest_t2:
        print(total_t2 - total_t1)
    else:
        print(total_t2 - total_t1 + 1)
        