#
# @lc app=leetcode id=2542 lang=python3
#
# [2542] Maximum Subsequence Score
#

# @lc code=start
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        total = res = 0
        heap = []

        paris = zip(nums1, nums2)

        sorted_pairs = sorted(paris, key = itemgetter(1), reverse= True)

        for pair in sorted_pairs:
            num1, num2 = pair
            heappush(heap, num1)
            total += num1
            if len(heap) > k:
                total -= heappop(heap)
            if len(heap) == k:
                res = max(total * num2, res)
        
        return res
# @lc code=end

