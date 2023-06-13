#
# @lc app=leetcode id=2261 lang=python3
#
# [2261] K Divisible Elements Subarrays
#

# @lc code=start
class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        n = len(nums)
        sub_arrays = set()

        for i in range(n):
            count = 0
            temp = ''
            for j in range(i, n):
                if nums[j] % p == 0:
                    count += 1
                temp += str(nums[j]) + ','
                if count > k:
                    break
                sub_arrays.add(temp)
        
        return len(sub_arrays)
# @lc code=end

