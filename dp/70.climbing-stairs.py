#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1 for _ in range(n + 1)]
        # 状态转移：n 可以从 n - 2 或者 n - 1 踏一步上来
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]


# @lc code=end
Solution().climbStairs(4)
