import unittest
import pytest

from algorithms.binary_search import binary_search


def test_binary_search():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert binary_search(foo, 69) is True
    assert binary_search(foo, 1336) is False
    assert binary_search(foo, 69420) is True
    assert binary_search(foo, 69421) is False
    assert binary_search(foo, 1) is True
    assert binary_search(foo, 0) is False
