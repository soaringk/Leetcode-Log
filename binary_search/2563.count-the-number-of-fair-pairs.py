#
# @lc app=leetcode id=2563 lang=python3
#
# [2563] Count the Number of Fair Pairs
#
from typing import List

# @lc code=start
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for j, x in enumerate(nums):
            li = self.binsearch_left(nums[:j], lower - x)
            ri = self.binsearch_right(nums[:j], upper - x)
            ans += ri - li
        return ans

    def binsearch_left(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1

    def binsearch_right(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return right + 1


# @lc code=end
print(Solution().countFairPairs([0,1,7,4,4,5],3,6))
