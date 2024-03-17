x: int = int(input())
y: int = int(input())
p: int = int(input())
def simulation(x: int, y: int, p: int, ratio: float) -> int:
    count: int = 0
    warrior: int = 0
    while y > ratio:
        count += 1
        if warrior >= x:
            return 10**9
        y -= x - warrior
        warrior = 0
        if y > 0:
            warrior += p
    while y > 0:
        count += 1
        if x <= 0:
            return 10**9
        if x > y:
            warrior -= x - y
            y = 0
        else:
            y -= x
        x -= max(0, warrior)
        if y > 0:
            warrior += p
    while warrior > 0:
        count += 1
        if x <= 0:
            return 10**9
        warrior -= x
        x -= max(0, warrior)
    return count
mn: int = 10**9
for i in range(5001):
    mn = min(simulation(x, y, p, ratio=i), mn)
print(mn if mn != 10**9 else -1)