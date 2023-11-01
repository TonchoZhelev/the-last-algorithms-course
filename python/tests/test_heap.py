from algorithms.heap import MinHeap

#also known as priority queue

def test_heap():
    heap = MinHeap()

    assert len(heap) == 0

    heap.insert(5)
    heap.insert(3)
    heap.insert(69)
    heap.insert(420)
    heap.insert(4)
    heap.insert(1)
    heap.insert(8)
    heap.insert(7)

    assert len(heap) == 8
    assert heap.delete() == 1
    assert heap.delete() == 3
    assert heap.delete() == 4
    assert heap.delete() == 5
    assert len(heap) == 4
    assert heap.delete() == 7
    assert heap.delete() == 8
    assert heap.delete() == 69
    assert heap.delete() == 420
    assert len(heap) == 0

