import math
from typing import Any, Iterator, List, Union

from softwareproperties.gtk.utils import retry


class DynamicArray:
    def __init__(self, capacity: int = 10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive integer.")
        self.__capacity = capacity
        self.__size = 0
        self.__array: List[Any] = [None] * capacity

    def __getitem__(self, index):
        if index > self.__size:
            raise "Out of range"
        elif 0 <= index <= self.__size - 1:
            return self.__array[index]
        elif index < 0:
            return self.__array[self.__size - index - 1]

    def __setitem__(self, key, value):
        if key > self.__size - 1:
            raise "out of range"
        elif self.__size - 1 > key >= 0:
            self.__array[key] = value
        elif key < 0 and abs(key) < self.__size:
            self.__array[self.__size + key] = value
        else:
            raise "out of range"

    def __len__(self):
        return self.__size

    def __new_size(self, new_size):
        new_list = [None] * new_size
        for i in range(new_size):
            new_list[i] = self.__array[i]
        self.__array = new_list
        self.__size = new_size

    def append(self, item):
        if self.__size == self.__capacity:
            self.__new_size(2 * self.__capacity)
        self.__array[self.__size] = item
        self.__size += 1

    def __str__(self) -> str:

        return str([self.__array[i] for i in range(self.__size)])

    def __repr__(self) -> str:
        return f"DynamicArray({[self.__array[i] for i in range(self.__size)]})"

    def __add__(self, other: 'DynamicArray') -> 'DynamicArray':
        if isinstance(other, DynamicArray):
            new_array = DynamicArray(self.__size + other.__size)
            for i in range(self.__size):
                new_array.append(self.__array[i])
            for i in range(other.__size):
                new_array.append(other.__array[i])
            return new_array
        raise TypeError("Can only concatenate with another DynamicArray.")

    def __iadd__(self, other: 'DynamicArray') -> 'DynamicArray':
        if isinstance(other, DynamicArray):
            for i in range(other.__size):
                self.append(other.__array[i])
            return self
        raise TypeError("Can only concatenate with another DynamicArray.")

    def __eq__(self, other: Any) -> bool:
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

    # Implement other rich comparison methods (<=, >, >=) similarly.
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




