#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # 求和必须能被 2 整除才能等分
        s = sum(nums)
        if s % 2:
            return False

        target = s // 2
        # 定义 f[i+1][j] 是 target = j 时，前 i 个元素是否能满足条件的矩阵
        # f[i+1][j] = f[i][j-nums[i]] or f[i][j] if j > x
        n = len(nums)
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i, x in enumerate(nums):
            for j in range(target + 1):
                if j >= x:
                    dp[i + 1][j] = dp[i][j - x] or dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j]
        return dp[n][target]


# @lc code=end
