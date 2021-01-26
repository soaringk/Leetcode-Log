#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
from typing import List

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_bound():
            if len(nums) == 0:
                return -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1

            if l >= len(nums) or nums[l] != target:
                return -1
            return l

        def find_right_bound():
            if len(nums) == 0:
                return -1
            l = 0
            r = len(nums) - 1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    l = mid + 1
                elif nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1

            if r >= len(nums) or nums[r] != target:
                return -1
            return r

        left_bound = find_left_bound()
        right_bound = find_right_bound()

        return [left_bound, right_bound]


# @lc code=end
S = Solution()
S.searchRange([5, 7, 7, 8, 8, 10], 8)
