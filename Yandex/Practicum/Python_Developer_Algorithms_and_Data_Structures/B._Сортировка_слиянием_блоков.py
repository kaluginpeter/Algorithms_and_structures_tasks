# B. Сортировка слиянием блоков
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Проснувшись однажды утром после беспокойного сна, Антон обнаружил, что изобрёл новый алгоритм сортировки.
#
# Алгоритм предназначен для сортировки массивов длиной n, состоящих из уникальных чисел в диапазоне от 0 до n-1. Иными словами, массив должен содержать целые положительные числа от 0 до n-1, перемешанные как угодно. Например, если n = 8, то массив может быть таким:
#
# # Массив длиной 8 элементов
# 3 1 0 2 6 5 4 7  # В массиве содержатся все целые числа в диапазоне от 0 до 7.
# Суть алгоритма: исходный массив разделяется на блоки так, чтобы каждый блок можно было отсортировать и при слиянии отсортированных блоков получился отсортированный массив. Менять блоки местами нельзя.
#
# # Делим исходный массив на блоки, которые можно отсортировать:
#
# # Так нельзя: после сортировки блоков их не объединить в отсортированный массив.
# 3 1 | 0 2 | 6 | 5 4 | 7
#
# # И так нельзя.
# 3 | 1 0 2 | 6 5 4 7
#
# 3 1 0 2 | 6 5 4 | 7  # А вот такое деление - в самый раз!
#
# # Сортируем блоки:
# 0 1 2 3 | 4 5 6 | 7
#
# # Объединяем блоки:
# 0 1 2 3 4 5 6 7
#
# # Получили отсортированный массив!
# Алгоритм сортировки состоит из трёх шагов:
#
# Разбить исходную последовательность на k блоков. Блоки могут иметь разные размеры. Первый блок обязательно должен содержать 0. Если длина первого блока — r элементов, то максимальным значением в первом блоке должно быть число r - 1. А следующий блок (если он вообще будет) должен содержать число r. Этот принцип должен соблюдаться и в последующих блоках.
# Отсортировать каждый из блоков.
# Объединить блоки в единый массив.
# Такая сортировка выгодна в том случае, если разбить исходный массив на максимально возможное число блоков.
#
# В этом задании вам предстоит реализовать только первый шаг: разбить массив на блоки и вернуть их количество.
#
# Задание: написать программу, которая получает на вход массив и возвращает максимальное число блоков, на которое можно разбить этот массив так, чтобы сортировка отработала корректно.
#
# Ещё один пример:
#
# 3 2 0 1 4 6 5
# Минимальный размер первого блока — 4.
#
# Если взять лишь первые два элемента, то отсортированная последовательность будет начинаться с двойки, а это неправильно. Если взять первые три элемента, то последовательность будет начинаться с нуля, но после него сразу же пойдёт двойка. Опять нехорошо.
#
# А вот первые четыре элемента гарантируют, что первая часть результирующего массива будет корректной.
#
# Четвёрку можно взять как отдельный блок из одного элемента.
#
# Последние два элемента составят третий блок. Таким образом:
#
# первый блок: 3, 2, 0, 1;
# второй блок: 4;
# третий блок: 6, 5.
# В этом примере ответ равен 3: чтобы сортировка блоками отработала корректно, полученный массив можно разделить максимум на три блока.
#
# Формат ввода
# В первой строке задано n — количество чисел для сортировки (n ≤ 1000). В следующей строке записаны числа от 0 до n - 1, которые надо разбить на блоки.
#
# Формат вывода
# Выведите максимальное число блоков, на которое можно разбить данные при использовании метода частичной сортировки.
#
# Пример 1
# Ввод	Вывод
# 4
# 0 1 3 2
# 3
# Пример 2
# Ввод	Вывод
# 8
# 3 6 7 4 1 5 0 2
# 1
# Пример 3
# Ввод	Вывод
# 5
# 1 0 2 3 4
# 4
# Solution Greedy One Pass Time O(N) Memory O(1)
import sys


def parse_input() -> tuple[int, list[int]]:
    n: int = int(sys.stdin.readline().rstrip())
    numbers: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    return n, numbers


def maximum_blocks_that_can_get(numbers: list[int]) -> int:
    blocks: int = 0
    max_number: int = -1
    seen_zero: bool = False
    len_of_subsequence: int = 0
    for number in numbers:
        if not seen_zero:
            max_number = max(max_number, number)
            if number == 0: seen_zero = True
        elif (
            (max_number + 1 == len_of_subsequence)
            or len_of_subsequence == 1
            and number > max_number
        ):
            blocks += 1
            max_number = number
        else:
            max_number = max(max_number, number)
        len_of_subsequence += 1
    blocks += 1
    return blocks


def print_answer(answer: int) -> None:
    sys.stdout.write(str(answer))


def solution() -> None:
    n, numbers = parse_input()
    answer: int = maximum_blocks_that_can_get(numbers)
    print_answer(answer)


if __name__ == '__main__':
    solution()
