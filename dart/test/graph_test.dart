import 'package:dart/graph.dart';
import 'package:test/test.dart';

//     >(1)<--->(4) ---->(5)
//    /          |       /|
// (0)     ------|------- |
//    \   v      v        v
//     >(2) --> (3) <----(6)
WeightedAdjacencyMatrix matrix2 = [
  [0, 3, 1, 0, 0, 0, 0], // 0
  [0, 0, 0, 0, 1, 0, 0],
  [0, 0, 7, 0, 0, 0, 0],
  [0, 0, 0, 0, 0, 0, 0],
  [0, 1, 0, 5, 0, 2, 0],
  [0, 0, 18, 0, 0, 0, 1],
  [0, 0, 0, 1, 0, 0, 1],
];

// also known as priority queue
void main() {
  test('Test BFS graph list', () {
    expect(bfs(matrix2, 0, 6), [0, 1, 4, 5, 6]);
    expect(bfs(matrix2, 6, 2), null);
  });
}
