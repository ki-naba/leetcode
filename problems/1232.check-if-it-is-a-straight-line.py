#
# @lc app=leetcode id=1232 lang=python3
#
# [1232] Check If It Is a Straight Line
#

# @lc code=start
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) == 2:
            return True
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]

        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if ((y1- y0) * (x0 - x)) != ((y0 - y) * (x1- x0)):
                return False
        return True


# @lc code=end

