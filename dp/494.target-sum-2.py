#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#
from typing import List


# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # 思考：
        # 添加正号的元素之和为 p，其余添加负号的元素（绝对值）之和为 q，那么有：p + q = S
        # 又因为表达式运算结果等于 target，所以有：p − q = target
        # 解得：p = (S + target)/2, q = (S - target)/2 可以计算出来了
        # 问题转为正号元素和为 p（负号元素和为 q）的方案数
        # 根据 target是正负数还得分情况讨论取 p 还是取 q，综合考虑可以直接取 (S - |target|)/2

        """
        特殊情况：
        设 s = S - |target|。
            如果 s < 0，由于 nums[i] ≥ 0，我们无法得到负数，方案数是 0。
            如果 s 是奇数，由于 nums[i] 都是整数，我们无法得到非整数 s/2，方案数是 0。
        """
        S = sum(nums)
        s = S - abs(target)
        if s < 0 or s % 2 != 0:
            return 0

        s //= 2
        n = len(nums)
        # 定义：f[i+1][j] 为前 i 个元素求和为 j 的方案数
        # f[i+1][j] = f[i][j - x] + f[i][j]
        dp = [[0] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i, x in enumerate(nums):
            for j in range(s + 1):
                if j >= x:
                    dp[i + 1][j] = dp[i][j - x] + dp[i][j]
                else:
                    dp[i + 1][j] = dp[i][j]
        return dp[n][s]


# @lc code=end
Solution().findTargetSumWays([1, 1, 1, 1, 1], 3)
