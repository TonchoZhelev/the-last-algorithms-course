from algorithms.quick_sort import quick_sort

def test_quick_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]
    quick_sort(arr)
    assert arr == [3, 4, 7, 9, 42, 69, 420]
