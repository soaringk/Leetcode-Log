#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
from typing import List
# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        track = []

        def backtrack(nums, start, track):
            res.append(track[:])
            for i in range(start, len(nums)):
                track.append(nums[i])
                backtrack(nums, i + 1, track)
                track.pop()

        backtrack(nums, 0, track)
        return res

# @lc code=end
s = Solution()
s.subsets([1,2,3])
