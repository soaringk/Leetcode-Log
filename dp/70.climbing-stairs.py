#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # 定义 dp[i] 为到达第 i 层的不同方法数
        # dp[i] = dp[i-1]+1 + dp[i-2]+1
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]

# @lc code=end
Solution().climbStairs(2)