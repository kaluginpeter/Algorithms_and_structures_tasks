# A. Сортировка по шаблону
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# По прибытии на Марс грузового космического корабля робот-грузчик должен расставить прибывшие контейнеры в определённом порядке. Контейнеры пронумерованы вразнобой, а номера могут повторяться. Нумерация может быть, например, такой:
#
# # Прибыло 11 контейнеров:
# 2 3 1 3 2 4 6 7 9 2 19
# У робота-грузчика есть инструкция, шаблон, в котором указано, в каком порядке должны стоять контейнеры:
#
# 2 1 4 3 9 6
# Из этой инструкции следует, что сперва должны стоять все контейнеры с номером 2 (сколько бы их ни было на борту), следом — все контейнеры с номером 1, дальше — все контейнеры с номером 4 — и так до конца шаблона-инструкции.
#
# Если же в грузовике окажутся контейнеры, не учтённые в инструкции, их надо поставить последними, в порядке возрастания.
#
# 2 3 1 3 2 4 6 7 9 2 19  # Номера контейнеров в грузовике.
#
# 2 1 4 3 9 6  # Шаблон-инструкция
#
# 2 2 2 1 4 3 3 9 6 7 19  # Результат работы робота-грузчика.
#
# # Контейнеры 7 и 19 не были упомянуты в инструкции.
# # Они переставлены в конец результирующего массива
# # и отсортированы от меньшего к большему.
# # И это правильно, так и надо.
# Ваша задача — написать программу, которая:
#
# будет принимать на вход массив для сортировки и массив-шаблон, в соответствии с которым должна быть выполнена сортировка;
# вернёт массив, отсортированный в соответствии с шаблоном.
# Формат ввода
# В первой строке передаётся количество чисел, которые нужно отсортировать, n. Оно не превосходит 1500.
#
# Во второй строке передаются n чисел, которые надо отсортировать. Значения этих чисел не превосходят 1000.
#
# В третьей строке передаётся длина массива-шаблона m. Длина массива не превосходит 1500.
#
# В четвёртой строке передаётся массив-шаблон, в соответствии с которым нужно отсортировать первый массив. Значения в этом массиве не превосходят 1000.
#
# В первом массиве гарантированно присутствуют все числа из массива-шаблона.
#
# Формат вывода
# Выведите в строку через пробел значения из первого массива, отсортированные в соответствии с шаблоном.
#
# Пример 1
# Ввод	Вывод
# 10
# 2 4 3 5 6 0 9 8 7 7
# 6
# 2 4 3 5 6 0
# 2 4 3 5 6 0 7 7 8 9
# Пример 2
# Ввод	Вывод
# 11
# 2 3 1 3 2 4 6 7 9 2 19
# 6
# 2 1 4 3 9 6
# 2 2 2 1 4 3 3 9 6 7 19
# Пример 3
# Ввод	Вывод
# 11
# 3 10 5 9 2 7 6 0 8 3 4
# 8
# 3 10 5 9 2 7 6 0
# 3 3 10 5 9 2 7 6 0 4 8
# Solution Bucket sort Time O(N) Memory O(N)
import sys


def parse_input() -> tuple[int, list[int], int, list[int]]:
    len_n: int = int(sys.stdin.readline().rstrip())
    n: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    len_m: int = int(sys.stdin.readline().rstrip())
    m: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    return len_n, n, len_m, m


def create_bucket(numbers: list[int]) -> list[int]:
    bucket: list[int] = [0 for _ in range(max(numbers) + 1)]
    return bucket


def fill_bucket(bucket: list[int], numbers: list[int]) -> None:
    for number in numbers:
        bucket[number] += 1


def bucket_sort(bucket: list[int], numbers: list[int], template: list[int]) -> None:
    idx: int = 0
    for number in template:
        for _ in range(bucket[number]):
            numbers[idx] = number
            idx += 1
        bucket[number] = 0
    for number in range(len(bucket)):
        if bucket[number] > 0:
            for _ in range(bucket[number]):
                numbers[idx] = number
                idx += 1


def print_answer(arr: list[int]) -> None:
    print(' '.join(str(number) for number in arr))


def solution() -> None:
    len_n, n, len_m, m = parse_input()
    bucket: list[int] = create_bucket(n)
    fill_bucket(bucket, n)
    bucket_sort(bucket, n, m)
    print_answer(n)


if __name__ == '__main__':
    solution()