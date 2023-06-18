#
# @lc app=leetcode id=2328 lang=python3
#
# [2328] Number of Increasing Paths in a Grid
#

# @lc code=start
class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        res = 0
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(row, col, prev, dp, grid):
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] <= prev:
                return 0
            if dp[row][col] != -1:
                return dp[row][col]
            ans = 1
            for di in directions:
                newRow, newCol = row + di[0], col + di[1]
                ans += dfs(newRow, newCol, grid[row][col], dp, grid)
            dp[row][col] = ans
            return ans
        
        for row in range(rows):
            for col in range(cols):
                res += dfs(row, col, -1, dp, grid)
        
        return res % (10 ** 9 + 7)
        
# @lc code=end

