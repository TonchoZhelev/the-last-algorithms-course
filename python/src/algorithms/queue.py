from typing import Generic, TypeVar, Self
from dataclasses import dataclass

T = TypeVar('T')


@dataclass(slots=True)
class QNode(Generic[T]):
    """A List Node for the Queue"""
    value: T
    next: Self | None = None


class Queue(Generic[T]):
    """A generic queue implementation"""

    def __init__(self, *args: T):
        self.length: int = 0
        self.head: QNode[T] | None = None
        self.tail: QNode[T] | None = None
        for a in args:
            self.enqueue(a)

    def enqueue(self, item: T) -> None:
        node = QNode(item)

        if self.tail is None:
            self.tail = node
            self.head = node
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def deque(self) -> T | None:
        if self.head is None:
            return None

        head = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.length -= 1

        return head.value

    def peek(self) -> T | None:
        return self.head.value if self.head is not None else None

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        return f"Queue([{', '.join(map(repr, self))}])"
