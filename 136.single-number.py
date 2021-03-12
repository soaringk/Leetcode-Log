#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
from functools import reduce
class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        single = reduce(lambda x, y: x ^ y, nums)

        return single
# @lc code=end
