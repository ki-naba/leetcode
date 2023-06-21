#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#

# @lc code=start
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        arr = sorted(zip(nums, cost))
        total, count = sum(cost), 0
        for num, c in arr:
            count += c
            if count > total // 2:
                target = num
                break
        return sum(c * abs(num - target) for num, c in arr)
# @lc code=end

