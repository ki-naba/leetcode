#
# @lc app=leetcode id=137 lang=python3
#
# [137] Single Number II
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        once = set()
        twice = set()
        for n in nums:
            if n in once:
                twice.add(n)
                once.remove(n)
            elif n in twice:
                twice.remove(n)
            else:
                once.add(n)
        return once.pop()

# @lc code=end

