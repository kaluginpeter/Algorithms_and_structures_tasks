# B. Проект С.Ч.И.Т.А.Л.К.А.
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Полёты на Марс с участием человека уже не за горами. Команда для полёта почти сформирована. Осталось одно свободное место и масса претендентов на него.
#
# Для решения этой задачи создан проект С.Ч.И.Т.А.Л.К.А. — Стандартный Числовой Иррационально-Точный АЛгоритм Кастинга Астронавтов.
#
# На практике алгоритм реализуется так:
#
# Группа претендентов выстраивается в круг. Число претендентов обозначим через N, претенденты получают номера от 1 до N.
#
# Претенденты получают лист бумаги, на котором написана считалка. Считалка состоит из определённого количества «ритмических частей», тактов. Число тактов обозначим через K.
#
# Претендент под номером 1 произносит вслух считалку и, начиная с себя, на каждый такт указывает на каждого из претендентов. Тот, на ком считалка закончилась, выбывает из числа претендентов.
#
# Участник, следующий за выбывшим, вновь начинает произносить считалку, начав с себя и указывая последовательно на оставшихся претендентов.
#
# Отсев продолжается до тех пор, пока не останется только один претендент — именно он и войдёт в команду.
#
# Посмотрим, как это сработает на примере считалки из 16 тактов для группы из 5 человек. Считалка разбита на такты символом |, а над каждым тактом стоит цифра от 1 до 5: она обозначает, на кого именно показывает ведущий в процессе счёта.
#
#   1          2          3      4
# Десять, | девять, | восемь, | семь
#  5      1         2       3
# В кора|бле | нет места | всем
#  4        5          1     2
# Тот, | кто плохо | кашу | ел
# 3     4      5     1
# Нику|да | не поле|тел!
#
# # Претендент под номером 1 выбывает.
# # Считать начинает претендент, следующий за выбывшим, его номер - 2, он начинает с себя:
#
# 2          3          4         5
# Десять, | девять, | восемь, | семь
# 2       3       4         5
# В кора|бле | нет места | всем
# 2        3          4      5
# Тот, | кто плохо | кашу | ел
# 2     3     4      5
# Нику|да | не поле|тел!
#
# # Претендент под номером 5 выбывает.
# # Считать начинает претендент, следующий за выбывшим.
# # И так до последнего претендента.
# В считалке может быть от 1 до 500 ритмических шагов.
#
# Эни | бени | аппер | боттом
# Не | бывать | тебе | пилотом!
# В кастинге может принимать участие от 1 до 500 претендентов.
#
# Таким образом,
#
# N — любое положительное число от 1 до 500.
# K — любое положительное число от 1 до 500.
# Задачу можно решить в цикле или рекурсивно — любой из этих способов подойдёт. Если же вы сможете выполнить задание и тем и другим способом, это будет высший пилотаж.
#
# Формат ввода
# Первая строка — целое число от 1 до 500, количество претендентов.
#
# Вторая строка — целое число от 1 до 500, количество тактов в считалке.
#
# Формат вывода
# Целое число — номер победившего претендента.
#
# Пример 1
# Ввод	Вывод
# 5
# 2
# 3
# Пример 2
# Ввод	Вывод
# 5
# 1
# 5
# Пример 3
# Ввод	Вывод
# 5
# 6
# 4
# Solution Recursive way. Time O(N) Memory O(N)
import sys


def parse_input() -> tuple[int, int]:
    candidates: int = int(sys.stdin.readline().rstrip())
    countdown: int = int(sys.stdin.readline().rstrip())
    return candidates, countdown


def build_sequence_of_candidates(candidates: int) -> list[int]:
    output: list[int] = [candidate for candidate in range(1, candidates + 1)]
    return output


def last_survive_candidate(sequence_of_candidates: list[int], countdown: int, current: int) -> int:
    if len(sequence_of_candidates) == 1:
        return sequence_of_candidates[0]
    current = (current + countdown - 1) % len(sequence_of_candidates)
    sequence_of_candidates.pop(current)
    return last_survive_candidate(sequence_of_candidates, countdown, current)


def print_answer(answer: int) -> None:
    sys.stdout.write(str(answer))


def solution():
    candidates, countdown = parse_input()
    sequence_of_candidates: list[int] = build_sequence_of_candidates(candidates)
    current: int = 0
    answer: int = last_survive_candidate(sequence_of_candidates, countdown, current)
    print_answer(answer)


if __name__ == '__main__':
    solution()

# Solution While way. Time O(N) Memory O(N)
import sys


def parse_input() -> tuple[int, int]:
    candidates: int = int(sys.stdin.readline().rstrip())
    countdown: int = int(sys.stdin.readline().rstrip())
    return candidates, countdown


def build_sequence_of_candidates(candidates: int) -> list[int]:
    output: list[int] = [candidate for candidate in range(1, candidates + 1)]
    return output


def last_survive_candidate(sequence_of_candidates: list[int], countdown: int) -> int:
    current: int = 0
    while len(sequence_of_candidates) > 1:
        current = (current + countdown - 1) % len(sequence_of_candidates)
        sequence_of_candidates.pop(current)
    return sequence_of_candidates[0]


def print_answer(answer: int) -> None:
    sys.stdout.write(str(answer))


def solution():
    candidates, countdown = parse_input()
    sequence_of_candidates: list[int] = build_sequence_of_candidates(candidates)
    answer: int = last_survive_candidate(sequence_of_candidates, countdown)
    print_answer(answer)


if __name__ == '__main__':
    solution()
