#
# @lc app=leetcode id=547 lang=python3
#
# [547] Number of Provinces
#

# @lc code=start

# since matrix is symetoric, iteration begins from i + 1
# 
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        
        n = len(isConnected)
        visited = [False] * n

        def dfs(u):
            for v in range(n):
                if isConnected[u][v] == 1 and visited[v] == False:
                    visited[v] = True
                    dfs(v)
        
        count = 0

        for i in range(n):
            if visited[i] == False:
                visited[i] = True
                count += 1
                dfs(i)

        return count
# @lc code=end

