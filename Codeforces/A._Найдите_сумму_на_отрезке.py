# A. Найдите сумму на отрезке
# ограничение по времени на тест3 секунды
# ограничение по памяти на тест256 мегабайт
# Дан массив a
# . Поступают запросы поиска суммы на отрезке. Вам необходимо на них отвечать.
#
# Входные данные
# Первая строка входных данных содержит одно целое число n
#  (1≤n≤106
# ) — количество элементов массива.
#
# Вторая строка входных данных содержит n
#  целых чисел ai
#  (−109≤ai≤109
# ) — элементы массива a
# .
#
# Третья строка входных данных содержит одно целое число q
#  (1≤q≤106
# ) — количество запросов поиска суммы на отрезке.
#
# Каждая из последующих q
#  строк содержит по два целых числа li
#  и ri
#  (1≤li≤ri≤n
# ) — границы отрезка массива, на котором нужно найти сумму.
#
# Выходные данные
# Для каждого запроса в отдельной строке выведите сумму элементов на соответствующем отрезке массива (включая границы).
#
# Примеры
# Входные данныеСкопировать
# 2
# 10 30
# 3
# 1 1
# 2 2
# 1 2
# Выходные данныеСкопировать
# 10
# 30
# 40
# Входные данныеСкопировать
# 5
# -1 -2 3 0 4
# 5
# 1 5
# 1 2
# 4 4
# 3 4
# 2 5
# Выходные данныеСкопировать
# 4
# -3
# 0
# 3
# 5
# Входные данныеСкопировать
# 7
# 1 1 1 1 1 1 1
# 9
# 1 7
# 2 6
# 3 4
# 2 5
# 5 7
# 6 6
# 3 3
# 2 7
# 1 1
# Выходные данныеСкопировать
# 7
# 5
# 2
# 4
# 3
# 1
# 1
# 6
# 1
# Solution
# C++ O(N + T) O(N) PrefixSum
#include <bits/stdc++.h>


void solution() {
    int n;
    std::cin >> n;
    std::vector<long long> prefixSum (n + 1, 0);
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        prefixSum[i + 1] = prefixSum[i] + num;
    }
    int t;
    std::cin >> t;
    for (int i = 0; i < t; ++i) {
        int l, r;
        std::cin >> l >> r;
        std::cout << (prefixSum[r] - prefixSum[l - 1]) << "\n";
    }
}


int main () {
    std::ios::sync_with_stdio(NULL);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    solution();
}

# Python O(N + T) O(N) PrefixSum
from __future__ import annotations
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    prefix_sum: list[int] = [0] * (n + 1)
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + next(nums)
    t: int = int(sys.stdin.readline().rstrip())
    for _ in range(t):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(prefix_sum[r] - prefix_sum[l - 1]) + '\n')


if __name__ == '__main__':
    solution()