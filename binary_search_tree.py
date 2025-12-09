"""
Binary Search Tree (BST) Implementation
Author: Adam Trepáč
Description: A standard implementation of a BST with insertion, search (iterative & recursive),
minimum value retrieval, and validation logic.
"""

from typing import Any, Optional, List

class Node:
    """Represents a single node in the Binary Search Tree."""
    def __init__(self, key: Any = None) -> None:
        self.key: Any = key
        self.parent: Optional['Node'] = None
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None

class BinarySearchTree:
    """Represents the Binary Search Tree structure."""
    def __init__(self) -> None:
        self.root: Optional[Node] = None

def insert(tree: BinarySearchTree, key: Any) -> None:
    """
    Inserts a new key into the BST while maintaining tree properties.
    Time Complexity: O(h), where h is the tree height.
    """
    new_node = Node(key)
    parent = None
    current = tree.root
    
    # Find the correct position for the new node
    while current is not None:
        parent = current
        if key < current.key:
            current = current.left
        else:
            current = current.right
            
    # Attach the new node
    new_node.parent = parent
    if parent is None:
        tree.root = new_node
    elif key < parent.key:
        parent.left = new_node
    else:
        parent.right = new_node

def get_minimum(tree: BinarySearchTree) -> Optional[Any]:
    """Returns the minimum key value found in the tree."""
    current = tree.root
    if current is None:
        return None
        
    # Go as far left as possible
    while current.left is not None:
        current = current.left
    return current.key

def search_recursive(tree: BinarySearchTree, key: Any) -> Optional[Node]:
    """Recursively searches for a node with the given key."""
    def _search_helper(current: Optional[Node]) -> Optional[Node]:
        if current is None or current.key == key:
            return current
        if key < current.key:
            return _search_helper(current.left)
        return _search_helper(current.right)

    return _search_helper(tree.root)

def search_iterative(tree: BinarySearchTree, key: Any) -> Optional[Node]:
    """Iteratively searches for a node with the given key (Memory efficient)."""
    current = tree.root
    while current is not None and current.key != key:
        if key < current.key:
            current = current.left
        else:
            current = current.right
    return current

def is_valid_bst(tree: BinarySearchTree) -> bool:
    """
    Validates if the tree adheres to Binary Search Tree properties.
    Strategy: In-order traversal of a valid BST must be sorted.
    """
    keys = []

    def _inorder_collect(node: Optional[Node]):
        if node is not None:
            _inorder_collect(node.left)
            keys.append(node.key)
            _inorder_collect(node.right)

    _inorder_collect(tree.root)

    # Check if the collected keys are in strictly ascending order
    for i in range(1, len(keys)):
        if keys[i] <= keys[i - 1]:
            return False
    return True

# --- Main Execution for Demonstration ---
if __name__ == "__main__":
    print("--- Binary Search Tree Demo ---")
    
    bst = BinarySearchTree()
    values = [10, 5, 15, 3, 7, 12, 18]
    
    print(f"Inserting values: {values}")
    for v in values:
        insert(bst, v)

    min_val = get_minimum(bst)
    print(f"Minimum value: {min_val}")  # Should be 3

    search_key = 7
    found_node = search_iterative(bst, search_key)
    print(f"Search for {search_key}: {'Found' if found_node else 'Not Found'}")

    validity = is_valid_bst(bst)
    print(f"Is tree valid?: {validity}")
