from typing import Any, Protocol
from time import perf_counter_ns
from random import random

class TestFunc(Protocol):
    def __call__(self) -> Any:
        ...

a: list[float] = []

def time(fn: TestFunc) -> int:
    now = perf_counter_ns()
    fn();
    return perf_counter_ns() - now


def unshift(num: int):
    for _ in range(num):
        a.insert(0, random())

def shift(num: int): 
    for _ in range(num):
        a.pop(0)

def push(num: int):
    for _ in range(num):
        a.append(random())

def pop(num: int):
    for _ in range(num):
        a.pop()

def get(idx: int):
    return lambda: a[idx]

def push_arr(count: int):
    return lambda: push(count)

def pop_arr(count: int):
    return lambda: pop(count)

def unshift_arr(count: int):
    return lambda: unshift(count)

def shift_arr(count: int):
    return lambda: shift(count)

tests = [10, 100, 1000, 10000, 100000, 1_000_000, 10_000_000];

print("Testing get")
for t in tests:
    a.clear()
    push(t)
    print(t, time(get(t - 1)))

print("push")
for t in tests:
    a.clear()
    push(t)
    print(t, time(push_arr(1000)))

print("pop")
for t in tests:
    a.clear()
    push(t)
    print(t, time(pop_arr(min(t, 1000))))

print("unshift")
for t in tests:
    a.clear()
    push(t)
    print(t, time(unshift_arr(1000)))

print("shift")
for t in tests:
    a.clear()
    push(t)
    print(t, time(shift_arr(min(t, 1000))))
