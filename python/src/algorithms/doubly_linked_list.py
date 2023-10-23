from collections.abc import Generator
from typing import Self, TypeVar, Generic, overload
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Node(Generic[T]):
    value: T
    next: Self | None = None
    prev: Self | None = None
    

class DoublyLinkedList(Generic[T]):

    def __init__(self, *args: T):
        self._length = 0
        self.head: Node[T] | None = None
        self.tail: Node[T] | None = None
        for v in args:
            self.append(v)

    def __repr__(self) -> str:
        return f'DoublyLinkedList({", ".join(str(v) for v in self)})'

    def __len__(self) -> int:
        return self._length

    def get_node_iter(self) -> Generator[Node[T], None, None]:
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __iter__(self) -> Generator[T, None, None]:
        for n in self.get_node_iter():
            yield n.value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, DoublyLinkedList):
            return NotImplemented

        if len(self) != len(other):
            return False

        for a, b in zip(self, other):
            if a != b:
                return False

        return True

    def get_node(self, key: int) -> Node[T]:
        if key < 0 or key >= self._length:
            raise IndexError()
            
        for idx, node in enumerate(self.get_node_iter()):
            if idx == key:
                return node

        # should never happen, as we've already checked at the beggining
        # but python complains otherwise
        raise IndexError()

    def __getitem__(self, key: int) -> T:
        if key < 0 or key >= self._length:
            raise IndexError()

        for idx, v in enumerate(self):
            if idx == key:
                return v

        # should never happen, as we've already checked at the beggining
        # but python complains otherwise
        raise IndexError()

    def __setitem__(self, key: int, value: T) -> None:
        self.insertAt(value, key)

    def __delitem__(self, key: int) -> T | None:
        return self.remove_at(key)

    def prepend(self, item: T) -> None:
        node = Node(value=item)
        self._length += 1

        if not self.head:
            self.head = self.tail = node
            return
        
        node.next = self.head
        self.head.prev = node
        self.head = node

    def insertAt(self, item: T, idx: int) -> None:
        if idx < 0 or idx >= self._length:
            raise IndexError()
        elif idx == self._length - 1:
            self.append(item)
            return
        elif idx == 0:
            self.prepend(item)
            return

        curr = self.get_node(idx)

        node = Node(
            value = item,
            next = curr,
            prev = curr.prev)

        if curr.prev:
            curr.prev.next = node

        curr.prev = node
        self._length += 1


    def append(self, item: T) -> None:
        self._length += 1
        node = Node(value=item)

        if not self.tail:
            self.head = self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def remove_node(self, node: Node[T]) -> Node[T]:
        if self._length == 1:
            self.head = self.tail = None
            self._length -= 1
            return node
        
        if node.prev:
            node.prev.next = node.next

        if node.next:
            node.next.prev = node.prev

        if node == self.head:
            self.head = node.next

        if node == self.tail:
            self.tail = node.prev

        del node.prev
        del node.next
        self._length -= 1
        return node

    def remove(self, item: T) -> T | None:
        for curr in self.get_node_iter():
            if curr.value == item:
                return self.remove_node(curr).value
        
        return None

    def remove_at(self, idx: int) -> T | None:
        for i, curr in enumerate(self.get_node_iter()):
            if i == idx:
                return self.remove_node(curr).value
        
        return None








