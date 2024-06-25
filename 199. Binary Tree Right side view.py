
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root, targetSum: int) -> bool:
        if not root:
            return False

        left = root.val
        right = root.val

        if root.left:
            if self.dfs(root.left, left + root.left.val, targetSum):
                return True
        if root.right:
            if self.dfs(root.right, right + root.right.val, targetSum):
                return True
        return False

    def dfs(self, root, total, targetSum):
        if root.left is None and root.right is None and total == targetSum:
            e=total
            return True

        if root.left:
            a=root.val
            b=total
            if self.dfs(root.left, total + root.left.val, targetSum):
                return True
        if root.right:
            c=root.val
            d=total
            if self.dfs(root.right, total + root.right.val, targetSum):
                return True
        return False


# Helper function to build a binary tree from a list representation
def build_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        current = queue.pop(0)
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

# Test case
input_list = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]
root = build_tree_from_list(input_list)
targetSum = 22

solution = Solution()
print(solution.hasPathSum(root, targetSum))  # Expected output: True
