# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> List[List[int]]:
        if not root: return 0

        max_left = self.maxDepth(root.left)
        max_right = self.maxDepth(root.right)
        return 1 + max(max_left, max_right)