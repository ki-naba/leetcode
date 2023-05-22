#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        cur = root
        
        def dfs(cur):
            if not cur:
                return
            ans.append(cur.val)
            dfs(cur.left)
            dfs(cur.right)
        
        dfs(cur)

        return ans
        
# @lc code=end

