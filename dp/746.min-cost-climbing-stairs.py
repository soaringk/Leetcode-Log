#
# @lc app=leetcode id=746 lang=python3
#
# [746] Min Cost Climbing Stairs
#
from typing import List

# @lc code=start
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # dp[i] 爬到 i 的 cost 最小值
        # dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        n = len(cost)
        dp = ['inf'] * (n + 1)
        dp[0] = 0
        dp[1] = 0
        for i in range(2, n+1):
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i-2])
        return dp[n]
# @lc code=end

Solution().minCostClimbingStairs([10,15,20])