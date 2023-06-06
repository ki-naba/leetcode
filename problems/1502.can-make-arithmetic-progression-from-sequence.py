#
# @lc app=leetcode id=1502 lang=python3
#
# [1502] Can Make Arithmetic Progression From Sequence
#

# @lc code=start
class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        diff = arr[0] - arr[1]
        for i in range(2, len(arr)):
            if diff != arr[i - 1] - arr[i]:
                return False
        return True
# @lc code=end

