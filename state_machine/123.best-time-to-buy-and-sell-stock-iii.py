#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# 状态机

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_i_10 = 0
        dp_i_20 = 0
        dp_i_11 = float('-inf')
        dp_i_21 = float('-inf')
        for i in range(n):
            dp_i_10 = max(dp_i_10, dp_i_11 + prices[i])
            dp_i_11 = max(dp_i_11, -prices[i])
            dp_i_20 = max(dp_i_20, dp_i_21 + prices[i])
            dp_i_21 = max(dp_i_21, dp_i_10 - prices[i])
        return dp_i_20


# @lc code=end
