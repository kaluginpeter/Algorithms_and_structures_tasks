# In this Kata, you will be given a number n (n > 0) and your task will be to return the smallest square number N (N > 0) such that n + N is also a perfect square. If there is no answer, return -1 (nil in Clojure, Nothing in Haskell, None in Rust).
#
# solve(13) = 36
# # because 36 is the smallest perfect square that can be added to 13 to form a perfect square => 13 + 36 = 49
#
# solve(3) = 1 # 3 + 1 = 4, a perfect square
# solve(12) = 4 # 12 + 4 = 16, a perfect square
# solve(9) = 16
# solve(4) = -1
# More examples in test cases.
#
# Good luck!
#
# Algorithms
# Solution
def solve(n):
    smallest_square = float('inf')
    for a in range(1, int(n ** 0.5) + 1):
        if n % a == 0:
            b = n // a
            for x, y in [(a, b), (b, a)]:
                if (x + y) % 2 == 0 and (y - x) % 2 == 0:
                    m = (x + y) // 2
                    k = (y - x) // 2
                    square_k = k * k
                    if square_k > 0:
                        smallest_square = min(smallest_square, square_k)

    return smallest_square if smallest_square != float('inf') else -1