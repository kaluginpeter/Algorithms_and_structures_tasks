# B. Поиск подстроки
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Марсоход должен исследовать странные каменные структуры: на поверхности скал обнаружена последовательность символов. Предположительно, эту последовательность создали разумные существа. Учёные предполагают, что эта последовательность содержит некие коды или тексты.
#
# Для расшифровки необходимо выявить в последовательности самую длинную подстроку, состоящую из уникальных символов: наибольший ряд символов, в котором каждый символ встречается только один раз. Это поможет найти ключ к разгадке послания или просто даст понять, случайны ли эти символы, или в них есть порядок.
#
# Напишите программу, которая принимает на вход строку и находит в ней наибольшую длину подстроки, в которой нет повторяющихся символов. Программа должна вернуть натуральное число — длину этой подстроки.
#
# Используйте метод скользящего окна для решения задачи. Если в строке встретится дубликат, запомните длину получившейся подстроки и начинайте строить окно заново.
#
# Формат ввода
# Одна строка, состоящая из строчных латинских букв. Длина строки не превосходит 10 000 символов.
#
# Формат вывода
# Натуральное число — длина наибольшей подстроки с уникальными символами.
#
# Пример 1
# Ввод	Вывод
# abcabcbb
# 3
# Пример 2
# Ввод	Вывод
# bbbbb
# 1
# Solution Sliding Window HashSet Time O(N) Memory O(k) where k is length of unique chars
import sys


def parse_input() -> str:
    output: str = sys.stdin.readline().rstrip()
    return output


def find_longest_unique_substring(sequence: str) -> int:
    answer: int = 0
    char_sequence: set[str] = set()
    left: int = 0
    for right in range(len(sequence)):
        while sequence[right] in char_sequence:
            char_sequence.remove(sequence[left])
            left += 1
        char_sequence.add(sequence[right])
        answer = max(answer, right - left + 1)
    return answer


def print_answer(answer: int) -> None:
    sys.stdout.write(str(answer))


def solution() -> None:
    sequence: str = parse_input()
    answer: int = find_longest_unique_substring(sequence)
    print_answer(answer)


if __name__ == '__main__':
    solution()