from dataclasses import dataclass, field
from typing import Protocol

class Comparable(Protocol):
    def __lt__(self, other, /):
        ...

@dataclass
class MinHeap[T: Comparable]:
    _length: int = 0
    _data: list[T] = field(default_factory=list)

    def __len__(self) -> int:
        return self._length

    def insert(self, item: T):
        self._data.append(item)
        self._heapify_up(len(self))
        self._length += 1
        
    def delete(self) -> T:
        if len(self) == 0:
            raise IndexError("delete from empty heap")
            
        h = self._data[0]
        self._length -= 1

        if len(self) == 0:
            self._data.clear()
            return h
        
        # self._data[0] = self._data[len(self)]
        # self._data[len(self)] = None
        self._data[0] = self._data.pop()
        self._heapify_down(0)
        return h

    def _heapify_down(self, idx: int):
        if idx >= len(self):
            return

        li = self._left(idx)
        ri = self._right(idx)

        if li >= len(self) or ri >= len(self):
            return

        lv = self._data[li]
        rv = self._data[ri]
        v = self._data[idx]

        if lv > rv and v > rv:
            self._data[idx] = rv
            self._data[ri] = v
            self._heapify_down(ri)
        elif rv > lv and v > lv:
            self._data[idx] = lv
            self._data[li] = v
            self._heapify_down(li)

    def _heapify_up(self, idx: int): 
        if idx == 0:
            return
        
        p = self._parent(idx)
        pv = self._data[p]
        v = self._data[idx]

        if v < pv:
            self._data[idx] = pv
            self._data[p] = v
            self._heapify_up(p)

    def _parent(self, idx: int) -> int:
        return (idx - 1) // 2

    def _left(self, idx: int) -> int:
        return idx * 2 + 1

    def _right(self, idx: int) -> int:
        return idx * 2 + 2
