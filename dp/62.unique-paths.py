#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#


# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 定义 f[i+1][j+1] 是走到 i, j 格子的方案数
        # f[i+1][j+1] = f[i][j+1] + f[i+1][j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # 如果不写 f[0][1]=1，那么需要在代码中特判 i=j=0 的情况，因为 f[1][1] 属于初始值，不能用状态转移方程计算。
        # 但是，如果把初始值改成 f[0][1]=1（或者 f[1][0]=1），就无需特判 i=j=0 的情况了，f[1][1] 也可以用状态转移方程计算。
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j]
        return dp[m][n]


# @lc code=end
