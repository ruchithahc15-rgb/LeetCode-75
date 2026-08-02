# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        prefix = {0: 1}
        def dfs(node, current):
            if not node:
                return 0
            current += node.val
            paths = prefix.get(current - targetSum, 0)
            prefix[current] = prefix.get(current, 0) + 1
            paths += dfs(node.left, current)
            paths += dfs(node.right, current)
            prefix[current] -= 1
            return paths
        return dfs(root, 0)
        