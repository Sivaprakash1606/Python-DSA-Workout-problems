# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        a=root.val

        # Swap the left and right children
        temp = root.left
        root.left = root.right
        root.right = temp


        # Recursively invert the left and right subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# Helper function to insert nodes into the tree level by level
from collections import deque

def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):  # Corrected line
        current = queue.popleft()
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root


# Helper function to print the tree in level order for verification
def print_tree_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        current = queue.popleft()
        result.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return result


# Test case
input_list = [4, 2, 7, 1, 3, 6, 9]
root = build_tree_from_list(input_list)

solution = Solution()
inverted_root = solution.invertTree(root)

# Print the tree after inversion
print(print_tree_level_order(inverted_root))
