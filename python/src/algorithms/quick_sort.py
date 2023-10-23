

def qs(arr: list[int], lo: int, hi: int) -> None:
    if lo >= hi:
        return
    
    pivotIdx = partition(arr, lo, hi)

    qs(arr, lo, pivotIdx - 1)
    qs(arr, pivotIdx + 1, hi)


def partition(arr: list[int], lo: int, hi: int) -> int:
    # we use the last element as the pivot for simplicity
    # but this is not the best choice
    pivot = arr[hi]
    idx = lo - 1

    for i in range(lo, hi):
        if arr[i] <= pivot:
            idx += 1
            tmp = arr[i]
            arr[i] = arr[idx]
            arr[idx] = tmp

    idx += 1
    arr[hi] = arr[idx]
    arr[idx] = pivot

    return idx


def quick_sort(arr: list[int]) -> None:
    qs(arr, 0, len(arr) - 1)

