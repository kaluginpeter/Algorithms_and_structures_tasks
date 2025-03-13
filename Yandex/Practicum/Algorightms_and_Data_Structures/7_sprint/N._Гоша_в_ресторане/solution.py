import sys


def solution():
    """
    Time Complexity O(N**2)
    Memory Complexity O(N**2)
    """
    n: int = int(sys.stdin.readline().rstrip())
    prices: list[int] = [0] * n
    for i in range(n): prices[i] = int(sys.stdin.readline().rstrip())
    dp: list[list[int]] = [[float('inf')] * (n + 2) for _ in range(n + 1)]
    dp[0][0] = 0
    for day in range(1, n + 1):
        for ticket in range(day + 1):
            if prices[day - 1] > 500:
                dp[day][ticket] = dp[day - 1][ticket + 1]
                if ticket: dp[day][ticket] = min(dp[day][ticket], dp[day - 1][ticket - 1] + prices[day - 1])
            else: dp[day][ticket] = min(dp[day - 1][ticket] + prices[day - 1], dp[day - 1][ticket + 1])
    ticket: int = 0
    min_price: int = float('inf')
    for chosen_ticket in range(n + 1):
        if dp[n][chosen_ticket] < min_price:
            min_price = dp[n][chosen_ticket]
            ticket = chosen_ticket
    last_price: int = min_price
    days: list[int] = []
    for day in range(n - 1, -1, -1):
        if dp[day][ticket + 1] == last_price:
            days.append(day + 1)
            ticket += 1
        else:
            if prices[day] > 500: ticket -= 1
            last_price -= prices[day]
    days.reverse()
    sys.stdout.write('{} {}\n'.format(min_price, len(days)))
    sys.stdout.write('{}\n'.format(' '.join(str(day) for day in days)))


if __name__ == '__main__':
    solution()