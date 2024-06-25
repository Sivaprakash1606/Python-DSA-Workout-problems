class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root):
        if root is None:
            return []

        result = []
        queue = [root]

        while queue:
            level_sum = 0
            level_size = len(queue)

            for _ in range(level_size):
                current = queue.pop(0)
                level_sum += current.val

                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            result.append(level_sum / level_size)

        return result

# Create the tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

# Instantiate the solution class
sol = Solution()

# Get the result
output = sol.averageOfLevels(root)
print(output)
