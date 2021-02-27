#
# @lc app=leetcode id=931 lang=python3
#
# [931] Minimum Falling Path Sum
#
from typing import List
# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        # dp[i][j] -> 从 matrix[0][:] 向下落，到位置 matrix[i][j] 的最小路径和
        dp = [[float('inf') for _ in range(n + 2)] for _ in range(n)]
        dp[0] = [x for x in matrix[0]]
        dp[0].insert(0, float('inf'))
        dp[0].append(float('inf'))

        for i in range(1, n):
            for j in range(1, n + 1):
                dp[i][j] = matrix[i][j - 1] + min(
                    dp[i - 1][j],
                    dp[i - 1][j - 1],
                    dp[i - 1][j + 1]
                )

        return min(dp[n - 1])

# @lc code=end
s = Solution()
s.minFallingPathSum([[69]])
