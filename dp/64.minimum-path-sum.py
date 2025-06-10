#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#
from typing import List
from math import inf


# @lc code=start
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 定义 f[i+1][j+1] 表示从左上角到第 i 行第 j 列这个格子（记作 (i,j)）的最小价值和。
        # f[i+1][j+1] = min(f[i][j+1] + grid[i][j], f[i+1][j] + grid[i][j])
        # f[0][j] 和 f[i][0] 都需要初始化
        m, n = len(grid), len(grid[0])
        dp = [[inf] * (n + 1) for _ in range(m + 1)]
        dp[0][1] = 0
        dp[1][0] = 0
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                dp[i + 1][j + 1] = min(dp[i + 1][j], dp[i][j + 1]) + x
        return dp[m][n]


# @lc code=end
