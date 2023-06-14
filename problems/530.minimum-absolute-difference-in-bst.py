#
# @lc app=leetcode id=530 lang=python3
#
# [530] Minimum Absolute Difference in BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def dfs(node):
            if not node:
                return 
            values.append(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        values.sort()

        res = float('Inf')
        for i in range(1, len(values)):
            res = min(res, values[i] - values[i - 1])
        return res

        
# @lc code=end

