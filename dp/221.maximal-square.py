#
# @lc app=leetcode id=221 lang=python3
#
# [221] Maximal Square
#
from typing import List


# @lc code=start
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 定义 f[i][j] 为以 i, j 为右下角的最大矩形的边长
        # f[i][j] = min(f[i-1][j], f[i-1][j-1], f[i][j-1]) + 1 ，即左、左上、上的最小值
        # 边界情况：1. 如果 matrix[i][j] 为 0，那么为 0。且其他格子为 0 时，最大为 1
        # 2. 如果左、上出界，那么最多为 1
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        maxSide = 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                    maxSide = max(maxSide, dp[i][j])
        return maxSide**2


# @lc code=end
