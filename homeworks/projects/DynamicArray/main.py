import math, array
from typing import Iterator, Any


class DynamicArray:
    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive.")
        self.__capacity = capacity
        self.__size = 0
        self.__array = [0] * capacity

    def __getitem__(self, index):
        if isinstance(index, int):
            if index >= 0 and index > self.__size:
                raise IndexError
            elif index < 0 and abs(index) <= self.__size:
                return self.__array[index]
            elif 0 <= index < self.__size:
                return self.__array[index]
        raise TypeError

    def __setitem__(self, index: int, value: int):
        if isinstance(value, int) and isinstance(index, int):
            if index < -self.__size or index >= self.__size:
                raise IndexError
            self.__array[index] = value
        else:
            raise TypeError

    def __len__(self):
        return self.__size

    def resize(self):
        new_capacity = 2 * self.__capacity
        new_list = self.__capacity * [0]
        for i in range(self.__size):
            new_list[i: int] = self.__array[i]
        self.__array = new_list
        self.__capacity = new_capacity


    def __str__(self) -> str:
        return str([self.__array[i] for i in range(self.__size)])

    def __repr__(self) -> str:
        return f"DynamicArray({[self.__array[i] for i in range(self.__size)]})"

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        if isinstance(other, DynamicArray):
            new_capacity = self.__capacity + other.__capacity
            new_array = DynamicArray(new_capacity)
            new_array.__size = self.__size + other.__size
            for i in range(self.__size):
                new_array.__array[i] = self.__array[i]
            for i in range(other.__size):
                new_array.__array[self.__size + i] = other.__array[i]
            return new_array
        raise TypeError

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        result = self.__add__(other)
        self.__array = result.__array
        self.__size = result.__size
        self.__capacity = result.__capacity
        return self

    def append(self, value: int):
        if self.__size == self.__capacity:
            self.resize()
        self.__array[self.__size] = value
        self.__size += 1

    def __eq__(self, other) -> bool:
        if not isinstance(other, DynamicArray):
            return False
        if self.__size != other.__size:
            return False
        for i in range(self.__size):
            if self.__array[i] != other.__array[i]:
                return False
        return True

    def __lt__(self, other: 'DynamicArray') -> bool:
        if not isinstance(other, DynamicArray):
            return NotImplemented
        return self.__array[:self.__size] < other.__array[:other.__size]

    def __le__(self, other: 'DynamicArray') -> bool:
        return self < other or self == other

    def __gt__(self, other: 'DynamicArray') -> bool:
        return not (self <= other)

    def __ge__(self, other: 'DynamicArray') -> bool:
        return not (self < other)

    def __iter__(self) -> Iterator[Any]:
        self._index = 0
        return self

    def __next__(self) -> Any:
        if self._index < self.__size:
            result = self.__array[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __hash__(self) -> int:
        raise TypeError("DynamicArray objects are mutable and cannot be hashed")


# arr1 = DynamicArray()
# arr2 = DynamicArray()
# arr1.append(20)
# arr2.append(50)
# print(arr1)
# print(arr2)
# print(arr1 + arr2)
# arr1 += arr2
# print(arr1)
# print(arr1.__getitem__(1))




