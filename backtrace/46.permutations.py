#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#
from typing import List
# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        track = []
        res = []

        def backtack(nums, track):
            if len(nums) == 0:
                res.append(track[:])
                return

            for i in nums:
                track.append(i)
                backtack([x for x in nums if x != i], track)
                track.remove(i)

        backtack(nums, track)

        return res


# @lc code=end
