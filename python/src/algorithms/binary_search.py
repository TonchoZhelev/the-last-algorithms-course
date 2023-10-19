def binary_search(haystack: list[int], needle: int) -> bool:
    """Return True if needle is in haystack, False otherwise."""
    lo: int = 0
    hi: int = len(haystack)

    while lo < hi:
        m = lo + ((hi - lo) // 2)
        v = haystack[m]
        if v == needle:
            return True
        elif v > needle:
            hi = m
        else:
            lo = m + 1

    return False
