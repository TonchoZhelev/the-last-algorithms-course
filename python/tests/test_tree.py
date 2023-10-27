from algorithms.tree import (BinaryNode, pre_order_search, in_order_search,
    post_order_search, breadth_first_search)

tree = BinaryNode(
    value = 20,
    right = BinaryNode(
        value = 50,
        right = BinaryNode(value = 100),
        left = BinaryNode(
            value = 30,
            right = BinaryNode(value = 45),
            left = BinaryNode(value = 29),
        ),
    ),
    left = BinaryNode(
        value = 10,
        right = BinaryNode(value = 15),
        left = BinaryNode(
            value = 5,
            right = BinaryNode(value = 7),
        ),
    ),
)

tree2 = BinaryNode(
    value = 20,
    right = BinaryNode(
        value = 50,
        left = BinaryNode(
            value = 30,
            right = BinaryNode(
                value = 45,
                right = BinaryNode(
                    value = 49,
                ),
            ),
            left = BinaryNode(
                value = 29,
                left = BinaryNode(
                    value = 21,
                ),
            )
        ),
    ),
    left = BinaryNode(
        value = 10,
        right = BinaryNode(
            value = 15,
        ),
        left = BinaryNode(
            value = 5,
            right = BinaryNode(
                value = 7,
            ),
        )
    )
)

def test_binary_trees():
    assert tree == tree
    assert tree != tree2

def test_binary_tree_pre_order():
    assert pre_order_search(tree) == [20, 10, 5, 7, 15, 50, 30, 29, 45, 100]

def test_binary_tree_in_order():
    assert in_order_search(tree) == [5, 7, 10, 15, 20, 29, 30, 45, 50, 100]

def test_binary_tree_post_order():
    assert post_order_search(tree) == [7, 5, 15, 10, 29, 45, 30, 100, 50, 20]

def test_breadth_first_search():
    assert breadth_first_search(tree, 45) == True
    assert breadth_first_search(tree, 7) == True
    assert breadth_first_search(tree, 69) == False
