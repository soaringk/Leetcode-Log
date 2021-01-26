#
# @lc app=leetcode id=198 lang=python3
#
# [198] House Robber
#


# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0 for x in range(len(nums) + 2)]

        for i in range(len(nums)):
            dp[i + 2] = max(dp[i] + nums[i], dp[i + 1])

        return dp[-1]

    def rop_recursive(self, nums):
        memo = [-1 for x in range(len(nums))]

        def dp(nums, start):
            if start >= len(nums): return 0

            if memo[start] != 1: return memo[start]

            res = max(
                # 抢
                nums[start] + dp(nums, start + 2),
                # 不抢
                dp(nums, start + 1))
            memo[start] = res
            return res
        return dp(nums, 0)


# @lc code=end
