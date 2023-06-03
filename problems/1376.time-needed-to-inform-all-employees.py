#
# @lc app=leetcode id=1376 lang=python3
#
# [1376] Time Needed to Inform All Employees
#

# @lc code=start
class Solution:
    def dfs(self, manager, informTime, adjList):
        maxTime = 0
        for subo in adjList[manager]:
            maxTime = max(maxTime, self.dfs(subo, informTime, adjList))
        return maxTime + informTime[manager]
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adjList = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                adjList[manager[i]].append(i)
        
        return self.dfs(headID, informTime, adjList)
# @lc code=end

