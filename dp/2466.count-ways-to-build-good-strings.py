#
# @lc app=leetcode id=2466 lang=python3
#
# [2466] Count Ways To Build Good Strings
#


# @lc code=start
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 1_000_000_007

        # 定义 f[i] 表示构造长为 i 的字符串的方案数
        # dp[i] = dp[i-zero] + dp[i-one]
        dp = [0] * (high + 1)
        dp[0] = 1
        for i in range(1, high+1):
            if i - zero >= 0:
                dp[i] = dp[i-zero]
            if i - one >= 0:
                dp[i] = (dp[i] + dp[i-one]) % MOD
        return sum(dp[low:high+1]) % MOD


# @lc code=end
