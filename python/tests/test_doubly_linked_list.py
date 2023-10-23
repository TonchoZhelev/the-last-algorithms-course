from algorithms.doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list():
    breakpoint()
    list = DoublyLinkedList[int]()

    list.append(5)
    list.append(7)
    list.append(9)

    assert list[2] == 9
    assert list.remove_at(1) == 7
    assert len(list) == 2

    list.append(11)
    assert list.remove_at(1) == 9
    assert list.remove(9) == None
    assert list.remove_at(0) == 5
    assert list.remove_at(0) == 11
    assert len(list) == 0

    list.prepend(5)
    list.prepend(7)
    list.prepend(9)

    assert list[2] == 5
    assert list[0] == 9
    assert list.remove(9) == 9
    assert len(list) == 2
    assert list[0] == 7
