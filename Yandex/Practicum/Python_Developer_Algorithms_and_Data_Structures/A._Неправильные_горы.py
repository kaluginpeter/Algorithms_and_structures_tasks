# A. Неправильные горы
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# При путешествии по планете марсоход постоянно замеряет высоту рельефа и сохраняет результаты замеров в массив.
#
# Одна из задач марсохода — поиск «правильных гор». «Правильной» считается та гора, у которой на пути от подножия до вершины высота постоянно растёт, а на пути от вершины к подножию — постоянно уменьшается. Если у горы есть несколько вершин или в каком-то месте встречается горизонтальный участок — это «неправильная гора».
#
# Напишите функцию valid_mountain_array, которая будет принимать на вход массив с высотами и возвращать True или False в зависимости от того, «правильная» это гора или нет.
#
# Если в массиве менее трёх элементов, такой массив не может описывать «правильную» гору.
#
# Формат ввода
# Массив целых чисел через пробел — отметки о высоте точек рельефа.
#
# Формат вывода
# Булево значение: True — если гора «правильная», False — если гора «неправильная».
#
# Пример 1
# Ввод	Вывод
# 2 1 3 5 8
# False
# Пример 2
# Ввод	Вывод
# 3 5 5
# False
# Пример 3
# Ввод	Вывод
# 0 3 2 1
# True
# Solution One Pass Time O(N) Memory O(1)
import sys


def parse_input() -> list[int]:
    output: list[int] = list(map(int, sys.stdin.readline().rstrip().split()))
    return output


def check_mountain_sequence(sequence: list) -> bool:
    if len(sequence) < 2: return True
    increase: bool = sequence[0] < sequence[1]
    decrease: bool = sequence[0] > sequence[1]
    if not increase: return False
    for high in range(1, len(sequence)):
        if sequence[high] > sequence[high - 1]:
            if not increase: return False
        elif sequence[high] < sequence[high - 1]:
            if increase:
                increase, decrease = False, True
        else:
            return False
    return decrease


def print_answer(answer: bool) -> None:
    sys.stdout.write(str(answer))


def solution() -> None:
    mountain: list[int] = parse_input()
    answer: bool = check_mountain_sequence(mountain)
    print_answer(answer)


if __name__ == '__main__':
    solution()