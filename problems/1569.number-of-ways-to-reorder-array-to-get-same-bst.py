#
# @lc app=leetcode id=1569 lang=python3
#
# [1569] Number of Ways to Reorder Array to Get Same BST
#
# copied editorial answer 

# @lc code=start
class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        def dfs(nums):
            m = len(nums)
            if m <= 2:
                return 1
            left_nodes = [a for a in nums if a < nums[0]]
            right_node = [a for a in nums if a > nums[0]]
            return dfs(left_nodes) * dfs(right_node) * comb(m - 1, len(left_nodes)) % mod
        return (dfs(nums) - 1) % mod
# @lc code=end

