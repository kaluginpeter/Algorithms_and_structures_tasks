import sys


def solution() -> None:
    """
    Time Complexity O(2**M)
    Memory Complexity O(M)
    """
    N, M = map(int ,sys.stdin.readline().rstrip().split())
    coins: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    min_coins: int = float('inf')
    best_combination: list[int] = []
    for mask in range(1 << (2 * M)):
        total: int = 0
        count: int = 0
        current: list[int] = []
        valid: bool = True
        for i in range(M):
            bits: int = (mask >> (2 * i)) & 0x3
            if bits > 2:
                valid = False
                break 
            total += bits * coins[i]
            count += bits
            for j in range(bits): current.append(coins[i])
        if valid and total == N:
            if count < min_coins:
                min_coins = count
                best_combination = current
    if min_coins != float('inf'):
        sys.stdout.write('{}\n{}\n'.format(min_coins, ' '.join(str(coin) for coin in best_combination)))
    else:
        total_money: int = 0
        for coin in coins: total_money += 2 * coin
        sys.stdout.write('{}\n'.format([0, -1][total_money < N]))


if __name__ == '__main__':
    solution()