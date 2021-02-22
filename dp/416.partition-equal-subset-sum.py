#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        # 给一个可装载重量为 sum / 2 的背包和 N 个物品，每个物品的重量为 nums[i]。
        n = len(nums)
        target //= 2

        dp = [[False for _ in range(target + 1)] for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if j - nums[i - 1] < 0:
                    dp[i][j] = dp[i - 1][j]  # 不把物品 i 装进背包
                else:
                    dp[i][j] = dp[i - 1][j] or \
                        dp[i - 1][j - nums[i - 1]]

        return dp[n][target]


# @lc code=end
s = Solution()
s.canPartition([1,2,5])
