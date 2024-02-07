# So in its a basic inplementation of list in python. In python programming language,
# list implemented as dynamic array
# Design a Dynamic array class that support following operations:
# DynamicArray(capacity: int) - will initialize an empty array with capacity
#     of capacity, where capacity > 0
# .get(i: int) -> int - will return the element at index i.
#     if you give invalid index, method through exception ValueError
# .set(i: int, n: int) -> None - will set element at index i to n.
#     if you take a incorrect index, method through ValueError exception.
# .pushback(n: int) -> None - will push element to the end of array.
#     And it's dynamic array implementation, so if size of array fill be full,
#     capacity will be automaticly doubled.
# .popback() -> int - will pop end return element at the end of array.
#     If array size will be empty, method thorough the exception ValueEror
# .resize() -> None - will double capacity of array
# .getSize() -> int - will return the size of array
# .getCapacity() -> int: will return the capacity of array
class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.arr: list = [0] * capacity
        self.size: int = 0

    def get(self, i: int) -> int:
        if i < 0 or i > self.size:
            raise ValueError()
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i > self.size:
            raise ValueError()
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        if self.size == 0:
            raise ValueError()
        self.size -= 1
        return self.arr[self.size]

    def resize(self) -> None:
        self.capacity *= 2
        new_arr: list = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.arr[i]
        self.arr = new_arr

    def getSize(self) -> int:
        return self.size

    def getCapacity(self) -> int:
        return self.capacity