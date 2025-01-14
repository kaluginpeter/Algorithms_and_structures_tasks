# B. Найдите XOR на отрезке
# ограничение по времени на тест3 секунды
# ограничение по памяти на тест256 мегабайт
# Дан массив a
# . Поступают запросы поиска XOR (побитового исключающего или) на отрезке. Вам необходимо на них отвечать.
#
# Входные данные
# Первая строка входных данных содержит одно целое число n
#  (1≤n≤106
# ) — количество элементов массива.
#
# Вторая строка входных данных содержит n
#  целых чисел ai
#  (0≤ai≤109
# ) — элементы массива a
# .
#
# Третья строка входных данных содержит одно целое число q
#  (1≤q≤106
# ) — количество запросов поиска XOR'а на отрезке.
#
# Каждая из последующих q
#  строк содержит по два целых числа li
#  и ri
#  (1≤li≤ri≤n
# ) — границы отрезка массива, на котором нужно найти XOR.
#
# Выходные данные
# Для каждого запроса в отдельной строке выведите XOR элементов на соответствующем отрезке массива (включая границы).
#
# Примеры
# Входные данныеСкопировать
# 2
# 12 6
# 3
# 1 1
# 2 2
# 1 2
# Выходные данныеСкопировать
# 12
# 6
# 10
# Входные данныеСкопировать
# 5
# 1 2 3 0 4
# 5
# 1 5
# 1 2
# 4 4
# 3 4
# 2 5
# Выходные данныеСкопировать
# 4
# 3
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
# 1
# 1
# 0
# 0
# 1
# 1
# 1
# 0
# 1
# Solution
# C++ O(N) O(N) PrefixSum
#include <bits/stdc++.h>


void solution () {
    int n;
    std::cin >> n;
    std::vector<long long> prefixSum (n + 1, 0);
    for (int i = 0; i < n; ++i) {
        int num;
        std::cin >> num;
        prefixSum[i + 1] = prefixSum[i] ^ num;
    }
    int q;
    std::cin >> q;
    for (int i = 0; i < q; ++i) {
        int l, r;
        std::cin >> l >> r;
        std::cout << (prefixSum[l - 1] ^ prefixSum[r]) << "\n";
    }
}


int main () {
    std::ios::sync_with_stdio(NULL);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    solution();
}

# Python O(N) O(N) PrefixSum
from __future__ import annotations
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    prefix_sum: list[int] = [0] * (n + 1)
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] ^ next(nums)
    q: int = int(sys.stdin.readline().rstrip())
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().rstrip().split())
        sys.stdout.write(str(prefix_sum[l - 1] ^ prefix_sum[r]) + '\n')


if __name__ == '__main__':
    solution()