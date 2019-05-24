# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

'''
complexity for both algorithms are O(n)

'''
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        dq = collections.deque()
        res = []
        dq.append(root)

        while dq:
            size = len(dq)

            cur_level = []
            for _ in range(size):
                node = dq.popleft()
                cur_level.append(node.val)

                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            res.append(cur_level)

        return res


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        res = []
        self._dfs(res, root, 0)
        return res

    def _dfs(self, res, node, level):
        if not node: return

        if len(res) < level + 1:
            res.append([])

        res[level].append(node.val)
        self._dfs(res, node.left, level + 1)
        self._dfs(res, node.right, level + 1)