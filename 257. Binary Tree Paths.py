# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root):
        result = []
        if root:
            self.dfs(root, "", result)
        return result

    def dfs(self, node, path, result):
        path += str(node.val)
        if not node.left and not node.right:
            result.append(path)
            return
        if node.left:
            self.dfs(node.left, path + "->", result)
        if node.right:
            self.dfs(node.right, path + "->", result)


# Create the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)

# Test the Solution
solution = Solution()
output = solution.binaryTreePaths(root)
print(output)  # Output: ["1->2->5", "1->3"]
