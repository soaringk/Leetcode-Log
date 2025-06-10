#
# @lc app=leetcode id=918 lang=python3
#
# [918] Maximum Sum Circular Subarray
#
from typing import List
import math

# @lc code=start
class Solution:
    # 两种思路：
    # 1. 数组后面插入一个相同数组解决环形数组问题
    # 2. 分类讨论，发现答案是简洁的 max(max_s, sum(nums) - min_s) / max_s
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_s = -math.inf  # 最大子数组和，不能为空
        min_s = 0     # 最小子数组和，可以为空
        max_f = min_f = 0
        for x in nums:
            # 以 nums[i-1] 结尾的子数组选或不选（取 max）+ x = 以 x 结尾的最大子数组和
            max_f = max(max_f, 0) + x
            max_s = max(max_s, max_f)
            # 以 nums[i-1] 结尾的子数组选或不选（取 min）+ x = 以 x 结尾的最小子数组和
            min_f = min(min_f, 0) + x
            min_s = min(min_s, min_f)
        if sum(nums) == min_s: # 特殊情况，最小子数组就是整个数组，那么最大子数组就是空的，是题目非法的情况，直接不关注
            return max_s
        return max(max_s, sum(nums) - min_s)
# @lc code=end

