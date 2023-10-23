from algorithms.stack import Stack


def test_stack():
    list = Stack[int]()

    list.push(5)
    list.push(7)
    list.push(9)

    assert list.pop() == 9
    assert len(list) == 2

    list.push(11)
    assert list.pop() == 11
    assert list.pop() == 7
    assert list.peek() == 5
    assert list.pop() == 5
    assert list.pop() is None

    list.push(69)
    assert list.peek() == 69
    assert len(list) == 1

