#
# @lc app=leetcode id=837 lang=python3
#
# [837] New 21 Game
#

# @lc code=start
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        dp = [0] * (n + 1)
        dp[0] = 1

        if k > 0:
            s = 1
        else:
            s = 0

        for i in range(1, n + 1):
            dp[i] = s/maxPts
            if i < k:
                s += dp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                s -= dp[i - maxPts]
        return sum(dp[k:])
# @lc code=end

