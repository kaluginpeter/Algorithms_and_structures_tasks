# Given a string of integers, count how many times that integer repeats itself, then return a string showing the count and the integer.
#
# Example: "1123"
#
# Here 1 comes twice so <count><integer> will be "21"
# then 2 comes once so <count><integer> will be "12"
# then 3 comes once so <count><integer> will be "13"
# hence output string will be "211213".
#
# Similarly "211213" will return "1221121113" (1 time 2, 2 times 1, 1 time 2, 1 time 1, 1 time 3)
#
# Return "" for empty, nil or non numeric strings
#
# Fundamentals
# Solution
def count_me(data):
    if not data: return ''
    n: int = len(data)
    output: list[str] = []
    left: int = 0
    for right in range(n):
        if not data[right].isdigit(): return ''
        if data[left] != data[right]:
            output.append(f'{right - left}{data[left]}')
            left = right
    output.append(f'{n - left}{data[left]}')
    return ''.join(output)