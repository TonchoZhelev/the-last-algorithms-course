from math import sqrt, floor


def two_cristal_balls(breaks: list[bool]) -> int:
    lenBreaks = len(breaks)
    jmpAmount = floor(sqrt(lenBreaks))

    i = jmpAmount

    while i < lenBreaks:
        if breaks[i]:
            break
        i += jmpAmount

    i -= jmpAmount

    j = 0

    while j < jmpAmount and i < lenBreaks:
        if breaks[i]:
            return i
        j += 1
        i += 1

    return -1


def two_cristal_balls2(breaks: list[bool]) -> int:
    lenBreaks = len(breaks)
    jmpAmount = floor(sqrt(lenBreaks))

    for i in range(jmpAmount, lenBreaks, jmpAmount):
        if breaks[i]:
            break

    i -= jmpAmount

    j = 0

    while j < jmpAmount and i < lenBreaks:
        if breaks[i]:
            return i
        j += 1
        i += 1

    return -1
