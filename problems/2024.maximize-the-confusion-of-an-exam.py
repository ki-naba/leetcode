#
# @lc app=leetcode id=2024 lang=python3
#
# [2024] Maximize the Confusion of an Exam
#

# @lc code=start
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        def longestWin(c: str, k: int) -> int:
            lo, win = -1, 0
            for hi in range(len(answerKey)):
                if answerKey[hi] == c:
                    k -= 1
                while k < 0:
                    lo += 1
                    k += answerKey[lo] == c
                win = max(win, hi - lo)
            return win     

        return max(longestWin('T', k), longestWin('F', k))
# @lc code=end

