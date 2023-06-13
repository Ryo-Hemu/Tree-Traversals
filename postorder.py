# Post-Order Traversal
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root):
        from collections import deque

        if not root:
            return []
        stack, result = [root], deque()
        while stack:
            current = stack.pop()
            result.appendleft(current)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)
        return result


class SolutionRecursive:
    def postOrderTraversal(self, root):
        if not root:
            return []
        return (
            self.postOrderTraversal(root.left)
            + self.postOrderTraversal(root.right)
            + [root.val]
        )
