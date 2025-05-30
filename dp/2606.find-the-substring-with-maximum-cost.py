#
# @lc app=leetcode id=2606 lang=python3
#
# [2606] Find the Substring With Maximum Cost
#
from typing import List


# @lc code=start
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        mapping = dict(zip(chars, vals))
        # 定义 f[i] 为以 i 元素结尾的最大 cost
        # f[i] = max(f[i-1] + s[i], s[i])
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = max(0, mapping.get(s[0], ord(s[0]) - ord("a") + 1))
        for i in range(1, n):
            cost = mapping.get(s[i], ord(s[i]) - ord("a") + 1)
            dp[i] = max(dp[i-1] + cost, cost, 0)
        return max(dp)


# @lc code=end
Solution().maximumCostSubstring("kqqqqqkkkq", "kq", [-6, 6])
