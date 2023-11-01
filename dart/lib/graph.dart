typedef WeightedAdjacencyMatrix = List<List<int>>;

List<int>? bfs(
  WeightedAdjacencyMatrix graph,
  int source,
  int needle,
) {
  final seen = [for (final _ in graph) false];
  final prev = [for (final _ in graph[0]) -1];

  seen[source] = true;
  final q = [source];

  do {
    final curr = q.removeAt(0);
    if (curr == needle) {
      break;
    }

    final adjs = graph[curr];
    for (var i = 0; i < graph.length; i++) {
      if (adjs[i] == 0) {
        continue;
      }

      if (seen[i]) {
        continue;
      }

      seen[i] = true;
      prev[i] = curr;
      q.add(i);
    }

    seen[curr] = true;
  } while (q.isNotEmpty);

  var curr = needle;
  final out = <int>[];

  while (prev[curr] != -1) {
    out.add(curr);
    curr = prev[curr];
  }

  if (out.isNotEmpty) {
    return [source, ...out.reversed];
  }

  return null;
}
