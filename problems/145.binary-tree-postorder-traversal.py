#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        bag = [root]
        if not root:return []
        
        while bag:
            node = bag.pop()
            ans.append(node.val)

            if node.left:
                bag.append(node.left)
            if node.right:
                bag.append(node.right)
            
        return ans[::-1]
        
# @lc code=end

