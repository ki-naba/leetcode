#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#

# 辞書型をうまく使う
# 辞書型のソートや配列にして出すことなど
# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
            
        sorted_freq = dict(sorted(freq.items(), key = lambda x:x[1], reverse=True))

        return list(sorted_freq.keys())[:k]
        
# @lc code=end

