import random

from algorithms.search_crystal_balls import (two_cristal_balls,
                                             two_cristal_balls2)


def test_crystal_balls():
    random.seed()
    idx = random.randrange(10000)

    data = [x >= idx for x in range(10000)]

    assert two_cristal_balls(data) == idx
    assert two_cristal_balls([False for _ in range(821)]) == -1


def test_crystal_balls2():
    random.seed()
    idx = random.randrange(10000)

    data = [x >= idx for x in range(10000)]

    assert two_cristal_balls2(data) == idx
    assert two_cristal_balls2([False for _ in range(821)]) == -1
