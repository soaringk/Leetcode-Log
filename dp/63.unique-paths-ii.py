#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#
from typing import List


# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # 定义 f[i+1][j+1] 为走到 i, j 的方案数
        # f[i+1][j+1] = f[i][j+1] + f[i+1][j] if i, j 没有障碍
        # f[i+1][j+1] = 0 if 有障碍
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 1
        for i in range(m):
            for j in range(n):
                dp[i + 1][j + 1] = dp[i][j + 1] + dp[i + 1][j] if obstacleGrid[i][j] != 1 else 0
        return dp[m][n]


# @lc code=end
