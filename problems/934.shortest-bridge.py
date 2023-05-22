#
# @lc app=leetcode id=934 lang=python3
#
# [934] Shortest Bridge
#

# @lc code=start

# 最初に島がある位置をdfsで集める
# 次にbfsで島があるところを島がないところを探す
# 上下4か所のなめ方や、適したデータ構造などを復習できる
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        i, j = next( (i, j) for i in range(m) for j in range(n) if grid[i][j])

        stack = [(i, j)]
        seen = set(stack)
        while stack:
            i, j = stack.pop()
            seen.add((i, j))
            for ii , jj in (i - 1, j), (i, j - 1), (i, j + 1), (i + 1, j):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] and (ii, jj) not in seen:
                    stack.append((ii, jj))
                    seen.add((ii, jj))

        ans = 0
        queue = list(seen)
        while queue:
            newq = []
            for i, j in queue:
                for ii, jj in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                    if 0 <= ii < m and 0 <= jj < n and (ii, jj) not in seen:
                        if grid[ii][jj] == 1: return ans
                        newq.append((ii, jj))
                        seen.add((ii, jj))
            queue = newq
            ans += 1
# @lc code=end

