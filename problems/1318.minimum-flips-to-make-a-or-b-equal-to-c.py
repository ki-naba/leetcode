#
# @lc app=leetcode id=1318 lang=python3
#
# [1318] Minimum Flips to Make a OR b Equal to c
#

# @lc code=start

# bit manipulation
# shifting to right is "a >>= 1"
# a & 1 checks whether the most siginificant bit is 1 or not.
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        while a or b or c:
            if c & 1:
                if a & 1 or b & 1:
                    ans += 0
                else:
                    ans += 1
            else:
                ans += (a & 1) + (b & 1)
            a >>= 1
            b >>= 1
            c >>= 1
        return ans
        
# @lc code=end

