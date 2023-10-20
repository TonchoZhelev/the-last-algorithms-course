import pytest
import unittest

from algorithms.bubble_sort import bubble_sort


def test_bubble_sort():
    arr = [9, 3, 7, 4, 69, 420, 42]

    bubble_sort(arr)

    assert arr == [3, 4, 7, 9, 42, 69, 420]
