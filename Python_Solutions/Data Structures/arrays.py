# So in its a basic inplementation of list in python. In python programming language,
# list implemented as dynamic array
# Design a Dynamic array class that support following operations:
# DynamicArray(capacity: int) - will initialize an empty array with capacity
#     of capacity, where capacity > 0
# .get(i: int) -> object - will return the element at index i.
#     if you give invalid index, method through exception ValueError
# .set(i: int, n: object) -> None - will set element at index i to n.
#     if you take a incorrect index, method through ValueError exception.
# .add(n: object) -> None - will push element to the end of array.
#     And it's dynamic array implementation, so if size of array fill be full,
#     capacity will be automaticly doubled.
# .popback() -> object - will pop end return element at the end of array.
#     If array size will be empty, method thorough the exception ValueEror
# .resize() -> None - will double capacity of array
# .getSize() -> int - will return the size of array
# .getCapacity() -> int: will return the capacity of array
# .clear() -> None - will clear all data in array
# .is_empty() -> bool - return True if array is not emtpy othewise, return False
# .removeAt(i: int) -> obj - will remove elements by given index and return it. If given index invalid
#     method will raise exception
# .remove(obj: object) -> bool - will delete given object and return True if object exist, otherwise return False
# .indexOf(obj: object) -> int - will return index of given number if object exist, otherwise return -1
# .contains(obj: object) -> bool - will return boolean True if array have given object otherwise False
# .__iter__() - by this method we can iterate through arra
# .__next__() - by this method we can get next element of array
class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity: int = capacity
        self.arr: list = [0] * capacity
        self.size: int = 0

    def get(self, i: int) -> object:
        if i < 0 or i > self.size:
            raise ValueError()
        return self.arr[i]

    def set(self, i: int, n: object) -> None:
        if i < 0 or i > self.size:
            raise ValueError()
        self.arr[i] = n

    def add(self, n: object) -> None:
        if self.size + 1 > self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> object:
        if self.is_empty():
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

    def clear(self) -> None:
        for i in range(self.size):
            self.arr[i] = None
        self.size = 0

    def is_empty(self) -> bool:
        return self.size > 0

    def removeAt(self, i: int) -> object:
        if i > self.size or i < 0:
            raise ValueError()
        data = self.arr[i]
        new_arr: list = [0] * (self.size - 1)
        index_of_new_arr: int = 0
        for j in range(self.size):
            if j != i:
                new_arr[index_of_new_arr] = self.arr[j]
        self.arr = new_arr
        self.size -= 1
        self.capacity = self.size
        self.count = 0
        return data

    def remove(self, n: object) -> bool:
        for i in range(self.size):
            if self.arr[i] == n:
                self.removeAt(i)
                return True
        return False

    def indexOf(self, obj: object) -> int:
        for i in range(self.size):
            if self.arr[i] == obj:
                return i
        return -1

    def contains(self, obj: object) -> bool:
        return self.indexOf(obj) != -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.size:
            element = self.arr[self.count]
            self.count += 1
            return element
        else:
            self.count = 0
            raise StopIteration