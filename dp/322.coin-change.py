#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#


# @lc code=start
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        # 定义：要凑出金额 n，至少要 dp(n) 个硬币
        def dp(n):
            if n in memo: return memo[n]
            # base case
            if n == 0: return 0
            if n < 0: return -1
            res = float('INF')  # 初始化
            # 做选择，选择需要硬币最少的那个结果
            for coin in coins:
                subproblem = dp(n - coin)
                # 无解
                if subproblem == -1: continue
                res = min(res, 1 + dp(n - coin))

            memo[n] = res if res != float('INF') else -1
            return memo[n]

        # 题目要求的最终结果是 dp(amount)
        return dp(amount)

    def bottomUp(self, coins, amount):
        # base case
        dp = [amount + 1 for x in range(amount + 1)]
        dp[0] = 0
        # 外层 for 循环在遍历所有状态的所有取值
        for i in range(amount + 1):
            # 内层 for 循环在求所有选择的最小值
            for coin in coins:
                # 子问题无解，跳过
                if i - coin < 0: continue
                dp[i] = min(dp[i], 1 + dp[i - coin])

        return dp[amount] if dp[amount] != amount + 1 else -1


# @lc code=end
