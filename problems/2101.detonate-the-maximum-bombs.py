#
# @lc app=leetcode id=2101 lang=python3
#
# [2101] Detonate the Maximum Bombs
#

# 辞書を使って近いところを貯めていく

# @lc code=start
class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        n = len(bombs)

        for i in range(n):
            for j in range(n):
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                if ri ** 2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)
        
        def dfs(i):
            stack = [i]
            visited = set()

            while stack:
                cur = stack.pop()
                for neib in graph[cur]:
                    if neib not in visited:
                        visited.add(neib)
                        stack.append(neib)

            return len(visited)
        
        answer = 0
        for i in range(n):
            answer = max(answer, dfs(i))

        return answer
# @lc code=end

