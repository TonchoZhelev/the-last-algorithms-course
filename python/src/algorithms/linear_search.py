def linear_search(haystack: list[int], needle: int) -> bool:
    """Return True if needle is in haystack, False otherwise."""
    for item in haystack:
        if item == needle:
            return True
    return False
