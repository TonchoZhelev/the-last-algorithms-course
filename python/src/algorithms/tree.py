from dataclasses import dataclass
from typing import Self


@dataclass
class BinaryNode[T]:
    value: T
    left: Self | None = None
    right: Self | None = None

    def __eq__(self, other) -> bool:
        if not isinstance(other, BinaryNode):
            return False

        return (self.value == other.value
                and self.left == other.left
                and self.right == other.right)



def pre_order_search[T](head: BinaryNode[T]) -> list[T]:
    """Return a list of values from a pre-order search of the tree."""
    def walk(curr: BinaryNode[T] | None, path: list[T]) -> list[T]:
        if curr is None:
            return path

        #pre 
        path.append(curr.value)

        #recurse
        walk(curr.left, path)
        walk(curr.right, path)

        #post
        return path


    return walk(head, [])

def in_order_search[T](head: BinaryNode[T]) -> list[T]:
    """Return a list of values from a in-order search of the tree."""
    def walk(curr: BinaryNode[T] | None, path: list[T]) -> list[T]:
        if curr is None:
            return path

        #pre
        walk(curr.left, path)

        #recurse
        path.append(curr.value)
        walk(curr.right, path)

        #post
        return path


    return walk(head, [])

def post_order_search[T](head: BinaryNode[T]) -> list[T]:
    """Return a list of values from a post-order search of the tree."""
    def walk(curr: BinaryNode[T] | None, path: list[T]) -> list[T]:
        if curr is None:
            return path

        #pre
        #recurse
        walk(curr.left, path)
        walk(curr.right, path)

        #post
        path.append(curr.value)
        return path


    return walk(head, [])

def breadth_first_search[T](head: BinaryNode[T], needle: T) -> bool:
    """Return True if the needle is in the tree, False otherwise."""
    q = [head]

    while q:
        curr = q.pop(0)

        if curr and curr.value == needle:
            return True
        
        if curr.left:
            q.append(curr.left)

        if curr.right:
            q.append(curr.right)

    return False

