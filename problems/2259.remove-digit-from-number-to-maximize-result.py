#
# @lc app=leetcode id=2259 lang=python3
#
# [2259] Remove Digit From Number to Maximize Result
#

# @lc code=start
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = 0

        for n in range(1, len(number)):
            if number[n - 1] == digit:
                if int(number[n]) > int(number[n - 1]):
                    return number[:n - 1] + number[n:]
                else:
                    last = n - 1

        if number[-1] == digit:
            last = len(number) - 1
        return number[:last] + number[last + 1:]
# @lc code=end

