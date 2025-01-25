# -- ПРИНЦИП РАБОТЫ --
# Алгоритм выполняет пирамидальную сортировку по следующему принципу:
#    Создается минимальная куча и каждый элемент из входной последовательности,
#    добавляется в кучу. При добавлении элемента, выполняется операция "Просеивание вверх",
#    чтобы поддерживать корректный минимальный элемент пирамиды.
#    После вставки всех элементов, происходит удаление из кучи до тех пор, пока
#    пирамида не окажется пуста. При каждом удалении элемента, выполняется операция "Просеивание вниз",
#    чтобы обновить минимальный элемент в пирамиде.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Алгоритм корректно выводит данные в отсортированном виде, так как:
# 1. При вставке:
#     Операция "Просеивание вверх" обновляет пирамиду в соответствии с правильным положением нового элемента
#     и обеспечивает корректный минимальный элемент кучи.
# 2. При удалении:
#     Операция "Просеивание вниз" изменяет пирамиду, чтобы поставить корректный минимальный
#     элемент в начало очереди в соответствии с приоритетом.
# Таким образом, алгоритм корректен. ■
# Временная сложность
# 1. Вставка исходной последовательности: O(NH) => O(NlogN)
#    Каждая вставка i'го элемента выполняется за O(H) времени, где H это высота кучи. По
#    определению пирамида, будет сбалансированным деревом и высота будет равна O(log(L+1)), где L количество элементов
#    в пирамиде.
#    Соответственно N элементов займут O(NH) или O(NlogN) операций.
# 2. Извлечение из очереди: O(NH) => O(NlogN)
#    Каждое удаление из очереди, будет занимать O(H) времени на просеивание вниз,
#    соответственно N удалений, займут O(NlogN) операций.
# Итоговая временная сложность: O(NlogN + NlogN) => O(2NlogN) => O(NlogN)
# Пространственная сложность
# Хранение кучи в памяти: O(N)
# Итоговая пространственная сложность: O(N), где N количество элементов из исходной последовательности.

import sys


class MinHeap:
    def __init__(self) -> None:
        self.min_heap: list[int] = [None]

    def sift_up(self, idx: int) -> None:
        while idx > 1:
            parent_idx: int = idx // 2
            if self.min_heap[parent_idx] > self.min_heap[idx]:
                self.min_heap[parent_idx], self.min_heap[idx] = self.min_heap[idx], self.min_heap[parent_idx]
                idx = parent_idx
            else: break

    def sift_down(self, idx: int) -> None:
        upper_bound: int = len(self.min_heap) - 1
        while True:
            left_idx: int = idx * 2
            right_idx: int = idx * 2 + 1
            if left_idx > upper_bound: break
            lowest_idx: int = left_idx

            if right_idx <= upper_bound and self.min_heap[lowest_idx] > self.min_heap[right_idx]:
                lowest_idx = right_idx

            if self.min_heap[lowest_idx] < self.min_heap[idx]:
                self.min_heap[lowest_idx], self.min_heap[idx] = self.min_heap[idx], self.min_heap[lowest_idx]
                idx = lowest_idx
            else: break

    def push_back(self, x: tuple[int, int, str]) -> None:
        self.min_heap.append(x)
        self.sift_up(len(self.min_heap) - 1)

    def pop_back(self) -> str:
        result: str = self.min_heap[1][2]
        self.min_heap[1] = self.min_heap[len(self.min_heap) - 1]
        self.min_heap.pop()
        self.sift_down(1)
        return result

    def empty(self) -> bool:
        return len(self.min_heap) == 1


def solution() -> None:
    n: int = int(sys.stdin.readline().rstrip())
    min_heap: MinHeap = MinHeap()
    for _ in range(n):
        login, tasks, penalty = sys.stdin.readline().rstrip().split()
        min_heap.push_back((-int(tasks), int(penalty), login))

    while not min_heap.empty():
        sys.stdout.write(min_heap.pop_back() + '\n')


if __name__ == '__main__':
    solution()