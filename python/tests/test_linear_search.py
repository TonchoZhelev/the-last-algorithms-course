import unittest
import pytest

from algorithms.linear_search import linear_search


def test_linear_search():
    foo = [1, 3, 4, 69, 71, 81, 90, 99, 420, 1337, 69420]
    assert linear_search(foo, 69) is True
    assert linear_search(foo, 1336) is False
    assert linear_search(foo, 69420) is True
    assert linear_search(foo, 69421) is False
    assert linear_search(foo, 1) is True
    assert linear_search(foo, 0) is False
