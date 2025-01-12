# A. Построение префиксных сумм
# ограничение по времени на тест3 секунды
# ограничение по памяти на тест256 мегабайт
# Дан массив a
# . Выведите его массив префиксных сумм. Иными словами, выведите 0
# , a1
# , a1+a2
# , …
# , a1+a2+…+an
# .
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
# Выходные данные
# В единственной строке выведите массив префиксных сумм массива a
# .
#
# Примеры
# Входные данныеСкопировать
# 1
# 178
# Выходные данныеСкопировать
# 0 178
# Входные данныеСкопировать
# 7
# 0 1 2 3 4 5 6
# Выходные данныеСкопировать
# 0 0 1 3 6 10 15 21
# Входные данныеСкопировать
# 5
# -1 -2 3 0 4
# Выходные данныеСкопировать
# 0 -1 -3 0 0 4
# Solution
# C++ O(N) O(1) Math PrefixSum
#include <bits/stdc++.h>


void solution() {
    int n;
    std::cin >> n;
    long long prev = 0;
    for (int i = 0; i < n; ++i) {
        std::cout << prev << " ";
        int num;
        std::cin >> num;
        prev += num;
    }
    std::cout << prev << "\n";
}


int main() {
    std::ios::sync_with_stdio(NULL);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    solution();
}

# Python O(N) O(1) Math PrefixSum
import sys


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    prev: int = 0
    nums: iter[int] = map(int, sys.stdin.readline().rstrip().split())
    for _ in range(n):
        sys.stdout.write(str(prev) + ' ')
        prev += next(nums)
    sys.stdout.write(str(prev) + '\n')


if __name__ == '__main__':
    solution()