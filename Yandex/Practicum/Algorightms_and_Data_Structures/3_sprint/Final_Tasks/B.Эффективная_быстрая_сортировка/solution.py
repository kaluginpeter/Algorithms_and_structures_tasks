# -- ПРИНЦИП РАБОТЫ --
# Сортировка выполняется следующими функциями:
#     quick_sort(iter) - принимает итерируемую последовательность:
#             Вызывается функция partition
#                 Функция ничего не возвращает.
#     partition(iter, left, right) рекурсивно сортирует переданный список.
#         Берется pivot индекс случайный в диапазоне [left, right] и swap(pivot, left), pivot = left.
#         Далее заводятся два указателя less_than=left + 1
#         и greater_than = right. Пока less_than <= right_than:
#             1) Пока less_than <= greater_than И array[less_than] < array[pivot] = ++less_than
#             2) Пока less_than <= greater_than И array[greater_than] > array[pivot] = --greater_than;
#             3) Если less_than > greater_than = прерываем цикл.
#             4) Иначе swap(less_than, greater_than)
#         Далее swap(pivot, greater_than) = после swap все элементы меньшие pivot будут находиться в левой части.
#         Рекурсивно сортируем partition(left, greater_than - 1) и partition(greater_than + 1, right).
#         Функция ничего не возвращает.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
#    Для partition:
#        После каждого завершения функции будет одновременно верно, что:
#            array[i] < array[pivot] для каждого i в диапазоне [left, right]
#            и array[i] > array[pivot] для каждого i в диапазоне (pivot, right].
#        На каждом этапе N=right - left + 1, сокращается в приблизительно N/2, то есть
#            максимальное количество сокращений Ω(n)=logN до O(N) для каждого i в N,
#            соответственно для N характерно: Ω(N)=NlogN и O(N^2), а θ(N)=NlogN
# Таким образом, алгоритм корректен. ■

# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# На каждом вызове partition N=right - left + 1 сокращается на Ω(n)=logN или O(N).
#     Каждый вызов требует O(N) времени для сравнения элемента.
#         Соответственно на сортировку уходит O(N^2) или θ(N)=NlogN.
# Итоговая временная сложность O(N^2) или θ(N)=NlogN в среднем случае
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Алгоритм сортировки в худшем случае может потребовать O(N) памяти для хранения стека вызовов рекурсии.
# Итоговая пространственная сложность O(N)

import sys
from random import randint

def comparator(x: tuple[str, int, int], y: tuple[str, int, int]) -> int:
    if x[1] != y[1]:
        return -1 if x[1] < y[1] else 1
    elif x[2] != y[2]:
        return -1 if x[2] > y[2] else 1
    return -1 if x[0] > y[0] else 1

def partition(peoples: list[tuple[str, int, int]], left: int, right: int) -> None:
    if left >= right:
        return
    pivot: int = randint(left, right)
    peoples[pivot], peoples[left] = peoples[left], peoples[pivot]
    pivot = left
    less_than: int = left + 1
    greater_than: int = right
    while True:
        while less_than <= greater_than and comparator(peoples[less_than], peoples[pivot]) == 1:
            less_than += 1
        while less_than <= greater_than and comparator(peoples[greater_than], peoples[pivot]) == -1:
            greater_than -= 1
        if less_than > greater_than:
            break
        peoples[less_than], peoples[greater_than] = peoples[greater_than], peoples[less_than]
    peoples[left], peoples[greater_than] = peoples[greater_than], peoples[left]
    partition(peoples, left, greater_than - 1)
    partition(peoples, greater_than + 1, right)


def quick_sort(peoples: list[tuple[str, int, int]]) -> None:
    partition(peoples, 0, len(peoples) - 1)


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    peoples: list[tuple[str, int, int]] = []
    for _ in range(n):
        name, problems, penalty = sys.stdin.readline().rstrip().split()
        peoples.append((name, int(problems), int(penalty)))
    quick_sort(peoples)
    for idx in range(n):
        if idx:
            sys.stdout.write('\n')
        sys.stdout.write(peoples[idx][0])


if __name__ == '__main__':
    solution()