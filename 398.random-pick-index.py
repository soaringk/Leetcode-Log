#
# @lc app=leetcode id=398 lang=python3
#
# [398] Random Pick Index
#
from typing import List

# @lc code=start
import random

class Solution:

    def __init__(self, nums: List[int]):
        idx_map = {}
        for idx, val in enumerate(nums):
            if val not in idx_map:
                idx_map[val] = [idx]
            else:
                idx_map[val].append(idx)

        self.map = idx_map

    def pick(self, target: int) -> int:
        idx_range = self.map[target]
        i = 0
        res = 0
        while i < len(idx_range):
            if random.randrange(i + 1) == 0:
                res = idx_range[i]
            i += 1

        return res



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)
# @lc code=end
