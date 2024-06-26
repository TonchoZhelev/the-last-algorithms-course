from algorithms.queue import Queue


def test_queue():
    list = Queue[int]()

    list.enqueue(5)
    list.enqueue(7)
    list.enqueue(9)

    assert list.deque() == 5
    assert len(list) == 2

    list.enqueue(11)

    assert list.deque() == 7
    assert list.deque() == 9
    assert list.peek() == 11
    assert list.deque() == 11
    assert list.deque() is None
    assert len(list) == 0

    list.enqueue(69)

    assert list.peek() == 69
    assert len(list) == 1
