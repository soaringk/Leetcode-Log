#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List
# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 假设加法的总和为 x 有
        # x = (S + sum) / 2
        sum_nums = sum(nums)
        if S > sum_nums or (S + sum_nums) % 2 == 1:
            return 0

        size = (S + sum_nums) // 2
        n = len(nums)

        def subset_knapsack_2D():
            # dp[i][j]定义为用前 i 个物品填满 j 这么大的包，有dp[i][j]种方法
            dp = [[0] * (size + 1) for _ in range(n + 1)]

            # init
            # dp[0] = ...
            for t in range(n):
                dp[t][0] = 1

            for i in range(1, n + 1):
                for j in range(size + 1):
                    if j >= nums[i - 1]:
                        dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                    else: # 背包空间不足
                        dp[i][j] = dp[i - 1][j]

            return dp[n][size]

        def subset_knapsack_1D():
            # dp[j]定义为填满j（包括j）这么大容积的包，有dp[j]种方法
            dp = [0 for _ in range(size + 1)]
            dp[0] = 1

            for i in range(n):
                for j in range(size, nums[i] - 1, -1):
                    dp[j] += dp[j - nums[i]]

            return dp[size]

        # return subset_knapsack_1D()
        return subset_knapsack_2D()


    def backtrack(self, nums, S):
        if not nums:
            return 0

        path = []
        choice = 0

        def backtrack(i):
            if i == len(nums):
                if sum(path) == S:
                    nonlocal choice
                    choice += 1
                return

            for f in (1, -1):
                path.append(nums[i] * f)
                backtrack(i + 1)
                path.pop()

        backtrack(0)

        return choice

# @lc code=end
s = Solution()
s.findTargetSumWays([1000], -1000)
