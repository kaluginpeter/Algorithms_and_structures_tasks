# A. Служба доставки
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# На Марс заброшена партия стационарных роботов-исследователей. Марсоход должен перевезти их на определённые точки планеты.
#
# Для перевозки роботов есть неограниченное количество транспортных платформ, каждая из которых способна выдерживать определённый вес limit. На одной платформе можно перевезти либо одного робота, либо двух — при условии, что их совокупный вес не превышает limit. Роботы имеют разный вес.
#
# Программа должна получить на вход массив, каждый элемент которого — это вес робота. Второй параметр, который должна принять программа, — это значение limit, грузоподъёмность одной платформы.
#
# Определите минимальное количество транспортных платформ, необходимое для перевозки всех роботов, описанных в массиве.
#
# Количество платформ неограниченно.
# Каждая платформа выдерживает максимальный вес limit.
# На каждой платформе можно перевезти не более двух роботов при условии, что их совокупный вес не превышает limit.
# Вес отдельного робота не может превышать limit.
# Не забудьте добавить в код аннотации типов данных.
#
# После успешного прохождения тестов на платформе Яндекс Контест отправьте решение на проверку ревьюеру.
#
# Формат ввода
# В первой строке записан массив целых чисел, через пробел — это вес отдельных роботов.
#
# Во второй строке записан лимит — предельная грузоподъёмность платформы.
#
# Формат вывода
# Целое число, указывающее на необходимое количество платформ для транспортировки.
#
# Пример 1
# Ввод	Вывод
# 1 2
# 3
# 1
# Пример 2
# Ввод	Вывод
# 3 2 2 1
# 3
# 3
# Пример 3
# Ввод	Вывод
# 3 5 3 4
# 5
# 4
# First review Time O(NlogN) Memory O(1)
import array
from typing import Tuple, List
from collections.abc import MutableSequence


def parse_input_data() -> Tuple[MutableSequence[int], int]:
    """
    Parse input data from file and return it.
    File should name as 'input.txt'
    :return tuple with first argument is array of int and second argument is integer:
    """
    with open('input.txt', 'r') as input_file:
        lines: List[str, str] = input_file.readlines()

    iterable_sequence: iter = map(int, lines[0].rstrip().split())
    output_array: MutableSequence[int] = array.array('i', sorted(iterable_sequence))
    output_number: int = int(lines[1].rstrip())
    return output_array, output_number


def find_answer_in_sequence(sequence: MutableSequence[int], limit: int, boundary: int) -> int:
    """
    Return maximum number of platforms that should be used for storing all robots.
    :param sequence: Array of int representing weight of each robot.
    :param limit: max size that can be stored in one platform.
    :param boundary: length of sequence.
    :return: integer representing answer.
    General idea:
    Sort sequence in increasing order and use two pointers with greedy approach.
    So we have two decision:
    - Most heavy and the lightest weight can store together at one platform,
        if it is, we move both pointers
    - Platform can story only most heavy robot,
        so we just need move right pointer.
    """
    platform: int = 0
    left_boundary: int = 0
    right_boundary: int = boundary - 1
    while left_boundary <= right_boundary:
        # Condition if both robots can be store at one platform
        if sequence[left_boundary] + sequence[right_boundary] <= limit:
            left_boundary, right_boundary = left_boundary + 1, right_boundary - 1
        # Otherwise it means that platform can store only one robot
        else:
            right_boundary -= 1
        platform += 1
    return platform


def print_answer(answer: int) -> None:
    """
    Write answer in file.
    Output file has name 'output.txt'
    :param answer: integer representing answer
    :return: None
    """
    with open('output.txt', 'w') as output_file:
        output_file.write(str(answer))


def solution() -> None:
    """
    Solution use Two Pointers, Sorting and Greedy approaches.
    Time complexity is O(NlogN)
    Memory complexity is O(1)
    :return: None
    """
    sequence: MutableSequence[int]
    limit: int
    sequence, limit = parse_input_data()
    length_of_sequence: int = len(sequence)
    answer: int = find_answer_in_sequence(sequence, limit, length_of_sequence)
    print_answer(answer)


if __name__ == '__main__':
    solution()

# Second review Time O(NlogN) Memory O(1)
# Id of successfully attempt - 114609905
from collections.abc import MutableSequence

def minimum_amount_platform_to_store_robots(
    weights: MutableSequence[int], limit: int
) -> int:
    """
    Return maximum number of platforms that should be used for storing all robots.
    :param weights: Array of objects representing weight of each robot.
    :param limit: max size that can be stored in one platform.
    :return: integer representing minimum amount of platforms used to store all robots.
    General idea:
    Sort sequence in increasing order and use two pointers with greedy approach.
    So we have two decision:
    - Most heavy and the lightest weight robots can store together at one platform,
        if it is, we move both pointers
    - Platform can story only most heavy robot,
        so we just need move right pointer.
    """
    # Sorting in increasing order, where (i0 <= i1 <= ... <= in-1 <= in)
    weights = sorted(weights)
    platform: int = 0
    lightwest_robot_pointer: int = 0
    # The highest robot will be at the end of sequence
    highest_robot_pointer: int = len(weights) - 1
    while lightwest_robot_pointer <= highest_robot_pointer:
        # Condition if both robots can be store at one platform
        if (
            weights[lightwest_robot_pointer]
            + weights[highest_robot_pointer] <= limit
        ):
            lightwest_robot_pointer += 1
        highest_robot_pointer -= 1
        platform += 1
    return platform


if __name__ == '__main__':
    """
    Time complexity O(NlogN)
    Memory complexity O(1)
    Algorithms: Two Pointers, Greedy, Sorting
    """
    print(
        minimum_amount_platform_to_store_robots(
            list(map(int, input().split())), int(input())
        )
    )
