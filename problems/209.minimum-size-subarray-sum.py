#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        res = len(nums) + 1
        total = nums[0]
        while r < len(nums):
            if total < target:
                r += 1
                if r < len(nums):
                    total += nums[r]
            elif total >= target:
                res = min(r - l + 1, res)
                total -= nums[l]
                l += 1

        return res if res <= len(nums) else 0
# @lc code=end

