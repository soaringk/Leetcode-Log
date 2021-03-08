#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#

# @lc code=start
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [i for i in range(n + 1)]

        for i in range(1, n + 1):
            j = 1
            while i - j**2 >= 0:
                dp[i] = min(dp[i], dp[i - j**2] + 1)
                j += 1

        return dp[n]
# @lc code=end
s = Solution()
s.numSquares(7927)
