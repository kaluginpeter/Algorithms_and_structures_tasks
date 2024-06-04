# A. Шифрованные инструкции
# Ограничение времени	1 секунда
# Ограничение памяти	64.0 Мб
# Ввод	стандартный ввод или input.txt
# Вывод	стандартный вывод или output.txt
# Марсоход получает с Земли сокращённые инструкции с заданиями, например:
#
# с — сделать снимок;
# в — взять образец грунта;
# ш — сделать шаг;
# о — включить освещение;
# и — инициировать сканирование местности.
# Из-за ограничений канала связи инструкции отправляются в сжатом виде. Например, если марсоходу нужно сделать 10 снимков подряд, инструкция будет выглядеть как 10[с].
#
# Число перед квадратными скобками обозначает, сколько раз надо повторить последовательность внутри скобок. Скобки могут быть и вложенными: 2[ш3[с]]10[с].
#
# Таким образом, командный центр на Земле может отправить марсоходу сжатую строку инструкций, а марсоход получит и расшифрует её в полную последовательность команд.
#
# Команды могут обозначаться символами латиницы или кириллицы.
#
# Пример:
#
# Команда: 2[с]3[в]ш
# Расшифровка: «ссвввш».
# Смысл: сделать два снимка, взять три образца грунта и сделать шаг.
# Пример 2:
#
# Команда: 2[в3[ш]]с
# Расшифровка: «вшшшвшшшс»
# Смысл: Взять образец грунта, сделать три шага; взять образец грунта, сделать три шага; сделать снимок.
# Напишите программу, которая расшифровывает сжатые сообщения и возвращает строку с командами.
#
# Не забудьте добавить в код аннотации типов данных.
#
# После успешного прохождения тестов на платформе Яндекс Контест отправьте решение на проверку ревьюеру.
#
# Формат ввода
# Сокращенная форма команды. Например, 3[a]2[bc]. Гарантированно приходит валидная строка. В строке могут быть только буквы, числа и квадратные скобки.
#
# Длина строки может находиться в диапазоне от 0 (пустая строка) до 30 символов включительно. Числа в строке могут быть от 1 до 300 включительно.
#
# Формат вывода
# Полная форма команды. Например, aaabcbc.
#
# Пример 1
# Ввод	Вывод
# 3[a]2[bc]
# aaabcbc
# Пример 2
# Ввод	Вывод
# 3[a2[c]]
# accaccacc
# Пример 3
# Ввод	Вывод
# 2[abc]3[cd]ef
# abcabccdcdcdef
# Solution 1 (First review) Recursive way to solve. Time O(NM) Memory O(NM)
def decrypted_commands(commands: str, current_idx: int = 0):
    """
    Decrypted string by recursively call inside yourself.
    Time Complexity O(NM).
    Memory Complexity O(NM).
    Where N is length of commands and M is depth of recursion call(frequency of square brackets).
    :param commands: string with encrypted commands
    :param current_idx:*
    :return: tuple of decrypted string and current_index*
    * - Don't touch and use! For builtin usages only!
    """
    decrypted_string: str = ''
    while current_idx < len(commands):
        # If we meet closed square bracket, it means that we go to the end of recursive command
        if commands[current_idx] == ']': break
        if commands[current_idx].isalpha():
            decrypted_string += commands[current_idx]
            current_idx += 1
        else:
            multiplicator: int = 0
            while commands[current_idx] != '[':
                multiplicator = multiplicator * 10 + int(commands[current_idx])
                current_idx += 1
            # current_idx == '[' at this moment and we should skipp it
            current_idx += 1
            # Call recursively string with elements inside of square brackets
            new_decrypted_string, current_idx = decrypted_commands(commands, current_idx)
            decrypted_string += multiplicator * new_decrypted_string
    return decrypted_string, current_idx + 1


if __name__ == '__main__':
    commands: str = input()
    print(decrypted_commands(commands)[0])

# Solution 2 (Accepted review) Iterative straight forward. Time O(NM) Memory O(NM)
# Id 114935205
from string import digits
DIGITS = digits
def decrypted_commands(commands: str) -> str:
    """
    Decrypts the string moving straight forward.
    Time Complexity O(NM).
    Memory Complexity O(NM).
    Where N is length of commands and M is size of multiplier frequencies.
    :param commands: string with encrypted commands
    :return: string of decrypted commands
    """
    accumulate_storage = []
    accumulate = decrypted = ''
    for letter in commands:
        match letter:
            case _ if letter in DIGITS: accumulate += letter
            case '[':
                accumulate_storage.append((decrypted, int(accumulate)))
                accumulate = decrypted = ''
            case ']':
                previous_decrpyted, previous_accumulate = (
                    accumulate_storage.pop()
                )
                decrypted = (
                    previous_decrpyted
                    + decrypted * previous_accumulate
                )
            case _: decrypted += letter
    return decrypted

if __name__ == '__main__':
    print(decrypted_commands(input()))
