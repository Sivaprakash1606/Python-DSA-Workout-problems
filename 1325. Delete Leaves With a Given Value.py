# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def removeLeafNodes(self, root, target: int):
        if root:
            return self.dfs(root, target)
        return None

    def dfs(self, root, target):
        if not root:
            return None
        queue=root.val

        root.left = self.dfs(root.left, target)
        root.right = self.dfs(root.right, target)

        if root.left is None and root.right is None and root.val == target:
            return None

        return root


# Function to build a binary tree from a list representation
def build_tree(nodes):
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        current = queue.pop(0)
        if nodes[i] is not None:
            current.left = TreeNode(nodes[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes) and nodes[i] is not None:
            current.right = TreeNode(nodes[i])
            queue.append(current.right)
        i += 1
    return root


# Function to print the binary tree level by level
def print_tree(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
        else:
            result.append(None)
    return result


# Input
input_list = [1, 2, 3, 2, None, 2, 4]
target = 2

# Build the binary tree
root = build_tree(input_list)

# Create Solution object
solution = Solution()

# Remove leaf nodes with the target value
result_root = solution.removeLeafNodes(root, target)

# Print the resulting tree level by level
print(print_tree(result_root))
