#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def dp(nums):
            memo = [0 for x in range(len(nums) + 2)]

            for i in range(len(nums)):
                memo[i + 2] = max(memo[i] + nums[i], memo[i + 1])

            return memo[-1]

        return max(dp(nums[:-1]), dp(nums[1:]))


# @lc code=end
s = Solution()
s.rob([1])
