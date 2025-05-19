#
# @lc app=leetcode id=213 lang=python3
#
# [213] House Robber II
#
from typing import List


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        # 条件：
        # 1. 偷nums[0], 那么 nums[1] 和 nums[n−1] 不能偷，i 的范围是 2...n-2，最后再加上 nums[0]
        # 2. 不偷nums[0]，那么 nums[1] 和 nums[n−1] 可以偷，i 的范围是 1...n-1
        return max(self.rob_linear(nums[2:-1]) + nums[0], self.rob_linear(nums[1:]))

    def rob_linear(self, nums: List[int]) -> int:
        # 定义 dp[i+2] 抢前 i 家的最大金额
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        n = len(nums)
        dp = [0] * (n + 2)
        for i in range(n):
            dp[i + 2] = max(dp[i + 1], dp[i] + nums[i])
        return dp[-1]

    def rob_recursive(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(nums):
            memo = [0 for x in range(len(nums) + 2)]

            for i in range(len(nums)):
                memo[i + 2] = max(memo[i] + nums[i], memo[i + 1])

            return memo[-1]

        return max(dp(nums[:-1]), dp(nums[1:]))


# @lc code=end
s = Solution()
s.rob([1])
