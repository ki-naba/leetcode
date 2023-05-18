#
# @lc app=leetcode id=1557 lang=python3
#
# [1557] Minimum Number of Vertices to Reach All Nodes
#

# @lc code=start
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans = set(range(n))
        for e in edges:
            if e[1] in ans:
                ans.remove(e[1])
        return list(ans)
    
#   telling from examples, I noticed unreachable edges are the expected outputs.


# @lc code=end

