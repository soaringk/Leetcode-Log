#
# @lc app=leetcode id=188 lang=python3
#
# [188] Best Time to Buy and Sell Stock IV
#
# 状态机
# from typing import List


# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n < 2: return 0
        dp = [[[0, float('-inf')] for y in range(k + 1)] for z in range(n)]

        for i in range(n):
            for j in range(k, 0, -1):
                if i - 1 == -1:  # base case
                    dp[i][j][0] = 0
                    dp[i][j][1] = -prices[i]
                    continue
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1],
                                  dp[i - 1][j - 1][0] - prices[i])
        return dp[n - 1][k][0]


# @lc code=end
# S = Solution()
# S.maxProfit(2, [3, 3, 5, 0, 0, 3, 1, 4])
