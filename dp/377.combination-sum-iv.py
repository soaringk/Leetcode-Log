#
# @lc app=leetcode id=377 lang=python3
#
# [377] Combination Sum IV
#
from typing import List

# @lc code=start
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # 回溯肯定可以做
        # 但是存在重复计算的子树，因此用dp优化
        # 定义：dp[i] 为选项构成 i 的方案数量
        # dp[i] = sum(所有选项dp[i-选项])
        n = target
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range (1, n+1):
            for op in nums:
                if i - op >= 0:
                    dp[i] += dp[i-op]
        return dp[n]

    def combinationSum4Backtrace(self, nums: List[int], target: int) -> int:
        ans = 0
        def dfs(t):
            if t == 0:
                nonlocal ans
                ans += 1
            if t <= 0:
                return
            
            for op in nums:
                dfs(t-op)
        dfs(target)
        return ans
        
# @lc code=end

Solution().combinationSum4([1,2,3],4)