#
# @lc app=leetcode id=2320 lang=python3
#
# [2320] Count Number of Ways to Place Houses
#

# @lc code=start
class Solution:
    def countHousePlacements(self, n: int) -> int:
        # 定义 dp[i+2] 抢前 i 根线的方案数
        # dp[i] = max(dp[i-1], dp[i-2] + nums[i-2])
        # 由于两侧的房屋互相独立，根据乘法原理，答案为 f[n]^2
        MOD = 1_000_000_007
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2]) % MOD
        return (dp[n] * dp[n]) % MOD
        
# @lc code=end

