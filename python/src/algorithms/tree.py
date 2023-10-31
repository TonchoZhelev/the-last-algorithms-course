from dataclasses import dataclass
from typing import Protocol, Self, runtime_checkable

@runtime_checkable
class Comparable(Protocol):
    def __le__(self, other,/) -> bool:
        ...

    def __lt__(self, other,/) -> bool:
        ...

    def __eq__(self, other,/) -> bool:
        ...

    def __gt__(self, other,/) -> bool:
        ...


class TestFunc[T: Comparable](Protocol):
    def __call__(self, curr: "BinaryNode[T]") -> bool:
        ...



class BinaryNode[T: Comparable]:

    def __init__(self, value: T, 
                 left: Self | None = None,
                 right: Self | None = None) -> None:
        self.value = value
        self.height: int = 1

        if left:
            self.left = left

            if self.right is None or self.left.height >= self.right.height:
                self.height += 1

        if right:
            self.right = right

            if self.left is None or self.right.height >= self.left.height:
                self.height += 1
        

    def __eq__(self, other) -> bool:
        if not isinstance(other, BinaryNode):
            return False

        return (self.value == other.value
                and self.left == other.left
                and self.right == other.right)

    def find(self, needle: T) -> tuple[Self | None, Self | None]:
        if self.value == needle:
            return (self, None)

        def inject_parent(t):
            if not t or not t[0]:
                return (None, None)

            if t[1]:
                return t
            else:
                return (t[0], self)

        if needle < self.value and self.left:
            left = self.left.find(needle)
            return inject_parent(left)
        elif needle > self.value and self.right:
            right = self.right.find(needle)
            return inject_parent(right)

        return (None, None)


    def insert(self, item: T) -> None:
        if item <= self.value:
            if self.left is not None:
                self.left.insert(item)
            else:
                self.left = BinaryNode(value=item)

            if self.right is None or self.left.height >= self.right.height:
                self.height += 1
        else:
            if self.right is not None:
                self.right.insert(item)
            else:
                self.right = BinaryNode(value=item)

            if self.left is None or self.right.height >= self.left.height:
                self.height += 1


    def remove(self, item: T) -> None:
        child, parent = self.find(item)

        # Node not found
        if not child or not parent:
            return

        match (child.left, child.right):
            case (None, None):  # Node with no children
                if parent.left is child:
                    parent.left = None
                else:
                    parent.right = None
            
            case (_, None):  # Node with only left child
                if parent.left is child:
                    parent.left = child.left
                else:
                    parent.right = child.left
            
            case (None, _):  # Node with only right child
                if parent.left is child:
                    parent.left = child.right
                else:
                    parent.right = child.right

            case (left, right) if left.height >= right.height:
                # Replace with predecessor (largest in left subtree)
                largest_parent = child
                largest = child.left
                while largest.right:
                    largest_parent = largest
                    largest = largest.right

                if largest.left:
                    largest_parent.right = largest.left

                child.value = largest.value
            
            case (left, right) if left.height < right.height:
                # Replace with successor (smallest in right subtree)
                smallest_parent = child
                smallest = child.right
                while smallest.left:
                    smallest_parent = smallest
                    smallest = smallest.left

                if smallest.right:
                    smallest_parent.left = smallest.right

                child.value = smallest.value
        

def pre_order_search[T: Comparable](head: BinaryNode[T]) -> list[T]:
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

def in_order_search[T: Comparable](head: BinaryNode[T]) -> list[T]:
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

def post_order_search[T: Comparable](head: BinaryNode[T]) -> list[T]:
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

def breadth_first_search[T: Comparable](head: BinaryNode[T], needle: T) -> bool:
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

