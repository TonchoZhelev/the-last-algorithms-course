class MinHeap<T> {
  int _length = 0;
  final _data = <T>[];

  /// compare(a, b) should return -1 if a < b, 0 if a == b, 1 if a > b
  final int Function(T, T) compare;

  MinHeap(this.compare);

  int get length => _length;

  void insert(T item) {
    _data.add(item);
    _heapifyUp(_length);
    _length++;
  }

  T delete() {
    if (_length == 0) {
      throw Exception("delete from empty heap");
    }

    final h = _data[0];
    _length--;

    if (_length == 0) {
      _data.clear();
      return h;
    }

    _data[0] = _data.removeLast();
    _heapifyDown(0);
    return h;
  }

  void _heapifyDown(int idx) {
    if (idx >= _length) return;

    final li = _left(idx);
    final ri = _right(idx);

    if (li >= _length || ri >= _length) return;

    final lv = _data[li];
    final rv = _data[ri];
    final v = _data[idx];

    if (compare(lv, rv) > 0 && compare(v, rv) > 0) {
      _data[idx] = rv;
      _data[ri] = v;
      _heapifyDown(ri);
    } else if (compare(rv, lv) > 0 && compare(v, lv) > 0) {
      _data[idx] = lv;
      _data[li] = v;
      _heapifyDown(li);
    }
  }

  void _heapifyUp(int idx) {
    if (idx == 0) return;

    final p = _parent(idx);
    final pv = _data[p];
    final v = _data[idx];

    if (compare(v, pv) < 0) {
      _data[idx] = pv;
      _data[p] = v;
      _heapifyUp(p);
    }
  }

  int _parent(int idx) => (idx - 1) ~/ 2;

  int _left(int idx) => idx * 2 + 1;

  int _right(int idx) => idx * 2 + 2;
}
