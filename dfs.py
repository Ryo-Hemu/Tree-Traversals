# Depth-First Search or Pre-Order Traversal


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Iterative Solution
class Solution:
    def preorderTraversal(self, root):
        if not root:
            return []
        result, stack = [], [root]
        while stack:
            current = stack.pop()
            result.append(current.val)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        return result


class SolutionRecursive:
    def preorderTraversal(self, root):
        if not root:
            return []
        return (
            [root.val]
            + self.preorderTraversal(root.left)
            + self.preorderTraversal(root.right)
        )
