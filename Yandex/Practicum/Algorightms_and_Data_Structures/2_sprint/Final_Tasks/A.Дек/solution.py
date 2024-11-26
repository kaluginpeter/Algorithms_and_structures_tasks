# -- ПРИНЦИП РАБОТЫ --
# Дек реализован на кольцевом буффере, иначе говоря, циклическом массиве.
# Поддерживаемые методы:
# - decrement_index уменьшает заданный индекс на "-1" с сохранением цикличности
#       Дерево принятия решений:
#       1) Взятие текущего значения переданного поля (методом getattr) со сдвигом по формуле
#           и присваивание результата переменной decremented_index.
#           Формула сдвига: g(i) = (i - 1 + Capacity) mod Capacity,
#           где Capacity - максимальная вместимость дека. Это позволяет поддерживать цикличность массива.
#       2) Возвращаем сдвинутый индекс под переменной decremented_index
#
# - increment_index увеличивает заданный индекс на "1" с сохранением цикличности
#       Дерево принятия решений:
#       1) Взятие текущего значения переданного поля (методом getattr) со сдвигом по формуле
#           и присваивание результата переменной incremented_index. Формула сдвига: f(i) = (i + 1) mod Capacity,
#           где Capacity - максимальная вместимость дека. Это позволяет поддерживать цикличность массива.
#       2) Возвращаем сдвинутый индекс под переменной decremented_index
#
# - get_tail_index возвращает индекс элемента в конце очереди, использует формулу
#       f() = (h + s) mod c, где:
#           h - это индекс элемента в начале дека,
#           s - текущий размер дека
#           c - вместимость дека
#
# - push_back постановка элемента в конец дека.
#       Дерево принятия решений:
#       1) Если дек полон(проверка методом is_full), выбрасывается исключение IndexError с сообщением "error\n"
#       2) Увеличиваем текущий размер дека, параметром size_
#       3) Получаем tail_index методом get_tail_index
#       4) Присваиваем массиву переданный элемент под индексом tail_index
#
# - push_front постановка элемента в начало дека
#       Дерево принятия решений:
#       1) Если дек полон(проверка методом is_full), выбрасывается исключение IndexError с сообщением "error\n"
#       2) Присваиваем массиву переданный элемент под индексом head_index
#       3) Сдвигаем head_index на -1, методом decrement_index
#       4) Увеличиваем текущий размер дека, параметром size_
#
# - pop_front взятие элемента из начала дека
#       Дерево принятия решений:
#       1) Если дек пуст(проверка методом is_empty), выбрасывается исключение IndexError с сообщением "error\n"
#       2) Сдвигаем head_index на 1, методом increment_index
#       3) Сохраняем выходное значение в переменную output под индексом head_index
#       4) Очищаем элемент в массиве под индексом head_index (ставим значение 0)
#       5) Уменьшаем текущий размер дека, параметром size_
#       6) Возвращаем значение переменной output
#
# - pop_back взятие элемента с конца дека
#       Дерево принятия решений:
#       1) Если дек пуст(проверка методом is_empty), выбрасывается исключение IndexError с сообщением "error\n"
#       2) Получаем tail_index методом get_tail_index
#       3) Сохраняем выходное значение в переменную output под индексом tail_index
#       4) Очищаем элемент в массиве под индексом tail_index (ставим значение 0)
#       5) Уменьшаем текущий размер дека, параметром size_
#       6) Возвращаем значение переменной output
#
# - is_empty проверят пуст ли дек
#       Дерево принятия решений:
#       1) Возвращаем текущую длину дека (параметр size_) с логической инверсией
#
# - is_full проверят заполнен ли дек
#       Дерево принятия решений:
#       1) Возвращаем результат сравнения на равенство текущей длины дека (параметр size_)
#           c максимальной вместимостью массива (параметр capacity_)
#
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Из описания алгоритма следует, что при любом удалении и вставке элемента в дек. Гарантируется инвариант,
#     что индексы сдвигаются на 0 <= 1 шагов
#     и цикличность массива поддерживается модульной арифметикой:
#         Для вставки в конец: После применения increment_index гарантируется,
#             что новый индекс будет в диапазоне [0, Capacity).
#         Для вставки в начало: После применения decremented_index также будет в диапазоне [0, Capacity),
#             даже если исходный индекс был 0.
#      это верно для каждого i, где {i ∣ i = k mod Capacity, k ∈ Z}
# Таким образом, алгоритм корректен. ■
#
# -- ВРЕМЕННАЯ СЛОЖНОСТЬ --
# - decrement_index, increment_index выполняются за O(1) из-за математических операций
#
# - push_back, push_front, pop_front, pop_back выполняются за O(1) по определению абстрактной структуры данных "массив"
#
# - is_empty, is_full выполняются за O(1) из-за сравнения значения переменных
#
# - Конструктор дека выполняется за O(N), для резервирования массива размером N.
# Итоговая временная сложность O(N)
# -- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ --
# Дек потребляет O(N) памяти, для хранения массива размером N
# Итоговая пространственная сложность O(N)

import sys


class CircularBufferedDeque:
    def __init__(self, capacity: int) -> None:
        self.deque: list[int] = [0] * capacity
        self.capacity_: int = capacity
        self.size_: int = 0
        self.head_index: int = 0

    def decrement_index(self, field: str) -> None:
        decremented_index: int = (getattr(self, field) - 1 + self.capacity_) % self.capacity_
        setattr(self, field, decremented_index)

    def increment_index(self, field: str) -> None:
        incremented_index: int = (getattr(self, field) + 1) % self.capacity_
        setattr(self, field, incremented_index)

    def get_tail_index(self) -> int:
        return (self.head_index + self.size_) % self.capacity_

    def push_back(self, value: int) -> None:
        if self.is_full():
            sys.stdout.write('error\n')
            return
        self.size_ += 1
        tail_index: int = self.get_tail_index()
        self.deque[tail_index] = value

    def push_front(self, value: int) -> None:
        if self.is_full():
            sys.stdout.write('error\n')
            return
        self.deque[self.head_index] = value
        self.decrement_index('head_index')
        self.size_ += 1

    def pop_front(self) -> None:
        if self.is_empty():
            sys.stdout.write('error\n')
            return
        self.increment_index('head_index')
        output: int = self.deque[self.head_index]
        self.deque[self.head_index] = 0
        self.size_ -= 1
        sys.stdout.write(str(output) + '\n')

    def pop_back(self) -> None:
        if self.is_empty():
            sys.stdout.write('error\n')
            return
        tail_index: int = self.get_tail_index()
        output: int = self.deque[tail_index]
        self.deque[tail_index] = 0
        self.size_ -= 1
        sys.stdout.write(str(output) + '\n')

    def is_empty(self) -> bool:
        return not self.size_

    def is_full(self) -> bool:
        return self.size_ == self.capacity_


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    m: int = int(sys.stdin.readline().rstrip())
    deque: CircularBufferedDeque = CircularBufferedDeque(m)
    for _ in range(n):
        command: str = sys.stdin.readline().rstrip()
        args = command.split()
        getattr(deque, args[0])(*map(int, args[1:]))


if __name__ == '__main__':
    solution()