from algorithms.maze_solver import solve as maze_solver, Point

def drawPath(data: list[str], path: list[Point]):
    data2 = [[*row] for row in data]

    for p in path:
        if data2[p.y] and data2[p.y][p.x]:
            data2[p.y][p.x] = '*'

    return [''.join(c) for c in data2]

def test_maze_solver():
    maze = [
        "xxxxxxxxxx x",
        "x        x x",
        "x        x x",
        "x xxxxxxxx x",
        "x          x",
        "x xxxxxxxxxx",
    ]

    mazeResult = [
       Point(x = 10, y = 0 ),
       Point(x = 10, y = 1 ),
       Point(x = 10, y = 2 ),
       Point(x = 10, y = 3 ),
       Point(x = 10, y = 4 ),
       Point(x = 9, y = 4 ),
       Point(x = 8, y = 4 ),
       Point(x = 7, y = 4 ),
       Point(x = 6, y = 4 ),
       Point(x = 5, y = 4 ),
       Point(x = 4, y = 4 ),
       Point(x = 3, y = 4 ),
       Point(x = 2, y = 4 ),
       Point(x = 1, y = 4 ),
       Point(x = 1, y = 5 ),
    ]

    result = maze_solver(maze, "x", Point(x = 10, y = 0), Point(x = 1, y = 5))
    assert result == mazeResult
    assert drawPath(maze, result) == drawPath(maze, mazeResult)

