#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#


# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 定义 f[i] 表示以 nums[i] 结尾的最大子数组和。
        if not nums: return 0
        dp = [-1 for _ in nums]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])

        return max(dp)


# @lc code=end
