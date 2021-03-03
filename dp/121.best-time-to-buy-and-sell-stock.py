#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# 状态机
from typing import List
# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        dp_i_0 = 0
        dp_i_1 = float('-inf')
        for i in range(n):
            dp_i_0 = max(dp_i_0, dp_i_1 + prices[i])
            dp_i_1 = max(dp_i_1, -prices[i])
        return dp_i_0

    def normal(self, prices):
        res = 0
        buy_min = prices[0]
        for sell in range(1, len(prices)):
            buy_min = min(buy_min, prices[sell])
            res = max(res, prices[sell] - buy_min)
        return res


# @lc code=end
s = Solution()
s.normal([7, 1, 5, 3, 6, 4])
