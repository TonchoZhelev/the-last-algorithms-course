from dataclasses import dataclass, astuple

@dataclass(slots=True)
class Point:
    x: int = 0
    y: int = 0

directions = [
    (-1, 0),
    ( 1, 0),
    ( 0,-1),
    ( 0, 1),
]

def walk(maze: list[str], wall: str,\
         current: Point, end: Point,\
         seen: list[list[bool]], path: list[Point]) -> bool:
    # off the map
    if current.x < 0 or current.x >= len(maze[0]) \
        or current.y < 0 or current.y >= len(maze):
        return False

    # on a wall
    if maze[current.y][current.x] == wall:
        return False

    if current == end:
        path.append(current)
        return True

    if seen[current.y][current.x]:
        return False

    # pre
    seen[current.y][current.x] = True
    path.append(current)

    for i in directions:
        x, y = i
        succ = walk(maze, wall,\
                    Point(x = current.x + x, y = current.y + y),\
                    end, seen, path)
        if succ:
            return True

    # post
    path.pop()

    return False


def solve(maze: list[str], wall: str, start: Point, end: Point) -> list[Point]:
    # this used to be [[False] * len(maze[0])] * len(maze)
    # NEVER do this, all the columns end up pointing 
    # at the same instance of the first array
    seen: list[list[bool]] = [[False] * len(maze[0]) for _ in maze] # fill seen with Falses
    path: list[Point] = []

    walk(maze, wall, start, end, seen, path)

    return path
