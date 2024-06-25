# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root):
        if root is None:
            return []
        result = []
        self.postorder(root, result)
        return result

    def postorder(self, root, result):
        if root is None:
            return

        queue=[root.val]
        self.postorder(root.left, result)
        self.postorder(root.right, result)
        result.append(root.val)


# Create the binary tree
root = TreeNode(1)
root.right = TreeNode(2)
root.left = TreeNode(0)
root.right.left = TreeNode(3)

# Instantiate the Solution class
solution = Solution()

# Call the postorderTraversal method
output = solution.postorderTraversal(root)
print(output)  # Output should be: [3, 2, 1]
