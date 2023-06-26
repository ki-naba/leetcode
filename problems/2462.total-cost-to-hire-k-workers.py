#
# @lc app=leetcode id=2462 lang=python3
#
# [2462] Total Cost to Hire K Workers
#

# @lc code=start
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        q = costs[:candidates]
        qq = costs[max(candidates, len(costs)-candidates):]
        heapify(q)
        heapify(qq)
        ans = 0 
        i, ii = candidates, len(costs)-candidates-1
        for _ in range(k): 
            if not qq or q and q[0] <= qq[0]: 
                ans += heappop(q)
                if i <= ii: 
                    heappush(q, costs[i])
                    i += 1
            else: 
                ans += heappop(qq)
                if i <= ii: 
                    heappush(qq, costs[ii])
                    ii -= 1
        return ans 
        
# @lc code=end

