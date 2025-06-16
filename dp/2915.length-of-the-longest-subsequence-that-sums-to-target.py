#
# @lc app=leetcode id=2915 lang=python3
#
# [2915] Length of the Longest Subsequence That Sums to Target
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        # 定义 f[i+1][j] 为 前 i 个元素求和为 i 的最长子序列
        # f[i+1][j] = max(f[i][j], f[i][j-nums[i]] + 1)
        n = len(nums)
        dp = [[-inf] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(n):
            for j in range(target + 1):
                if j >= nums[i]:
                    dp[i + 1][j] = max(dp[i][j], dp[i][j - nums[i]] + 1)
                else:
                    dp[i + 1][j] = dp[i][j]
        return dp[n][target] if dp[n][target] > 0 else -1


# @lc code=end
Solution().lengthOfLongestSubsequence([1, 2], 10)
