#
# @lc app=leetcode id=2260 lang=python3
#
# [2260] Minimum Consecutive Cards to Pick Up
#

# @lc code=start
class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        res = len(cards) + 1
        seen = {}
        for i, n in enumerate(cards):
            if n in seen:
                res = min(res, i - seen[n] + 1)
            seen[n] = i
        if res > len(cards):
            return -1
        else:
            return res
            
# @lc code=end

