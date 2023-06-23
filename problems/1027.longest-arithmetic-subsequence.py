#
# @lc app=leetcode id=1027 lang=python3
#
# [1027] Longest Arithmetic Subsequence
#

# @lc code=start
class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = {}
        for i, a2 in enumerate(nums[1:], start=1):
            for j, a1 in enumerate(nums[:i]):
                d = a2 - a1
                if (j, d) in dp:
                    dp[i, d] = dp[j, d] + 1
                else:
                    dp[i, d] = 2
        return max(dp.values())
# @lc code=end

