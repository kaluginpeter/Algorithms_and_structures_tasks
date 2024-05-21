# A. Удаление дубликатов
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Марсоход берёт пробы грунта, определяет тип горных пород и записывает полученные данные в отсортированный массив. Каждый тип горной породы обозначается целым числом.
#
# Массив отсортирован в порядке возрастания: значения идут от меньшего к большему. В массиве могут быть дублирующиеся значения, ведь в разных пробах могут встречаться одни и те же горные породы.
#
# Ваша задача — написать программу, удаляющую дубликаты из этого массива: каждый элемент должен встречаться в массиве только один раз. При этом относительный порядок элементов должен остаться прежним.
#
# Дублирующие значения нужно заменить на символ подчёркивания.
#
# После выполнения преобразований массив должен остаться такого же размера, как и был. В начале массива должны находиться уникальные элементы, а после них — элементы, содержащие символ подчёркивания. Эти элементы должны быть строго в конце массива, не между числами.
#
# Формат ввода
# В первой строке записано целое число n — это длина массива, переданного во второй строке.
#
# Во второй строке записано n натуральных чисел, разделённых пробелами.
#
# Формат вывода
# Уникальные числа из исходного массива по возрастанию и символы подчёркивания. Элементы должны быть разделены пробелами. Общее количество элементов должно быть равно n.
#
# Пример 1
# Ввод	Вывод
# 3
# 1 1 2
# 1 2 _
# Пример 2
# Ввод	Вывод
# 10
# 0 0 1 1 1 2 2 3 3 4
# 0 1 2 3 4 _ _ _ _ _
# Пример 3
# Ввод	Вывод
# 5
# 0 3 5 11 11
# 0 3 5 11 _
# Solution Bucket sort
# Time Complexity O(N)
# Memory Complexity O(N)
from typing import List, Tuple

def parse_input() -> Tuple[int, List[int]]:
    with open('input.txt', 'r') as file_in:
        lines: List[str] = file_in.readlines()

    n: int = int(lines[0].rstrip())
    output: List[int] = list(map(int, lines[1].rstrip().split()))
    return n, output

def create_bucket(boundary: int) -> List[int]:
    return [0 for chunk in range(boundary + 1)]

def fill_bucket(bucket: List[int], sentence: List[int]) -> None:
    for number in sentence:
        bucket[number] += 1

def count_duplicates(bucket: List[int], boundary: int) -> int:
    duplicates: int = 0
    for chunk in range(boundary + 1):
        duplicates += max(0, bucket[chunk] - 1)
    return duplicates

def rearange_numbers(sentence: List[int], bucket: List[int], duplicates: int, boundary: int) -> None:
    idx: int = 0
    for chunk in range(boundary + 1):
        if bucket[chunk] > 0:
            sentence[idx] = chunk
            idx += 1
    for duplicate in range(duplicates):
        sentence[idx] = '_'
        idx += 1

def print_answer(sentence: List[int | str]):
    with open('output.txt', 'w') as file_out:
        file_out.write(' '.join(str(number) for number in sentence))

def solution() -> None:
    n, numbers = parse_input()
    max_number: int = max(numbers)
    bucket: List[int] = create_bucket(max_number)
    fill_bucket(bucket, numbers)
    duplicates: int = count_duplicates(bucket, max_number)
    rearange_numbers(numbers, bucket, duplicates, max_number)
    print_answer(numbers)

if __name__ == '__main__':
    solution()