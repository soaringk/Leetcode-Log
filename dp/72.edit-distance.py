#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistanceRecursive(self, word1: str, word2: str) -> int:
        # 返回 word1[0:i] 和 word2[0:j] 的最小编辑距离

        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == -1: return j + 1
            if j == -1: return i + 1

            if word1[i] == word2[j]:
                memo[(i, j)] = dp(i - 1, j - 1) # 什么也不做
            else:
                memo[(i, j)] = min(
                    dp(i, j - 1) + 1,   # 插入
                    dp(i - 1, j) + 1,   # 删除
                    dp(i - 1, j - 1) + 1    # 替换
                )
            return memo[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        dp = [[float('inf') for _ in range(m + 1)] for _ in range(n + 1)]
        dp[0] = [i for i in range(m + 1)]
        for i in range(n + 1):
            dp[i][0] = i

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i - 1][j] + 1,
                        dp[i][j - 1] + 1,
                        dp[i - 1][j - 1] + 1,
                    )

        return dp[n][m]

# @lc code=end
