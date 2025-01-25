# -- ПРИНЦИП РАБОТЫ --
# Алгоритм удаляет узел из дерева поиска по следующему принципу:
#    В начале находим необходимый узел и его родителя. Для этого выполняем
#    поиск в глубину используя свойства дерева поиска для нахождения искомого элемента.
#    Затем моделируем ситуации:
#    - node = None -> узел не найден, возвращаем корень дерева
#    - node.left is None and node.right is None -> искомый узел "лист":
#        1) parent = None -> лист является корнем дерева, возвращаем None.
#        2) Удаляем узел node из parent.
#    - node.left and node.right -> узел имеет два поддерева:
#        Ищем самый левый узел в правом поддереве(назовем его "x").
#        Заменяем значение node.value на значение x.value.
#        Удаляем узел "x" из дерева.
#    - узел имеет одно поддерево:
#        Если parent is None, то возвращаем поддерево, т.к искомый элемент, это корень дерева.
#        Иначе заменяем node его поддеревом.
# -- ДОКАЗАТЕЛЬСТВО КОРРЕКТНОСТИ --
# Алгоритм корректно удаляет узел из дерева поиска, так как:
# 1. Нахождение узла и его родителя:
#     Оперируя свойством дерева поиска, мы находим узел в дереве и возвращаем узел и его родителя.
# 2. При удалении:
#     При удалении узла, алгоритм обрабатывает ситуации с поддеревьями удаляемого узла:
#     1) Если узел - лист, то узел удаляется
#     2) Если узел имеет два поддерева, то находим наименьший элемент в правом поддереве
#     и заменяем узел им, чтобы сохранить свойство дерева поиска.
#     3) При наличии одного поддерева, мы удаляем узел и привязываем поддерево к родителю,
#     чтобы сохранить поддерево в дереве поиска.
# Таким образом, алгоритм корректен. ■
# Временная сложность
# 1. Нахождение узла и родителя: O(H)
#    Поиск узла в дереве поиска, занимает время, равное высоту дерева. В худшем случае это O(N),
#    но при сбалансированном дереве, время O(logN).
# 2. Удаление узла: O(H)
#    Если узел не имеет двух поддеревьев, то удаление происходит за O(1),
#    но при наличии двух поддеревьев, поиск левого потомка в правом поддереве, потребует O(H) операций.
# Итоговая временная сложность: O(H)
# Пространственная сложность
# Поиск узла O(H), т.к на сохранение стека вызовов потребуется хранить рекурсивные состояния в памяти.
# Удаление узла O(1).
# Итоговая пространственная сложность: O(H), где H это высота дерева.

from typing import Optional
import os

LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

if LOCAL:
    class Node:
        def __init__(self, left=None, right=None, value=0):
            self.right = right
            self.left = left
            self.value = value
else:
    from node import Node


def find_node_and_parent(root: Node, key: int) -> tuple[Node, Node]:
    parent: Node = None
    while root and root.value != key:
        parent = root
        if root.value > key: root = root.left
        else: root = root.right
    return parent, root


def update_node(root: Node) -> Node:
    if not root: return root
    elif not root.left: root = root.right
    elif not root.right: root = root.left
    else:
        leftmost_node: Node = root.right
        while leftmost_node.left:
            leftmost_node = leftmost_node.left
        root.value = leftmost_node.value
        root.right = remove(root.right, leftmost_node.value)
    return root


def remove(root: Optional[Node], key: int) -> Optional[Node]:
    parent, old_node = find_node_and_parent(root, key)
    new_node: Node = update_node(old_node)
    if not parent: return new_node
    if parent.left == old_node: parent.left = new_node
    else: parent.right = new_node
    return root


def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    new_head = remove(node7, 10)
    assert new_head.value == 5
    assert new_head.right is node5
    assert new_head.right.value == 8


if __name__ == '__main__':
    test()
