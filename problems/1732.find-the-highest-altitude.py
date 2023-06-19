#
# @lc app=leetcode id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        cur = 0
        for g in gain:
            cur += g
            res = max(cur, res)
        return res
# @lc code=end

