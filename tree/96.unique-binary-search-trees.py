#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#


# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            for j in range(n):
                # P(left tree) multiplied by P(right tree)
                dp[i] += dp[j] * dp[i - j - 1]

        return dp[n]

    def CatalanNums(self, n: int) -> int:
        res = 1
        for i in range(n + 1, 2 * n + 1):
            res = res * i / (i - n)
        return res / (n + 1)


# @lc code=end
s = Solution()
s.numTrees(3)
