# -- ПРИНЦИП РАБОТЫ --
#    Алгоритм строит максимальное остовное дерево посредством алгоритма Прима.
#    Алгоритм хранит граф в виде списка смежностей и стартуя с любой вершины,
#    извлекает ребро из максимальной кучи, помечает его, как посещенное
#    и начинает добавлять все ребра еще не посещенных вершин исходящие из текущей вершины
#    в очередь с приоритетом. Алгоритм работает до тех пор, пока либо:
#    - Очередь не пуста ИЛИ количество посещенных вершин не равно количеству вершин в графе.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
#    "Не буду себя утруждать доказательством этого факта,
#    иначе мы просто утонем во всем этом, ааа, во всей этой информации") Овчинкин
#    Применим метод доказательства от противного:
#    Допустим, что существует граф G, для которого алгоритм Прима не возвращает максимальное остовное дерево.
#    Так как мы создаем дерево инкрементным способом, то это означает,
#    что существует момент, в который было принято неправильное решение.
#    Перед добавлением ребра (v, u) дерево Tprim состояло из набора ребер,
#    являющихся поддеревом определенного максимального остовного дерева Tmax,
#    но остовное дерево, полученное добавлением к этому поддереву ребра (v, u),
#    больше не является каким-либо возможным максимальным остовным деревом.
#    Могло ли это произойти? В остовном дереве Tmax должен быть путь p от вершины v к вершине u.
#    Этот путь должен содержать ребро (v1, v2), в котором вершина v1 уже находится в дереве Tprim,
#    а вершина v2 - нет. Вес этого ребра должен быть по крайней мере равен весу ребра (v, u),
#    иначе алгоритм Прима выбрал бы это ребро до ребра (v, u), когда у него была такая возможность.
#    Удалив из дерева Tmax ребро (v1, v2) и вставив вместо него ребро (v, u),
#    мы получим остовное дерево с весом не меньшим, чем прежнее ребро.
#    Это означает, что выбор алгоритмом Прима ребра (v, u) не мог быть ошибочным.
#    Таким образом, доказательство от противного показывает,
#    что создаваемое алгоритмом Прима остовное дерево должно быть максимальным.
#    Таким образом, алгоритм корректен. ■
# Временная сложность
# 1. Вставка исходной последовательности: O(|E|H) => O(|E|log(|E|))
#    Каждая вставка i'го ребра выполняется за O(H) времени, где H это высота кучи. По
#    определению пирамида, будет сбалансированным деревом и высота будет равна O(log(L+1)), где L количество ребер
#    в пирамиде.
#    Соответственно |E| ребер займут O(|E|H) или O(|E|log(|E|)) операций.
# 2. Извлечение из очереди: O(|E|log(|E|))
#    Каждое удаление из очереди, будет занимать O(H) времени на просеивание вниз,
#    соответственно |E| удалений, займут O(O(|E|log(|E|)) ) операций.
# Итоговая временная сложность: O(|E|log(|E|) + |E|log(|E|)) => O(2(|E|log(|E|))) => O(|E|log(|E|))
# Пространственная сложность
# Хранение списка смежности в памяти: O(|V| + |E|)
# Итоговая пространственная сложность: O(|V| + |E|), где |V| количество вершин,
#     а |E| количество ребер из исходной последовательности.
import sys
import heapq


def solution() -> None:
    n, m = map(int, sys.stdin.readline().rstrip().split())
    adj_list: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, weight = map(int, sys.stdin.readline().rstrip().split())
        adj_list[u].append((v, weight))
        adj_list[v].append((u, weight))
    seen: list[bool] = [False] * (n + 1)
    vertices: int = 0
    mst: int = 0
    max_heap: list[tuple[int, int]] = [(0, 1)]
    while max_heap and vertices < n:
        weight, vertex = heapq.heappop(max_heap)
        if not seen[vertex]:
            vertices += 1
            mst += -weight
            seen[vertex] = True
            for neighbor, cost in adj_list[vertex]:
                if not seen[neighbor]:
                    heapq.heappush(max_heap, (-cost, neighbor))
    if vertices != n:
        sys.stdout.write('Oops! I did it again\n')
    else:
        sys.stdout.write(f'{mst}\n')


if __name__ == '__main__':
    solution()