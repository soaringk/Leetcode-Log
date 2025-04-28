#
# @lc app=leetcode id=2080 lang=python3
#
# [2080] Range Frequency Queries
#
from typing import List
from collections import defaultdict


# @lc code=start
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        pos = defaultdict(list)
        for i, x in enumerate(arr):
            pos[x].append(i)
        self.pos = pos
        # 转换成下标列表中，满足 left ≤ i ≤ right 的下标 i 的个数。

    def query(self, left: int, right: int, value: int) -> int:
        idx = self.pos[value]
        l = self.binsearch(idx, left)
        r = self.binsearch(idx, right + 1)
        return r - l

    def binsearch(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
# @lc code=end
obj = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56])
param_1 = obj.query(1,2,4)
