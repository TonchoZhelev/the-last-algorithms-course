from dataclasses import dataclass
from typing import Generic, TypeVar, Self

T = TypeVar('T') 


@dataclass(slots=True)
class SNode(Generic[T]):
    value: T
    prev: Self | None = None

class Stack(Generic[T]):

    def __init__(self, *args) -> None:
        self.head: SNode[T] | None = None
        self._length: int = 0
        for arg in args:
            self.push(arg)

    def __len__(self) -> int:
        return self._length

    def push(self, item: T) -> None:
        node = SNode(value=item)
        self._length += 1
        if not self.head:
            self.head = node
            return
        else: 
            node.prev = self.head
            self.head = node

    def pop(self) -> T | None:
        head = self.head

        if self._length == 0:
            return None
        else:
            head = self.head
            self.head = head.prev if head else None

        self._length = self._length - 1
        return head.value if head else None


    def peek(self) -> T | None:
        return self.head.value if self.head is not None else None

    def __iter__(self):
        node = self.head
        while node:
            yield node.value
            node = node.prev

    def __repr__(self) -> str:
        return f'Stack({[v for v in self]})'

