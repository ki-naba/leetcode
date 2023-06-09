#
# @lc app=leetcode id=744 lang=python3
#
# [744] Find Smallest Letter Greater Than Target
#

# @lc code=start
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]

        left, right = 0, len(letters) - 1

        while left <= right:
            mid = (left + right) // 2
            if target >= letters[mid]:
                left = mid + 1
            if target < letters[mid]:
                right = mid - 1
        
        return letters[left]
# @lc code=end

