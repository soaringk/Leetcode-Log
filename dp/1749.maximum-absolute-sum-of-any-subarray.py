#
# @lc app=leetcode id=1749 lang=python3
#
# [1749] Maximum Absolute Sum of Any Subarray
#
from itertools import accumulate


# @lc code=start
class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # 方法一、dp
        # 定义 f[i] 为以 i 元素结尾的最大绝对值
        # f[i] = max(f[i-1] + nums[i], nums[i], 0)

        # 方法二、前缀和
        # 子数组的和等于两个前缀和的差 s[j]−s[i]。所以子数组和的绝对值等于: ∣s[j]−s[i]∣
        # s[i] 和 s[j] 相差越大，上式也就越大。
        # 最大的差来自 s 中的最大值和最小值，所以答案为: max(s)−min(s)
        s = list(accumulate(nums, initial=0))
        return max(s) - min(s)


# @lc code=end
