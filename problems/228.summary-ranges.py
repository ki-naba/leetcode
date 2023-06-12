#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#

# @lc code=start
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        l, r = 0, 0
        while l < len(nums) and r < len(nums):
            if r + 1 < len(nums) and nums[r] + 1 == nums[r + 1]:
                r += 1
            else:
                if l == r:
                    ans.append(str(nums[l]))
                    l += 1
                    r += 1
                else:
                    ans.append(str(nums[l])+'->'+str(nums[r]))
                    l = r + 1
                    r += 1
        return ans

        
# @lc code=end

