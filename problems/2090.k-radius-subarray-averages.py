#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        # cur_k = 0
        # cur_sum = 0
        # res = []
        # for i, n in enumerate(nums):
        #     cur_k += 1
        #     cur_sum += n
        #     if cur_k < k:
        #         res.append(-1)
        #     else:
        #         res.append(cur_sum)
        # res = [-1] * len(nums)

        # left, cur_sum, diameter = 0, 0, 2 * k + 1
        # for right in range(len(nums)):
        #     cur_sum += nums[right]
        #     if (right - left + 1 >= diameter):
        #         res[left + k] = cur_sum
        #         cur_sum -= nums[left]
        #         left += 1
        # return res
        res = [-1]*len(nums)

        left, curWindowSum, diameter = 0, 0, 2*k+1
        for right in range(len(nums)):
            curWindowSum += nums[right]
            if (right-left+1 >= diameter):
                res[left+k] = curWindowSum//diameter
                curWindowSum -= nums[left]
                left += 1
        return res
            


# @lc code=end

